from backend.fetch_deals import get_deals
from backend.database import save_deals

def update_deals():
    deals = get_deals()
    save_deals(deals)
    print("Updated deals in database")

if __name__ == "__main__":
    update_deals()
