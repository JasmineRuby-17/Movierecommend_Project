import pandas as pd
import numpy as np

# -----------------------------
# Load Movie Dataset
# -----------------------------
movies = pd.read_csv("D:/movie_recommendation_system/data/movie.csv")

num_users = 30
tags_data = []

np.random.seed(42)

# -----------------------------
# Genre → Tag Mapping (ALIGNED with rating.py)
# -----------------------------
movie_tag_map = {
    "action": ["mass", "fight", "hero", "revenge", "stunts"],
    "drama": ["emotional", "realistic", "family", "sentiment"],
    "comedy": ["fun", "laugh", "entertainment", "humor"],
    "romance": ["love", "emotional", "romantic", "heartbreak"],
    "crime": ["gangster", "police", "thriller", "investigation"],
    "thriller": ["suspense", "mystery", "dark", "twist"],
    "sports": ["game", "victory", "team", "champion"],
    "family": ["family", "bond", "sentiment", "emotional"],
    "fantasy": ["magic", "myth", "heroic", "adventure"],
    "legal": ["court", "justice", "law", "verdict"],
    "sci-fi": ["future", "robot", "space", "technology"]
}

# -----------------------------
# Generate Tags
# -----------------------------
for user_id in range(1, num_users + 1):

    # each user watches random movies
    movie_ids = np.random.choice(movies["movieId"], size=15, replace=False)

    for movie_id in movie_ids:

        genre = str(movies.loc[movies["movieId"] == movie_id, "genres"].values[0])

        genre_lower = genre.lower()

        matched = False

        # assign tag based on genre match
        for g in movie_tag_map:
            if g in genre_lower:
                tag = np.random.choice(movie_tag_map[g])
                tags_data.append([user_id, movie_id, tag])
                matched = True
                break

        # fallback tag if genre not found
        if not matched:
            tags_data.append([user_id, movie_id, "general"])

# -----------------------------
# Create DataFrame
# -----------------------------
tags_df = pd.DataFrame(tags_data, columns=["userId", "movieId", "tag"])

# -----------------------------
# Save File
# -----------------------------
tags_df.to_csv("D:/movie_recommendation_system/data/tag.csv", index=False)

print("✅ Tag dataset created successfully!")
print("Users:", num_users)
print("Movies:", movies.shape[0])
print("Total Tags:", len(tags_df))