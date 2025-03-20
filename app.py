import os
import streamlit as st

# Force install missing libraries
os.system("pip install joblib scikit-learn pandas numpy")

import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

st.title("🫁 Asthma Prediction App")

MODEL_PATH = "asthma_model.pkl"

# Check if model exists
if os.path.exists(MODEL_PATH):
    try:
        @st.cache_resource()
        def load_model():
            return joblib.load(MODEL_PATH)

        model = load_model()
        st.success("✅ Model loaded successfully!")

    except Exception as e:
        st.error(f"🚨 Error loading model: {e}")
else:
    st.error("🚨 Model file is missing! Make sure 'asthma_model.pkl' is uploaded.")
