import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
movies = pd.read_csv("movies.csv")

# Fill missing values
movies['overview'] = movies['overview'].fillna('')

# Convert overview text to TF-IDF features
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['overview'])

# Compute cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Reset index for reverse mapping
movies = movies.reset_index()
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

# Recommendation function
def recommend(title, num_recommendations=5):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices]

# Test the recommender
if __name__ == "__main__":
    movie_name = input("Enter a movie title: ")
    if movie_name in indices:
        recommendations = recommend(movie_name)
        print(f"Recommendations for '{movie_name}':")
        for i, title in enumerate(recommendations, 1):
            print(f"{i}. {title}")
    else:
        print("Movie not found in the dataset.")
