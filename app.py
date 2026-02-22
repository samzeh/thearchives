import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

with open('./data/processed/artifacts.pkl', 'rb') as f:
    artifacts = pickle.load(f)

group_text_result = artifacts['group_text_result']
genre_result = artifacts['genre_result']
user_rating_similarities = artifacts['user_rating_similarities']
book_id_list = artifacts['book_id_list']

def bookRecommendation(liked_book_id, top_k=5):
    liked_index = book_id_list.index(liked_book_id)  

    ratings_similarities = user_rating_similarities[liked_index]
    text_similarities = cosine_similarity(group_text_result[liked_index], group_text_result).flatten()
    genre_similarities = cosine_similarity(genre_result[liked_index], genre_result).flatten()

    similarities = 0.5 * ratings_similarities + 0.3 * text_similarities + 0.2 * genre_similarities
    similarities[liked_index] = -1  

    top_indices = similarities.argsort()[-top_k:][::-1]
    recommended_books = []
  
    for i in top_indices:
        recommended_books.append(book_id_list[i])

    print(f"Recommended book IDs for book {liked_book_id}: {recommended_books}")
    return recommended_books


liked_book_id = 68  # "Perks of Being a Wallflower"
bookRecommendation(liked_book_id)


def getBookDetails(book_id):
    books_df = pd.read_csv('./data/books.csv')

    row = books_df[books_df['book_id'] == book_id]
    authors = row['authors'].values[0]
    average_rating = row['average_rating'].values[0]
    description = row['description'].values[0]
    genres = row['genres'].values[0]
    image_url = row['image_url'].values[0]
    isbn13 = row['isbn13'].values[0]
    pages = row['pages'].values[0]
    
    return authors, average_rating, description, genres, image_url, isbn13, pages
