import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

model = joblib.load("house_model.joblib")
features = joblib.load("house_features.joblib")

#input schema
class HouseFeatures(BaseModel):
    MedInc: float = Field(gt=0, description="Median income of Neighbourhood")
    HouseAge: float = Field(gt=0, description="Median house age in block group")
    AveRooms: float = Field(gt=0, description="Average number of rooms per household")
    AveBedrms: float = Field(gt=0, description="Average number of bedrooms per household")
    Population: float = Field(gt=0, description="Block group population")
    AveOccup: float = Field(gt=0, description="Average number of household members")
    Latitude: float = Field(ge=32, le=42, description="Block group latitude")
    Longitude: float = Field(ge=-125, le=-114, description="Block group longitude")

    #home
    @app.get("/")
    def home():
        return {"message": "Welcome to the California Housing Price Prediction API!",
                "status": "API is running successfully.",
                "endpoint":"send a POST request to /predict with the required features to get the predicted house price."
                }
    
    @app.get("/health")
    def health():
        return {"status": "API is healthy and running.",
                "model": "Random Forest Regressor",
                "features": features,
                "avgerage error": "The model has an average error of approximately $39,000 in predicting house prices."
                }
    
#prediction
@app.post("/predict")
def predict_price(house: HouseFeatures):
    try:
        input_data = pd.DataFrame([{
            "MedInc": house.MedInc,
            "HouseAge": house.HouseAge,
            "AveRooms": house.AveRooms,
            "AveBedrms": house.AveBedrms,
            "Population": house.Population,
            "AveOccup": house.AveOccup,
            "Latitude": house.Latitude,
            "Longitude": house.Longitude
        }])

        predicted = model.predict(input_data)[0]
        price_usd = predicted * 100000  # Convert to USD
        return {"predicted_price": f"${price_usd:,.0f}", 
                "prerdicted_price_short": f"${predicted:,.2f} hundred thousands",
                "confidence_range": f"${price_usd - 39000:,.0f} to ${price_usd + 39000:,.0f}"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"prediction failed: {str(e)}")
    
