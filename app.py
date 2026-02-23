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

    books_df = pd.read_csv('./data/raw/books.csv')
  
    for i in top_indices:
        row = books_df[books_df['book_id'] == i+1]
        authors = row['authors'].values[0]
        average_rating = row['average_rating'].values[0]
        description = row['description'].values[0]
        genres = row['genres'].values[0]
        image_url = row['image_url'].values[0]
        isbn13 = row['isbn13'].values[0]
        pages = row['pages'].values[0]
        title = row['title'].values[0]

        recommended_books.append({
            "title": title,
            "book_id": book_id_list[i],
            "authors": authors,
            "average_rating": average_rating,
            "description": description,
            "genres": genres,
            "image_url": image_url,
            "isbn13": isbn13,
            "pages": pages
        })

    print(f"Recommended book IDs for book {liked_book_id}: {recommended_books}")
    return recommended_books

# recommended_books=bookRecommendation(68)

# print("Recommended id:")
# for book in recommended_books:
#     print("-", book["book_id"])

# print("Recommended titles:")
# for book in recommended_books:
#     print("-", book["title"])





liked_book_id = 68  # "Perks of Being a Wallflower"
# bookRecommendation(liked_book_id)
def getBookDetails(book_id):
    books_df = pd.read_csv('./data/raw/books.csv')

    row = books_df[books_df['book_id'] == book_id]
    authors = row['authors'].values[0]
    average_rating = row['average_rating'].values[0]
    description = row['description'].values[0]
    genres = row['genres'].values[0]
    image_url = row['image_url'].values[0]
    isbn13 = row['isbn13'].values[0]
    pages = row['pages'].values[0]
    title = row['title'].values[0]
    return title, authors, average_rating, description, genres, image_url, isbn13, pages


def createRecommendationGraph(liked_book_id, depth=3, top_k = 5, nodes=None, links=None, already_recommended=None):
    if nodes is None:
        nodes = []
    if links is None:
        links = []
    if already_recommended is None:
        already_recommended = set()

    if liked_book_id not in already_recommended:
        nodes.append({"id": 0, "book_id": liked_book_id, "label": getBookDetails(liked_book_id)[0], "authors": getBookDetails(liked_book_id)[1], "average_rating": getBookDetails(liked_book_id)[2], "description": getBookDetails(liked_book_id)[3], "genres": getBookDetails(liked_book_id)[4], "image_url": getBookDetails(liked_book_id)[5], "isbn13": getBookDetails(liked_book_id)[6], "pages": getBookDetails(liked_book_id)[7]})
        already_recommended.add(liked_book_id)

    recommended_books = bookRecommendation(liked_book_id, top_k)

    for i, book in enumerate(recommended_books):
        links.append({"source": liked_book_id, "target": book["book_id"]})

        if book["book_id"] not in already_recommended:
            nodes.append({"id": i+1, "book_id": book["book_id"], "label": book["title"], "authors": book["authors"], "average_rating": book["average_rating"], "description": book["description"], "genres": book["genres"], "image_url": book["image_url"], "isbn13": book["isbn13"], "pages": book["pages"]})

        if depth > 1 and book["book_id"] not in already_recommended:
            createRecommendationGraph(book["book_id"], depth - 1, top_k, nodes, links, already_recommended)
        already_recommended.add(book["book_id"])

    return nodes, links

        
nodes, links = createRecommendationGraph(68)
print("Nodes:", nodes)
print("Links:", links)

