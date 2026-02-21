from sklearn.feature_extraction.text import TfidfVectorizer

def cleanData(df, columns_to_keep, *args):
  clean_books_df = df[columns_to_keep].copy(deep=True)
  clean_books_df['group_text'] = clean_books_df[list(args)].astype(str).agg(" ".join, axis=1)
  clean_books_df = clean_books_df[["book_id", "group_text"]]
  return clean_books_df

def build_vectors(clean_books_df):
  vectorizer = TfidfVectorizer()
  result = vectorizer.fit_transform(clean_books_df['group_text'].tolist())
