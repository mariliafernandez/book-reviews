import pandas as pd
import ast
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import unidecode
import re


def clean_author_name(name):
    if not isinstance(name, str):
        return ""
    name = unidecode.unidecode(name)
    name = re.sub(f"\.+", "", name)
    name = re.sub(f"\?+", "", name)
    name = re.sub(r"\s+", " ", name)  # Replace multiple spaces with a single space
    name = " ".join(name.split())
    return name.strip()


books_data = pd.read_csv("data/books_data.csv")

print("Preprocessing data...")
books_data["authors"] = books_data["authors"].fillna("[]")
books_data["authors"] = books_data["authors"].apply(ast.literal_eval)
books_data = books_data.explode(column="authors")
books_data.dropna(subset=["authors"], inplace=True)
books_data["authors"] = books_data["authors"].apply(clean_author_name)
books_data = books_data[books_data["authors"] != ""]

ratings = pd.read_csv("data/Books_rating.csv")

cols = ["authors", "summary", "score"]
merged = pd.merge(books_data, ratings, how="right", on="Title")
merged.dropna(subset=cols, inplace=True)

# Agrupa por autor e seleciona os top 20 mais frequentes
stats = (
    merged.groupby(by=["authors"])
    .score.agg(["count"])
    .sort_values(by="count", ascending=False)
    .head(20)
)

top_authors = stats.index
filtered = merged[merged["authors"].isin(top_authors)]

print("Sentiment analysis...")
sia = SentimentIntensityAnalyzer()
filtered["sentiment"] = filtered["summary"].apply(
    lambda x: sia.polarity_scores(x)["compound"]
)

filtered.to_csv("data/sentiment.csv", index=False)
