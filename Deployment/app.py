import streamlit as st
import pandas as pd
import joblib

# Load trained model
from pathlib import Path
model = joblib.load(Path(__file__).parent / "best_crop_prediction_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Crop Recommendation AI",
    page_icon="🌱"
)

st.title("🌱 Crop Recommendation AI")
st.write("Enter the soil and environmental conditions to get a crop recommendation.")

# Input fields
N = st.number_input("Nitrogen (N)", min_value=0.0)
P = st.number_input("Phosphorus (P)", min_value=0.0)
K = st.number_input("Potassium (K)", min_value=0.0)
temperature = st.number_input("Temperature (°C)", min_value=0.0)
humidity = st.number_input("Humidity (%)", min_value=0.0)
ph = st.number_input("pH", min_value=0.0)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0)

# Prediction button
if st.button("Recommend Crop"):

    input_data = pd.DataFrame([[
        N, P, K, temperature, humidity, ph, rainfall
    ]], columns=[
        "N", "P", "K", "temperature", "humidity", "ph", "rainfall"
    ])

    prediction = model.predict(input_data)
    
    st.success(f"Recommended Crop: {prediction[0]}")
    
    probabilities = model.predict_proba(input_data)[0]
    
    probability_data = pd.DataFrame({
        "Crop": model.classes_,
        "Probability": probabilities
    })
    
    confidence = probabilities.max() * 100
    
    st.metric("Confidence", f"{confidence:.2f}%")
    
    st.bar_chart(
        probability_data.set_index("Crop")
    )