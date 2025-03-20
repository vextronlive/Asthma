import streamlit as st
import os

st.title("📂 Debugging Model Load Issue")

# List all files in the Streamlit Cloud directory
files = os.listdir()

st.write("📝 Files in Current Directory:")
st.write(files)  # Display all files present

# Check if the model exists
if "asthma_model.pkl" in files:
    st.success("✅ Model file found!")
else:
    st.error("🚨 Model file is missing! Make sure it's uploaded to GitHub.")
