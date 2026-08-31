import streamlit as st
import pandas as pd
import os
import sys

# Add parent directory to path to import ai_core
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ai_core.llm_client import get_ai_response

# Basic Page Configuration
st.set_page_config(
    page_title="Loop Troops - AI2B",
    page_icon="??",
    layout="wide"
)

st.title("?? AI2B Hackathon - Loop Troops")
st.markdown("Boilerplate initialized and ready. **Upload the event dataset below.**")

# 1. Dataset Ingestion (EDA / Integrator role)
st.sidebar.header("Data Configuration")
uploaded_file = st.sidebar.file_uploader("Upload Dataset", type=["csv", "json"])

if uploaded_file is not None:
    try:
        # Assuming CSV for the boilerplate, easy to adapt to JSON/Excel
        df = pd.read_csv(uploaded_file)
        st.subheader("Data Preview")
        st.dataframe(df.head())
        
        # 2. AI Interaction (AI Engine role)
        st.divider()
        st.subheader("AI Analysis")
        user_query = st.text_input("Ask something about this dataset or run an operation:")
        
        if st.button("Generate Insight"):
            if user_query:
                with st.spinner("AI is analyzing..."):
                    data_summary = f"Columns: {list(df.columns)}, Shape: {df.shape}"
                    full_prompt = f"Data Summary: {data_summary}\nUser Query: {user_query}"
                    
                    response = get_ai_response(full_prompt)
                    st.success("Analysis Complete")
                    st.write(response)
            else:
                st.warning("Please enter a query.")
                
    except Exception as e:
        st.error(f"Error loading file: {e}")
else:
    st.info("Awaiting dataset upload...")
