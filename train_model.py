import os
import pandas as pd
import pickle
from sklearn.preprocessing import MinMaxScaler

# Define correct paths
dataset_file = os.path.join(os.path.dirname(__file__), "../dataset/deals.csv")
model_file = os.path.join(os.path.dirname(__file__), "../models/model.pkl")

def train_model():
    """Train a recommendation model based on price, rating, and calculate deal score."""
    
    # Load dataset
    if not os.path.exists(dataset_file):
        print("Dataset file not found! Run fetch_deals.py first.")
        return
    
    df = pd.read_csv(dataset_file)

    # Ensure required columns exist
    required_columns = {"product_name", "price", "rating", "image_url", "product_link"}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"Dataset must contain {required_columns} columns.")

    # Normalize price and rating (lower price, higher rating = better deal)
    scaler = MinMaxScaler()
    df["price_score"] = 1 - scaler.fit_transform(df[["price"]])  # Lower price = higher score
    df["rating_score"] = scaler.fit_transform(df[["rating"]])  # Higher rating = higher score

    # Compute final deal score
    df["deal_score"] = df["price_score"] * 0.7 + df["rating_score"] * 0.3  # Weighted formula

    # Sort deals by deal_score
    df = df.sort_values(by="deal_score", ascending=False)

    # Save dataset with deal_score
    df.to_csv(dataset_file, index=False)  # Overwriting deals.csv with deal_score

    # Save model (sorted deals)
    with open(model_file, "wb") as file:
        pickle.dump(df, file)

    print("Model trained and saved successfully!")

if __name__ == "__main__":
    train_model()
