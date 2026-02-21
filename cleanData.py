import pandas as pd

ratings_df = pd.read_csv('./data/ratings.csv')
books_df = pd.read_csv('./data/books.csv')

# print(f"First 5 rows of ratings data:\n{ratings_df.head()}")
# print(f"First 5 rows of ratings data:\n{books_df.head()}")

user_ratings_count = ratings_df['user_id'].value_counts()
book_ratings_count = books_df['book_id'].value_counts()



def cleanData(df, *args):
  columns_to_keep = [*args]
  clean_books_df = df[columns_to_keep]
  return ratings_df.merge(clean_books_df, on='book_id')


cleanData(books_df, "book_id", "description", "genres", "authors").to_csv('./data/training_df.csv', index=False)

