import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# =============================
# LOAD DATA
# =============================
movies = pd.read_csv(r"D:\movie_recommendation_system\data\movie.csv")
ratings = pd.read_csv(r"D:\movie_recommendation_system\data\rating.csv")
tags = pd.read_csv(r"D:\movie_recommendation_system\data\tag.csv")


# =============================
# CLEAN DATA
# =============================
movies = movies.drop_duplicates(subset='title')
ratings = ratings.drop(columns=['timestamp'], errors='ignore')
tags = tags.drop(columns=['timestamp'], errors='ignore')


# =============================
# MERGE DATA
# =============================
data = pd.merge(ratings, movies, on="movieId")

# Sample safely
data = data.sample(min(30000, len(data)), random_state=42)

print("Data shape:", data.shape)


# =============================
# USER-MOVIE MATRIX
# =============================
user_movie_matrix = data.pivot_table(
    index='userId',
    columns='title',
    values='rating'
).fillna(0).astype('float32')


# =============================
# MOVIE-BASED FILTERING
# =============================
movie_similarity = cosine_similarity(user_movie_matrix.T)

movie_similarity_df = pd.DataFrame(
    movie_similarity,
    index=user_movie_matrix.columns,
    columns=user_movie_matrix.columns
)


def recommend_by_movie(movie_name, top_n=5):
    movie_name = movie_name.strip().lower()

    # better matching
    matches = [m for m in movie_similarity_df.columns if movie_name in m.lower()]

    if not matches:
        suggestions = [m for m in movie_similarity_df.columns if movie_name[:3] in m.lower()]
        return ["Movie not found ❌", suggestions[:5]]

    matches = sorted(matches)   # FIX: stable output
    movie_name = matches[0]

    similar = movie_similarity_df[movie_name].sort_values(ascending=False)
    return similar.iloc[1:top_n+1].index.tolist()


# =============================
# USER-BASED FILTERING
# =============================
user_similarity = cosine_similarity(user_movie_matrix)

user_similarity_df = pd.DataFrame(
    user_similarity,
    index=user_movie_matrix.index,
    columns=user_movie_matrix.index
)


def recommend_by_user(user_id, top_n=5):
    if user_id not in user_movie_matrix.index:
        return ["User not found"]

    similar_users = user_similarity_df[user_id].sort_values(ascending=False)
    nearest_users = similar_users.iloc[1:6].index

    recommendations = set()

    for u in nearest_users:
        similar_user_movies = set(
            user_movie_matrix.loc[u][user_movie_matrix.loc[u] >= 4].index
        )
        recommendations.update(similar_user_movies)

    user_movies = set(
        user_movie_matrix.loc[user_id][user_movie_matrix.loc[user_id] >= 3].index
    )

    final_recommendations = list(recommendations - user_movies)

    return final_recommendations[:top_n]

#Content based filtering

def recommend_content_based(movie_name, top_n=5):
    movie_name = movie_name.strip().lower()

    # find matching movie
    matches = [m for m in movies['title'] if movie_name in m.lower()]

    if not matches:
        return [
            "Movie not found ❌",
            "Try like:",
            movies['title'].head(5).tolist()
        ]

    selected_movie = matches[0]

    # get genre of selected movie
    movie_genre = movies[movies['title'] == selected_movie]['genres'].values[0]

    # find similar movies by same genre
    filtered = movies[
        movies['genres'].str.lower().str.contains(movie_genre.lower())
    ]

    # remove the selected movie itself
    filtered = filtered[filtered['title'] != selected_movie]

    return filtered['title'].head(top_n).tolist()