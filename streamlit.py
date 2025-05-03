import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title("Email Spam Classifier")

email = st.text_area("Enter the email", placeholder='Enter the email')

vectorizer = joblib.load("vectorizer.pkl")
model = joblib.load("nb_model.pkl")

def model_pred(email):
    X = vectorizer.transform([email])
    y_pred = model.predict(X)    
    return "Spam" if y_pred[0] == 1 else "Non-Spam"

if st.button("Classify"):
    st.write(f"The mail is {model_pred(email)}")
else:
    st.text("")

st.text("")
st.text("")
st.text("")


