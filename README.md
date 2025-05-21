# Movie-recommender-system
# 🎬 Movie Recommendation System

This is a **Content-Based Movie Recommendation System** built with Python. It recommends similar movies based on movie descriptions using **TF-IDF vectorization** and **cosine similarity**.

---

## 🚀 Features

- Content-based filtering using movie overviews
- TF-IDF text vectorization with scikit-learn
- Cosine similarity for recommendation ranking
- Simple command-line interface
- Easily extendable to genres, cast, or hybrid models

---

## 📁 Dataset

This project uses the **TMDB Movie Metadata** dataset from Kaggle:

🔗 [Download the dataset from Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

- File used: `tmdb_5000_movies.csv`
- Rename it to `movies.csv` and place it in the project folder

---

## 🛠️ Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender


2.Install dependencies:
pip install -r requirements.txt

3.How to Run:
python main.py

Example:
Enter a movie title: Avatar

Recommendations for 'Avatar':
1. John Carter
2. Guardians of the Galaxy
3. Star Trek
4. Pirates of the Caribbean: At World's End
5. The Hunger Games: Catching Fire
