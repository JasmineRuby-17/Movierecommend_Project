
https://github.com/user-attachments/assets/47aea5f6-8df7-4435-9773-7d9ecfdcc5d6


TAMIL MOVIE RECOMMENDATION SYSTEM: 

A Python-based movie recommendation system built with collaborative filtering and content based filtering techniques, featuring a dataset of 67 Tamil/South Indian films.

PROJECT OVERVIEW: 

This project implements three recommendation strategies to suggest Tamil movies to users based on their preferences and viewing patterns:
Movie-Based Filtering — Recommends movies similar to a given movie using cosine similarity on the user-movie rating matrix.
User-Based Filtering — Finds users with similar taste and recommends movies they enjoyed that the target user hasn't seen.
Content-Based Filtering — Recommends movies in the same genre as the input movie.

📦 Installation: 

1. Clone the repository:
   
    git clone https://github.com/your-username/movie-recommendation-system.git

    cd movie-recommendation-system

2. Install dependencies:

    pip install pandas numpy scikit-learn

3. Generate the dataset (if CSV files are not present):

    python movie.py     # Creates movie.csv
   
    python rating.py    # Creates rating.csv
   
    python tag.py       # Creates tag.csv

    Update the file paths in movie.py , rating.py , tag.py , and recommender.py to match your local directory before running.

5. Run the application:

    python main.py
    
