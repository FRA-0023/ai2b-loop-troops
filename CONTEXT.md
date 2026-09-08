---
type: agent-context
status: initialized
---

# ?? Agent Operational Context (Fresh Context)

## ?? Primary Objective (Hackathon Phase 0)
- Maintain the boilerplate structure.
- Stand by until the event day (Sept 8, 2026). Once the random track and dataset are provided, update this objective to reflect the specific MVP to build.

## ?? Current State
- **Phase:** Pre-event setup (Boilerplate only).
- **Latest Action:** Repository initialized with Streamlit, .gitignore, and AI API wrappers.
- **Working Directory:** C:\Documenti\UNIMIB\AI2B - Loop Troops

## 🛠️ Tech Stack & Constraints (Agent Guidelines)
- **Strict UI Constraint:** Only use streamlit to build the frontend. Do NOT attempt to build a React/Next.js SPA.
- **AI Integration:** Use langchain with OpenAI/Anthropic in ai_core/llm_client.py.
- **Data Processing:** Use pandas for EDA and dataset ingestion.
- **Active Skills (Orchestrated):**
  - Coding / Architecture: `dev-backend`
  - Data Science / EDA / ML: `data-science`
  - Business / Copy / Pitch: `marketing-strategy`
  - Business & Strategy: `business-career`
  - Economics & Financial Markets: `economics-finance-and-markets`
- **Negative Constraints:** Do not commit datasets, .env files, or heavy models (enforced by .gitignore).

## ?? Active Blockers
- None. Waiting for the hackathon dataset and track announcement.

## ?? Next Steps (For the Agent on Event Day)
1. Parse the provided hackathon dataset (.csv / .json).
2. Update PROJECT.md with the specific architecture chosen for the random track.
3. Implement the real API calls in i_core/llm_client.py.
4. Build the data ingestion UI in pp/main.py.
