# ⚡ AI2B Loop Troops: Rapid AI Prototyping Architecture for 8-Hour Sprints

[![Event](https://img.shields.io/badge/Event-AI2B%20Games%202026-blue)](#)
[![Frontend](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?logo=streamlit)](#)
[![Language](https://img.shields.io/badge/Language-Python%203.11+-3776AB?logo=python)](https://www.python.org/)
[![Architecture](https://img.shields.io/badge/Architecture-Decoupled%20Sprint%20Stack-green)](#)
[![Constraint](https://img.shields.io/badge/Time%20Limit-8%20Hours-red)](#)

> High-velocity deployment stack developed for competitive AI hackathons. Streamlit UI decoupled from a provider-agnostic LLM core under strict 8-hour sprint constraints.

---

## 📌 Executive Summary

Competitive AI hackathons fail when engineering teams spend crucial early hours debating UI libraries, rewiring API clients, or debugging monolithic scripts.

AI2B Loop Troops is an operational rapid-prototyping architecture built for the AI2B Games Milano Stage, engineered for execution under strict 8-hour time limits.

The stack establishes an immediate division of responsibilities: instant tabular ingestion in Streamlit, decoupled prompt engineering, and hot-swappable LLM clients.

---

## 🏛️ High-Velocity Sprint Architecture

```
                      AI2B LOOP TROOPS ARCHITECTURE
                                    │
                     User Data Upload (dataset.csv)
                                    │
                                    ▼
       ┌────────────────────────────────────────────────────────┐
       │             STREAMLIT INTERACTION LAYER                │
       │  Dynamic Data Ingestion & Visualization (app/main.py)  │
       └────────────────────────────┬───────────────────────────┘
                                    │
                                    ▼
       ┌────────────────────────────────────────────────────────┐
       │                 AI ORCHESTRATION CORE                  │
       │       Dynamic Prompt Engineering (ai_core/prompts.py)  │
       │       Provider-Agnostic Client (ai_core/llm_client.py) │
       └────────────────────────────┬───────────────────────────┘
                                    │
                                    ▼
       ┌────────────────────────────────────────────────────────┐
       │                   DECISION DELIVERABLE                 │
       │       Interactive Executive Dashboard & Live Insights  │
       └────────────────────────────────────────────────────────┘
```

The architecture strictly separates rapid exploratory data analysis from production app logic, keeping notebooks confined to experimentation.

---

## ⚙️ Core Architecture & Component Division

### Verified Component Structure
- **Interactive UI Cockpit ([`app/main.py`](app/main.py)):** Streamlit application managing user session state, CSV ingestion, data filtering, and real-time visualization.
- **AI Core Client ([`ai_core/llm_client.py`](ai_core/llm_client.py)):** Abstracted LLM communication layer supporting seamless switching between commercial APIs and local endpoints.
- **Prompt Engineering Layer ([`ai_core/prompts.py`](ai_core/prompts.py)):** Centralized prompt repository isolating system instructions and output contracts from UI code.
- **Architectural Specifications ([`PROJECT.md`](PROJECT.md) & [`CONTEXT.md`](CONTEXT.md)):** Formal tracking of sprint requirements, active team directives, and session continuity.

---

## 🛠️ Production Quickstart

### 1. Environment Setup
Create an isolated environment and install application dependencies:
```powershell
# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\activate

# Install requirements
pip install -r app/requirements.txt

# Configure environment variables
cp .env.example .env
```

### 2. Launch the Cockpit
Start the Streamlit dashboard in development mode:
```powershell
# Launch interactive application
streamlit run app/main.py
```

---

**Author:** Francesco Colombini  
[GitHub Profile](https://github.com/FRA-0023) · [LinkedIn](https://www.linkedin.com/in/francescocolombini/)