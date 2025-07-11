# 🎬 Movie Recommender System

A simple and efficient movie recommender system that suggests similar movies based on genre using content-based filtering. Built with **pandas**, **scikit-learn**, and **Streamlit**.

---

## 📌 Features

- 🔍 Fuzzy movie title search (partial input supported)
- 🧠 Content-based recommendations using genre vectors
- ⭐ Displays average user ratings from MovieLens data
- 🎯 Adjustable number of recommendations
- 🎨 Clean and responsive Streamlit UI

---

## 📁 Dataset

Uses the [MovieLens 32M dataset](https://grouplens.org/datasets/movielens/32m/), specifically:
- `movies.csv`: Contains movieId, title, genres
- `ratings.csv`: Contains movieId, userId, rating

Only a sample (e.g., 10K movies) may be used for performance.

---

## 🧠 How It Works

1. Genres are one-hot encoded for each movie
2. Cosine similarity is computed between movies
3. When a user selects a movie:
   - Similar movies are retrieved based on genre similarity
   - Displayed with genre and average rating

---

## 🚀 Run the App Locally

### 1. Clone the repo:
```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 📦 Project Structure

```
movie-recommender/
├── app.py                   # Streamlit UI
├── recommender.py           # Logic and model functions
├── movies.csv               # Movie metadata
├── ratings.csv              # User ratings
├── movie_genre_features.pkl # Preprocessed genre features
├── requirements.txt         # Required packages
└── README.md                # This file
```

## 🔧 Future Improvements

* Add tag-based similarity using `genome-tags.csv`
* Filter by number of ratings (popularity threshold)
* Add IMDb or YouTube links for movies
* Deploy to Streamlit Cloud for public access

---

## 👨‍💻 Author

**Lakshay Jain**
*Machine Learning & Data Scientist*
[LinkedIn](https://www.linkedin.com/in/lakshay-jain-a48979289/) • [GitHub](https://github.com/frogface539)

---

```
