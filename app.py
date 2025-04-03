import os
import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS  # Enable CORS

# Define paths
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATASET_FILE = os.path.join(BASE_DIR, "../dataset/deals.csv")

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow requests from frontend (fixes CORS issue)

# Load dataset
if os.path.exists(DATASET_FILE):
    df = pd.read_csv(DATASET_FILE)
else:
    print("⚠️ Warning: Dataset file not found! Make sure 'deals.csv' is available.")
    df = None  # Prevents breaking if dataset is missing

@app.route("/")
def home():
    return jsonify({"message": "Welcome to EcommerceDealsAI API! Use /recommend to get AI-powered deals."})

@app.route("/recommend", methods=["GET"])
def recommend_deals():
    """Returns top N recommended deals."""
    if df is None or df.empty:
        return jsonify({"error": "No deals available. Please upload the dataset."})

    # Get number of recommendations (default: 5)
    try:
        top_n = int(request.args.get("n", 5))
    except ValueError:
        return jsonify({"error": "Invalid number format. Please provide a valid integer."})

    # Sort by deal_score (highest first) and get top N deals
    top_deals = df.sort_values(by="deal_score", ascending=False).head(top_n)

    # Convert DataFrame to JSON format
    deals_json = top_deals.to_dict(orient="records")
    
    return jsonify({"recommendations": deals_json})

if __name__ == "__main__":
    app.run(debug=True)
