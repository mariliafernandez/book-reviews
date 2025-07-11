import pandas as pd
import ast
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import numpy as np

books_data = pd.read_csv("data/books_data.csv")[["Title", "categories"]]
books_data.dropna(subset=["categories"], inplace=True)

ratings = pd.read_csv("data/Books_rating.csv")[["Title", "score", "summary", "text"]]

merged = pd.merge(books_data, ratings, how="right", on="Title")
merged.dropna(subset=["categories"], inplace=True)
merged["categories"] = merged["categories"].apply(ast.literal_eval)

df = merged.explode(column="categories")
df["categories"] = df["categories"].apply(lambda x: x.lower())

print("Embedding...")
model = SentenceTransformer("all-MiniLM-L6-v2")
categories = df.categories.unique()
embeddings = model.encode(categories)

print("Clustering...")
kmeans = KMeans(n_clusters=20, random_state=42)
labels = kmeans.fit_predict(embeddings)
centroids = kmeans.cluster_centers_
distances = np.linalg.norm(embeddings - centroids[kmeans.labels_], axis=1)

clustered = pd.DataFrame(
    {
        "categories": categories,
        "category_group": labels,
        "dist": distances
    }
)

df = df.merge(clustered, how="left", on="categories")

group_names = {}

print("Finding group names...")
for label in clustered["category_group"].unique():
    df_category = df[df["category_group"] == label]
    # Pega a categoria com a menor distância para o centróide
    idx = int(df_category["dist"].argmin())
    group_name = df_category.iloc[idx]["categories"]
    print(f"Group {label}: {group_name}")
    group_names[int(label)] = group_name


clustered["group_name"] = clustered.category_group.map(lambda x: group_names[x])
clustered.to_csv("data/clusters.csv", index=False)
