# Project Architecture: AI2B Loop Troops

This document tracks the high-level architecture of our Hackathon project.

## Tech Stack
* **Frontend/UI:** Streamlit (Python)
* **Data Manipulation:** Pandas / Numpy / Polars
* **AI Core:** OpenAI / Anthropic APIs (via custom wrappers or LangChain)
* **Notebooks:** Jupyter (strictly for fast EDA, not for production code)

## Architecture Diagram (Mental Model)
1. **User** uploads the provided dataset.csv via the Streamlit interface.
2. **Streamlit (app/main.py)** reads the file into a Pandas DataFrame.
3. **App logic** formats the user query and data context.
4. **AI Core (ai_core/llm_client.py)** sends the prompt to the LLM API.
5. **App** renders the LLM response and visualizes the dataset (Charts/Tables).
