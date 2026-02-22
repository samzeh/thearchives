from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def cleanData(df, columns_to_keep, *args):
  clean_books_df = df[columns_to_keep].copy(deep=True)
  clean_books_df['group_text'] = clean_books_df[list(args)].astype(str).agg(" ".join, axis=1)
  clean_books_df = clean_books_df[["book_id", "group_text"]]
  return clean_books_df

def build_vectors(clean_books_df):
  vectorizer = TfidfVectorizer()
  result = vectorizer.fit_transform(clean_books_df['group_text'].tolist())

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
