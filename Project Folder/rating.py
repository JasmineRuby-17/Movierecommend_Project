import pandas as pd
import numpy as np

# -----------------------------
# Load Movie Dataset
# -----------------------------
movies = pd.read_csv("D:/movie_recommendation_system/data/movie.csv")

num_users = 30
ratings_data = []

np.random.seed(42)

# -----------------------------
# Define user genre preferences
# -----------------------------
genre_pool = [
    "Action", "Drama", "Comedy",
    "Romance", "Crime", "Thriller",
    "Sports", "Family", "Fantasy",
    "Legal", "Sci-Fi"
]

# -----------------------------
# Generate Ratings (GENRE BASED)
# -----------------------------
for user_id in range(1, num_users + 1):

    # each user likes 2–3 genres
    liked_genres = np.random.choice(genre_pool, size=np.random.randint(2, 4), replace=False)

    for _, row in movies.iterrows():

        movie_id = row["movieId"]
        title = row["title"]
        genre = str(row["genres"])

        # check if movie matches user preference
        if any(g.lower() in genre.lower() for g in liked_genres):
            rating = round(np.random.uniform(4.0, 5.0), 1)  # liked movie
        else:
            rating = round(np.random.uniform(2.5, 4.2), 1)  # neutral movie

        ratings_data.append([user_id, movie_id, rating])

# -----------------------------
# Create DataFrame
# -----------------------------
ratings_df = pd.DataFrame(ratings_data, columns=["userId", "movieId", "rating"])

# -----------------------------
# Save File
# -----------------------------
ratings_df.to_csv("D:/movie_recommendation_system/data/rating.csv", index=False)

print("Genre-based rating dataset created successfully!")
print("Users:", num_users)
print("Movies:", movies.shape[0])
print("Total Ratings:", len(ratings_df))