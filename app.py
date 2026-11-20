import requests
import streamlit as st

st.title("🚕 TaxiFare predictor")

pickup_datetime = st.text_input("Pickup date & time", "2014-07-06 19:18:00")
pickup_longitude = st.number_input("Pickup longitude", value=-73.950655, format="%.6f")
pickup_latitude = st.number_input("Pickup latitude", value=40.783282, format="%.6f")
dropoff_longitude = st.number_input("Dropoff longitude", value=-73.984365, format="%.6f")
dropoff_latitude = st.number_input("Dropoff latitude", value=40.769802, format="%.6f")
passenger_count = st.number_input("Passengers", min_value=1, max_value=8, value=1, step=1)

API_URL = st.secrets["API_URL"]

if st.button("Predict fare"):
    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": int(passenger_count),
    }
    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        fare = response.json()["fare"]
        st.success(f"Estimated fare: ${fare:.2f}")
    except requests.exceptions.RequestException as e:
        st.error(f"API error: {e}")
