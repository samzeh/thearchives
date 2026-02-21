import pandas as pd
from preprocessing import cleanData

books_df = pd.read_csv('./data/books.csv')

cleanData(books_df, ["book_id", "description", "genres", "authors"], "description", "genres", "authors").to_csv('./data/clean_books_df.csv', index=False)

# clean_books_df = pd.read_csv('./data/clean_books_df.csv')a