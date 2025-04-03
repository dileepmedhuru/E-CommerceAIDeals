import os
import pickle
import pandas as pd

# Define paths
base_dir = os.path.dirname(__file__)
dataset_path = os.path.join(base_dir, "../dataset/deals.csv")
model_path = os.path.join(base_dir, "../models/model.pkl")

# Load trained model
if os.path.exists(model_path):
    with open(model_path, "rb") as file:
        model = pickle.load(file)
else:
    print("Warning: Model file not found. Please train the model first!")
    model = None

# Load dataset for reference
if os.path.exists(dataset_path):
    df = pd.read_csv(dataset_path)
else:
    print("Warning: Dataset file not found!")
    df = None

def recommend_products(n=10):
    """Recommend the best deals using AI"""
    if df is None or model is None:
        return {"error": "Model or dataset not available. Please check file paths and train the model."}

    # Ensure the 'deal_score' column exists
    if "deal_score" not in df.columns:
        return {"error": "Missing 'deal_score' column. Re-train the model."}

    # Sort products based on AI-calculated deal score (higher = better deal)
    recommended = df.sort_values(by=["deal_score"], ascending=False).head(n)

    return recommended[["product_name", "price", "category", "rating", "deal_score"]].to_dict(orient="records")

# Run a test
if __name__ == "__main__":
    print(recommend_products())
