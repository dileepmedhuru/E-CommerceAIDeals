import os
import pandas as pd
import requests

# Ensure dataset directory exists
dataset_dir = os.path.join(os.path.dirname(__file__), "../dataset")
os.makedirs(dataset_dir, exist_ok=True)

def get_deals():
    url = "https://fakestoreapi.com/products"  # Example API
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to fetch deals.")
        return None
    
    deals = response.json()

    # Extract required fields
    extracted_data = []
    for product in deals:
        extracted_data.append({
            "id": product["id"],
            "product_name": product["title"],
            "price": product["price"],
            "category": product["category"],
            "rating": product["rating"]["rate"],  # Extracting only the rating value
            "image_url": product["image"],  # Product image URL
            "product_link": f"https://fakestoreapi.com/products/{product['id']}"  # Example product link
        })

    # Convert to DataFrame
    df = pd.DataFrame(extracted_data)

    # Save to CSV (overwrite existing file)
    csv_path = os.path.join(dataset_dir, "deals.csv")
    df.to_csv(csv_path, index=False)

    print(f"Dataset saved to {csv_path}")
    return df

# Run the function
if __name__ == "__main__":
    get_deals()
