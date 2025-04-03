# EcommerceDealsAI  

EcommerceDealsAI is an AI-powered recommendation system that fetches the best e-commerce deals based on AI rankings. The system includes a backend API built with Flask and a frontend UI with HTML, CSS, and JavaScript.  

## Features  
✅ Fetches and ranks e-commerce deals using AI  
✅ Displays deals with images, prices, categories, and ratings  
✅ "Buy Now" button redirects users to product pages  
✅ Users can specify the number of deals to display  
✅ Confirmation message after clicking "Buy Now"  
✅ Home button redirects back to the main page  

---

## 📂 Project Structure  

```plaintext
EcommerceDealsAI/
│── backend/
│   ├── __pycache__/
│   ├── ai_recommendation.py
│   ├── app.py              # Flask API to serve recommended deals
│   ├── check.py
│   ├── database.py
│   ├── fetch_deals.py      # Fetches deals from various sources
│   ├── requirements.txt    # Dependencies
│
│── dataset/
│   ├── deals.csv           # Dataset containing product deals
│
│── frontend/
│   ├── index.html          # Main UI
│   ├── script.js
│   ├── style.css
│── models/
│   ├── model.pkl           # Trained AI model
│   ├── train_model.py      # Training script for AI ranking
│
│── scripts/
│   ├── cron_fetch.py       # Scheduled fetch script
│
│── venv/                   # Virtual environment
```

---

## 🚀 Setup Instructions  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/dileepmedhuru/EcommerceDealsAI.git
cd EcommerceDealsAI
```

### 2️⃣ Set Up Virtual Environment  
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies  
```bash
pip install -r backend/requirements.txt
```

### 4️⃣ Run the Backend Server  
```bash
cd backend
python app.py
```

### 5️⃣ Open Frontend  
Open `index.html` in a browser or use Live Server in VS Code.

---

## 🌟 API Endpoints  

| Endpoint        | Method | Description |
|----------------|--------|-------------|
| `/`            | GET    | API Home |
| `/recommend?n=<num>` | GET  | Get top `<num>` recommended deals |

---
