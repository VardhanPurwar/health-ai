from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pickle

app = FastAPI()

# CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = pickle.load(open("model.pkl", "rb"))

class HealthData(BaseModel):
    data: list

@app.get("/")
def home():
    return {"message": "Health Prediction API running"}

@app.post("/predict")
def predict(input_data: HealthData):
    prediction = model.predict([input_data.data])
    return {"prediction": int(prediction[0])}