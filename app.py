import streamlit as st
import joblib
import numpy as np

class PredictionPipeline:
    def __init__(self, model_path, encoder_card_path, encoder_country_path, scaler_path, expected_features):
        self.model = joblib.load(model_path)
        self.encoder_card = joblib.load(encoder_card_path)
        self.encoder_country = joblib.load(encoder_country_path)
        self.scaler = joblib.load(scaler_path)
        self.expected_features = joblib.load(expected_features)

    def safe_transform(self, encoder, values):
        known_classes = set(encoder.classes_)
        return np.array([encoder.transform([v])[0] if v in known_classes else -1 for v in values])

    def preprocess(self, df):
        if 'card' in df.columns:
            df['card'] = self.safe_transform(self.encoder_card, df['card'])
        if 'country' in df.columns:
            df['country'] = self.safe_transform(self.encoder_country, df['country'])

        for col in self.expected_features:
            if col not in df.columns:
                df[col] = 0

        df = df[self.expected_features]
        df_scaled = self.scaler.transform(df)
        return df_scaled

    def predict(self, df):
        processed_data = self.preprocess(df)
        return self.model.predict(processed_data)

# Snippet to load the model pipeline that has been trained
pipeline = PredictionPipeline(
    "best_model.pkl", 
    "label_encoder_card.pkl", 
    "label_encoder_country.pkl", 
    "scaler.pkl",
    "expected_features.pkl"
)

# Load the prediction pipeline and label encoder
psp_encoder = joblib.load("label_encoder_psp.pkl")  # Load PSP LabelEncoder

st.title("Credit Card Routing System")

# Setting and getting the user input fields
amount = st.number_input("Amount (Euros)", min_value=0.01, step=0.01)
country = st.selectbox("Country", ["Germany", "Switzerland", "Austria"])
card = st.selectbox("Provider of the Credit Card", ["Master", "Visa", "Diners"])
secured = st.radio("Transaction 3D Secured?", [1, 0])

# Defining the button-function that will make the prediction based on the user filled data
if st.button("Predict Best PSP"):
    import pandas as pd

    input_data = pd.DataFrame([{
        "amount": amount,
        "country": country,
        "card": card,
        "3D_secured": secured
    }])

    prediction = pipeline.predict(input_data)
    predicted_psp = psp_encoder.inverse_transform(prediction)
    psp = ["Moneycard", "Goldcard", "UK_Card", "Simplecard"]
    st.success(f"Best Recommended PSP: {psp[predicted_psp[0]]}")
