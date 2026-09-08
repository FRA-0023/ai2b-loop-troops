---
type: agent-context
status: handoff-ready
---

# 🧭 Agent Operational Context (FinSight AI)

## 🎯 Strategic Positioning & Value Proposition
- **Product:** FinSight AI — Autonomous SME Credit Readiness & Capital Sizing Copilot.
- **Target Customer:** SME CFOs, Business Owners, and Corporate Accounting Advisory Firms (B2B2C distribution).
- **Core Value:** Eliminates the 3-week borrowing black box. Pre-evaluates bankability in 14 seconds using in-memory DuckDB balance sheet parsing, Banca d'Italia provincial credit default benchmarks, Open Data Lombardia sector indicators, and FastEmbed ESG disclosures.
- **Business Model:** Freemium bankability diagnostic + 0.5%-1.0% success/dossier certification fee upon loan drawdown. Zero direct CAC via 120,000 corporate accounting firms in Italy.

## 🛠️ Architecture & Settled Principles
- **Golden Architectural Rule:** The LLM is NEVER the financial calculator. All scoring, DSCR, leverage, and liquidity calculations are 100% deterministic (DuckDB / Python). The LLM is strictly an orchestrator, semantic extractor (RAG), and evidence synthesizer.
- **Data Sovereignty:** DuckDB runs as an in-process local OLAP engine. Sensitive accounting data is parsed in RAM without external cloud leaks.
- **Evidence Taxonomy:** Section 26 compliance with strict labeling: `[FACT]` (audited/central bank data), `[CALCULATION]` (deterministic math formulas), and `[REASONING]` (semantic synthesis).

## 📍 Current Workspace State
- `app/main.py`: Streamlit vertical slice with institutional dark theme, 7-step decision trace, Plotly gauges, What-If loan sizing slider, and certified dossier export.
- `app/api_client.py`: Antifragile dual-mode client (FastAPI `POST /evaluate` with 4.0s timeout and auto-failover to local deterministic payload).
- `app/mock_data.py`: Single source of truth for fallback and scenario formulas.
- `app/BACKEND_INTEGRATION_GUIDE.md`: Full specification for Teammate B.
- `presentation/FinSight_AI_Pitch_Deck.pptx`: 6-slide executive deck following `five-minute-pitch-engine`.
- `presentation/PITCH_AND_DEMO_SCRIPT_IT.md`: Italian script (~650 words, timed at 04:30) with Big4/Tech Q&A defense.
- `presentation/PITCH_AND_DEMO_SCRIPT.md`: English script (~660 words, timed at 04:30) with Big4/Tech Q&A defense.
