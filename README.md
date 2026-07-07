🏠 House Price Prediction API

A Machine Learning powered REST API built using FastAPI that predicts house prices based on user-provided input features.

This project demonstrates the complete process of deploying a Machine Learning model as an API, from model loading to real-time prediction.

🚀 Features

- Real-time house price prediction
- FastAPI-based REST API
- Machine Learning model integration
- Interactive API documentation using Swagger UI
- Fast and lightweight backend service

🛠️ Tech Stack

- Python
- FastAPI
- Scikit-learn
- Pandas
- NumPy
- Uvicorn

⚙️ How It Works

1. User provides house details through API input.
2. FastAPI receives and validates the request.
3. The trained Machine Learning model processes the input.
4. The API returns the predicted house price.

📂 Project Structure

house-price-prediction-api/
│
├── main.py              # FastAPI application
├── model/               # Trained ML model files
├── dataset/             # Dataset files
├── requirements.txt     # Dependencies
└── README.md

▶️ Running the Project Locally

Clone the repository:

git clone https://github.com/deepakbpit2504/house-price-prediction-api.git

Install dependencies:

pip install -r requirements.txt

Start the FastAPI server:

uvicorn main:app --reload

Open the API:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs


🔮 Future Improvements

- Deploy API on cloud platforms
- Add frontend interface
- Improve model performance
- Add more real-world features

👨‍💻 Author

Deepak Dudeja