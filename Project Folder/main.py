# =============================
# CLI INTERFACE
# =============================

from recommender import (
    recommend_by_movie,
    recommend_by_user,
    recommend_content_based
)

from recommender import user_movie_matrix
from recommender import movie_similarity_df


# =============================
# SYSTEM INFO
# =============================
print("Total Users:", len(user_movie_matrix.index))
print("Total Movies:", len(movie_similarity_df.columns))


# =============================
# MAIN MENU LOOP
# =============================
while True:
    print("\n🎬 MOVIE RECOMMENDER")
    print("1. Movie-Based")
    print("2. User-Based")
    print("3. Content-Based")
    print("4. Exit")

    choice = input("Enter choice: ")

    # -----------------------------
    # MOVIE-BASED RECOMMENDATION
    # -----------------------------
    if choice == "1":
        movie = input("Enter movie name (e.g., Master, Vikram, 96): ").strip()
        print(recommend_by_movie(movie))

    # -----------------------------
    # USER-BASED RECOMMENDATION
    # -----------------------------
    elif choice == "2":
        try:
            user = int(input("Enter user ID (e.g., 1–30): "))
            print(recommend_by_user(user))
        except:
            print("Invalid user ID")

    # -----------------------------
    # CONTENT-BASED RECOMMENDATION
    # -----------------------------
    elif choice == "3":
        movie = input("Enter the movie (e.g., leo, ayan): ")
        print(recommend_content_based(movie))

    # -----------------------------
    # EXIT
    # -----------------------------
    elif choice == "4":
        break