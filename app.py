import streamlit as st
import pandas as pd
import numpy as np
import joblib
import openpyxl


st.title("Email Spam Classifier")

email = st.text_area("Enter the email", placeholder='Enter the email')

vectorizer = joblib.load("vectorizer.pkl")
model = joblib.load("nb_model.pkl")

def predict_emails(df, email_column):
    X = vectorizer.transform(df[email_column])    
    df["Prediction"] = model.predict(X)
    return df

uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)
        st.write("Preview of uploaded data:", df.head())

        email_column = st.selectbox("Select column with email text", df.columns)

        if st.button("Predict Spam"):
            result_df = predict_emails(df, email_column)

            # Show preview of result
            st.write("Prediction Results:", result_df.head())

            # Download button
            output_file = "predicted_emails.xlsx"
            result_df.to_excel(output_file, index=False)

            with open(output_file, "rb") as f:
                st.download_button("Download Results", f, file_name=output_file)
    except Exception as e:
        st.error(f"Error: {e}")

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


