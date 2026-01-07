import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Feature Distribution", layout="wide")

st.title("📊 Feature Distribution Using Histograms")

# Upload dataset
uploaded_file = st.file_uploader("Upload Wine Dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head())

    st.subheader("📈 Feature Distributions")

    # Plot histograms
    fig, ax = plt.subplots(figsize=(15, 10))
    df.hist(bins=20, edgecolor="black", ax=ax)
    plt.suptitle("Feature Distribution of Wine Dataset", fontsize=16)

    st.pyplot(fig)

    st.markdown("""
    ### 📝 Observation
    - Features have different ranges and distributions  
    - Some features show skewness  
    - Feature scaling is required before clustering
    """)
else:
    st.info("⬆️ Please upload a CSV file to view histograms.")
