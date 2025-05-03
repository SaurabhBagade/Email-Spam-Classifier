import streamlit as st
import pandas as pd
import numpy as np


st.title("Email Spam Classifier")

email = st.text_area("Enter the email", placeholder='Enter the email')

st.button("Classify")
st.text("")
st.text("")
st.text("")

# df = pd.read_csv('combined_data.csv')

# freq = df["label"].value_counts()
# freq_df = freq.reset_index()
# freq_df.columns = ['label', 'count']
# freq_df = freq_df.set_index('label')

# st.write("### Email Type Count")
# st.bar_chart(freq_df)





