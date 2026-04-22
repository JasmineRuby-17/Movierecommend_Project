# 🎬 Tamil Movie Recommendation System

A Python-based movie recommendation system built with collaborative filtering and content-based filtering techniques, featuring a dataset of 67 Tamil/South Indian films.

---

## 📌 Project Overview

This project implements three recommendation strategies to suggest Tamil movies to users based on their preferences and viewing patterns:

- **Movie-Based Filtering** — Recommends movies similar to a given movie using cosine similarity on the user-movie rating matrix
- **User-Based Filtering** — Finds users with similar taste and recommends movies they enjoyed that the target user hasn't seen
- **Content-Based Filtering** — Recommends movies in the same genre as the input movie

---

## 🗂️ Project Structure

```
movie_recommendation_system/
│
├── data/
│   ├── movie.csv          # Movie dataset (67 Tamil/South Indian movies)
│   ├── rating.csv         # Synthetic genre-based user ratings (30 users)
│   └── tag.csv            # User-assigned tags per movie
│
├── main.py                # CLI interface — entry point
├── recommender.py         # Core recommendation logic
├── movie.py               # Script to generate movie.csv
├── rating.py              # Script to generate rating.csv
└── tag.py                 # Script to generate tag.csv
```

---

## 🎯 Features

| Feature | Description |
|---|---|
| 🎥 Movie-Based | Cosine similarity between movies based on user ratings |
| 👤 User-Based | K-nearest-neighbor style collaborative filtering |
| 🏷️ Content-Based | Genre matching for similar movie discovery |
| 🔍 Fuzzy Matching | Partial movie name search (e.g., type `singam` to find `Singam (2010)`) |
| ❌ Error Handling | Graceful responses for unknown movies/users |

---

## 🧰 Tech Stack

- **Python 3.x**
- **pandas** — Data manipulation
- **NumPy** — Numerical operations
- **scikit-learn** — Cosine similarity (`sklearn.metrics.pairwise`)

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. **Install dependencies**
   ```bash
   pip install pandas numpy scikit-learn
   ```

3. **Generate the dataset** (if CSV files are not present)
   ```bash
   python movie.py     # Creates movie.csv
   python rating.py    # Creates rating.csv
   python tag.py       # Creates tag.csv
   ```
   > ⚠️ Update the file paths in `movie.py`, `rating.py`, `tag.py`, and `recommender.py` to match your local directory before running.

4. **Run the application**
   ```bash
   python main.py
   ```

---

## 🖥️ Usage

Once you run `main.py`, you'll see an interactive menu:

```
🎬 MOVIE RECOMMENDER
1. Movie-Based
2. User-Based
3. Content-Based
4. Exit
Enter choice:
```

### Option 1 — Movie-Based Recommendation

```
Enter movie name (e.g., Master, Vikram, 96): Theri
→ ['Sivakasi (2005)', 'Master (2021)', 'Kaala (2018)', 'Thirupaachi (2005)', 'Sivaji (2007)']
```

### Option 2 — User-Based Recommendation

```
Enter user ID (e.g., 1–30): 17
→ ['Kaithi (2019)', 'Vikram (2022)', 'Thuppakki (2012)', 'Singam 2 (2013)', 'Mersal (2017)']
```

### Option 3 — Content-Based Recommendation

```
Enter the movie (e.g., leo, ayan): singam
→ ['Jailer (2023)', 'Singam 2 (2013)', 'Thuppakki (2012)', 'Asuran (2019)', 'Velayudham (2011)']
```

---

## 📊 Dataset Details

### movie.csv

| Column | Description |
|---|---|
| `movieId` | Unique movie ID (1–67) |
| `title` | Movie title with release year |
| `genres` | Genre(s) of the movie |

**Movies included (67 total):** Covers films from Vijay, Ajith, Rajinikanth, Kamal Haasan, Suriya, Dhanush, Vijay Sethupathi, Sivakarthikeyan, and major South Indian blockbusters.

### rating.csv

| Column | Description |
|---|---|
| `userId` | User ID (1–30) |
| `movieId` | Movie ID |
| `rating` | Rating (2.5–5.0, genre-preference based) |

Ratings are synthetically generated: each user has 2–3 preferred genres and gives higher ratings (4.0–5.0) to matching movies.

### tag.csv

| Column | Description |
|---|---|
| `userId` | User ID |
| `movieId` | Movie ID |
| `tag` | Keyword tag (e.g., `mass`, `emotional`, `thriller`) |

---

## ⚙️ How It Works

### Movie-Based Collaborative Filtering

```
User-Movie Matrix  →  Transpose  →  Cosine Similarity Matrix  →  Top N similar movies
```

Each movie is represented as a vector of user ratings. Cosine similarity between two movie vectors reveals how similarly users rated them.

### User-Based Collaborative Filtering

```
User-Movie Matrix  →  Cosine Similarity (users)  →  Find top 5 similar users
→  Collect their highly-rated movies  →  Remove movies the target user already rated
```

### Content-Based Filtering

```
Input Movie  →  Lookup Genre  →  Filter movies by matching genre  →  Return top N
```

---

## 📸 Screenshots

**System startup:**

> Data shape: (2010, 5) | Total Users: 30 | Total Movies: 67

**Movie-Based result for "Theri":**

> `['Sivakasi (2005)', 'Master (2021)', 'Kaala (2018)', 'Thirupaachi (2005)', 'Sivaji (2007)']`

**User-Based result for User 17:**

> `['Kaithi (2019)', 'Vikram (2022)', 'Thuppakki (2012)', 'Singam 2 (2013)', 'Mersal (2017)']`

**Content-Based result for "Singam":**

> `['Jailer (2023)', 'Singam 2 (2013)', 'Thuppakki (2012)', 'Asuran (2019)', 'Velayudham (2011)']`

---

## 🔧 Configuration

Before running, update the file paths in these scripts to match your system:

```python
# In recommender.py
movies  = pd.read_csv(r"YOUR_PATH/data/movie.csv")
ratings = pd.read_csv(r"YOUR_PATH/data/rating.csv")
tags    = pd.read_csv(r"YOUR_PATH/data/tag.csv")

# In movie.py / rating.py / tag.py
df.to_csv("YOUR_PATH/data/movie.csv", index=False)
```

---

## 🚀 Possible Enhancements

- Add a web UI using Flask or Streamlit
- Integrate real user ratings (e.g., from IMDb or Letterboxd)
- Add matrix factorization (SVD) for better collaborative filtering
- Expand dataset to include Malayalam, Telugu, and Hindi films
- Deploy as an API using FastAPI

---

## 👨‍💻 Author

Built as a learning project to explore recommender system concepts using a Tamil cinema dataset.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
