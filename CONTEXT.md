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
- `app/auth.py`: Role-based authentication and session state management linking SME Borrower (`cfo@ecotex.it`) and Bank Credit Officer (`underwriter@intesabancapmi.it`) via shared Application ID (`ECOTEX-2026-IT`).
- `app/duckdb_engine.py`: In-process DuckDB OLAP engine (`data/duckdb/finsight.duckdb`) supporting statutory Italian Bilancio CEE format (Art. 2424-2425 c.c.), section-aware parsing, certified evidence extraction (`[FACT]`, `[CALCULATION]`), and real-time DSCR sensitivity curve computation.
- `app/pdf_generator.py`: Deterministic institutional vector PDF generator built with PyMuPDF (`fitz`), exporting EBA/GL/2020/06 and TUB Art. 128-sexies compliant Credit Memorandums with SHA-256 integrity seal.
- `app/api_client.py`: Dynamic client accepting loan amount, coupon spread, and tenor years, routing to live FastAPI or local DuckDB with zero downtime.
- `app/main.py`: World-class frontier enterprise Streamlit application:
  - Strict micro-typography with `tabular-nums` for instant vertical number scanning.
  - Interactive vector **Covenant Headroom Bar** showing shock absorption distance before EBA/bank covenant breaches.
  - **Glass Box Audit Inspector** exposing deterministic DuckDB SQL lineage vs RAG evidence provenance.
  - Role-specialized workflows: **Prescriptive Tenor Waterfall** for SME CFOs and **2D Downside Stress Heatmap** (EBITDA vs Rate hikes) for Bank Underwriters.
  - Sub-15ms reactivity via `@st.fragment` without full-page re-rendering.
- `data/sample_balance_sheet_cee_2024.csv`: True statutory Italian Bilancio CEE sample data with official line items across Attivo, Passivo, and Conto Economico.
- `data/sample_esg_audit_ecotex.pdf`: Audited sustainability report for 1-click unstructured ingestion demos.
- `scripts/deep_audit.py`: Automated 6-domain test suite validating companies, ratios, PDF generation, lakehouse tables, ingestion, stress scenarios, and security.
- `scripts/test_frontend_enhancements.py`: Automated 5-suite verification script validating all user-requested frontend fixes and calculations.
- `app/BACKEND_INTEGRATION_GUIDE.md`: Full specification for Teammate B.
- `presentation/FinSight_AI_Pitch_Deck.pptx` & `presentation/FinSight_AI_Pitch_Deck_Enterprise.pptx`: 6-slide executive deck following `five-minute-pitch-engine`.
- `presentation/PITCH_AND_DEMO_SCRIPT_IT.md`: Italian script (~650 words, timed at 04:30) with Big4/Tech Q&A defense and live DuckDB demo cues.
- `presentation/PITCH_AND_DEMO_SCRIPT.md`: English script (~660 words, timed at 04:30) with Big4/Tech Q&A defense and live DuckDB demo cues.
- `scripts/generate_pitch_deck.py`: Python script automating PPTX slide creation.
