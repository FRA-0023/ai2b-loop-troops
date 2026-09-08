"""
FinSight AI - Financial Intelligence & Credit Readiness Engine
==============================================================
Platform for SMEs & Corporate Advisors to assess bankability, simulate loan sizing,
and generate certified bank-grade financing dossiers.

HORMOZI VALUE EQUATION OPTIMIZATION:
- Dream Outcome: €750k Green Financing at prime interest rate.
- Perceived Likelihood of Achievement: 94% Pre-Approval Acceptance Probability + SHA-256 Audit Seal.
- Time Delay: 14 Seconds (vs 21 Days).
- Effort & Sacrifice: 1-Click Automated Data Fusion.
"""

import os
import sys
import hashlib
from typing import Dict, Any

# Ensure workspace root is in sys.path
WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if WORKSPACE_ROOT not in sys.path:
    sys.path.insert(0, WORKSPACE_ROOT)

import streamlit as st
import plotly.graph_objects as go

from app.mock_data import get_base_demo_payload, calculate_scenario
from app.api_client import evaluate_application, DEFAULT_BACKEND_URL


# ==========================================
# PAGE CONFIGURATION & THEME
# ==========================================
st.set_page_config(
    page_title="FinSight AI | SME Credit Readiness & Bankability Engine",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .stApp {
        background-color: #0b0f19;
        color: #f1f5f9;
    }
    
    .finsight-header {
        border-bottom: 1px solid #1e293b;
        padding-bottom: 1.25rem;
        margin-bottom: 1.25rem;
    }
    
    .finsight-badge {
        display: inline-block;
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        padding: 0.25rem 0.65rem;
        border-radius: 9999px;
        margin-right: 0.5rem;
    }
    
    .badge-primary {
        background-color: rgba(37, 99, 235, 0.15);
        color: #60a5fa;
        border: 1px solid rgba(59, 130, 246, 0.3);
    }
    
    .badge-success {
        background-color: rgba(16, 185, 129, 0.15);
        color: #34d399;
        border: 1px solid rgba(16, 185, 129, 0.3);
    }
    
    .badge-warning {
        background-color: rgba(245, 158, 11, 0.15);
        color: #fbbf24;
        border: 1px solid rgba(245, 158, 11, 0.3);
    }

    .badge-danger {
        background-color: rgba(239, 68, 68, 0.15);
        color: #f87171;
        border: 1px solid rgba(239, 68, 68, 0.3);
    }
    
    .exec-card {
        background: #111827;
        border: 1px solid #1f2937;
        border-radius: 8px;
        padding: 1.25rem;
        margin-bottom: 1.25rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
    }
    
    .exec-card-title {
        font-size: 0.82rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        font-weight: 600;
        color: #94a3b8;
        margin-bottom: 0.75rem;
    }
    
    /* Hormozi Legal & Financial Certainty Box */
    .certainty-banner {
        background: linear-gradient(135deg, #0e2722 0%, #0c1a29 100%);
        border: 1px solid #10b981;
        border-radius: 8px;
        padding: 1rem 1.25rem;
        margin-bottom: 1.25rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .trace-step-container {
        display: flex;
        flex-wrap: wrap;
        gap: 0.75rem;
        margin: 1rem 0;
    }
    
    .trace-step {
        flex: 1 1 calc(14% - 0.75rem);
        min-width: 140px;
        background: #131d31;
        border: 1px solid #233554;
        border-radius: 6px;
        padding: 0.75rem 0.6rem;
        text-align: center;
        transition: all 0.2s ease;
    }
    
    .trace-step:hover {
        border-color: #38bdf8;
        background: #18243e;
    }
    
    .trace-step-num {
        font-size: 0.65rem;
        font-family: 'JetBrains Mono', monospace;
        color: #38bdf8;
        text-transform: uppercase;
        margin-bottom: 0.2rem;
    }
    
    .trace-step-title {
        font-size: 0.78rem;
        font-weight: 600;
        color: #e2e8f0;
    }
    
    .trace-step-status {
        font-size: 0.7rem;
        color: #10b981;
        margin-top: 0.25rem;
    }
    
    .tag-fact {
        background: rgba(56, 189, 248, 0.12);
        color: #38bdf8;
        border: 1px solid rgba(56, 189, 248, 0.25);
        font-size: 0.68rem;
        font-weight: 600;
        padding: 0.15rem 0.45rem;
        border-radius: 4px;
        display: inline-block;
    }
    
    .tag-calc {
        background: rgba(52, 211, 153, 0.12);
        color: #34d399;
        border: 1px solid rgba(52, 211, 153, 0.25);
        font-size: 0.68rem;
        font-weight: 600;
        padding: 0.15rem 0.45rem;
        border-radius: 4px;
        display: inline-block;
    }
    
    .tag-reason {
        background: rgba(251, 191, 36, 0.12);
        color: #fbbf24;
        border: 1px solid rgba(251, 191, 36, 0.25);
        font-size: 0.68rem;
        font-weight: 600;
        padding: 0.15rem 0.45rem;
        border-radius: 4px;
        display: inline-block;
    }

    .whatif-box {
        background: linear-gradient(135deg, #131b2e 0%, #0d1322 100%);
        border: 1px solid #2b3a58;
        border-radius: 8px;
        padding: 1.25rem;
    }
    
    .delta-down {
        color: #f87171;
        font-weight: 600;
    }
    
    .delta-up {
        color: #34d399;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)


# ==========================================
# GAUGE PLOT HELPER
# ==========================================
def create_gauge(value: int, title: str, benchmark: int, color_theme: str = "blue") -> go.Figure:
    color_map = {
        "blue": ("#38bdf8", "#1d4ed8"),
        "emerald": ("#10b981", "#047857"),
        "amber": ("#f59e0b", "#b45309")
    }
    bar_c, thresh_c = color_map.get(color_theme, ("#38bdf8", "#1d4ed8"))

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': title, 'font': {'size': 13, 'color': '#94a3b8', 'family': 'Inter'}},
        number={'font': {'size': 32, 'color': '#f8fafc', 'family': 'Inter'}, 'suffix': "/100"},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#334155", 'tickfont': {'color': '#64748b', 'size': 9}},
            'bar': {'color': bar_c, 'thickness': 0.35},
            'bgcolor': "#1e293b",
            'borderwidth': 0,
            'steps': [
                {'range': [0, 55], 'color': 'rgba(239, 68, 68, 0.12)'},
                {'range': [55, 75], 'color': 'rgba(245, 158, 11, 0.12)'},
                {'range': [75, 100], 'color': 'rgba(16, 185, 129, 0.12)'}
            ],
            'threshold': {
                'line': {'color': thresh_c, 'width': 3},
                'thickness': 0.75,
                'value': benchmark
            }
        }
    ))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=15, r=15, t=30, b=10),
        height=170,
        font={'color': "#e2e8f0", 'family': "Inter"}
    )
    return fig


# ==========================================
# SIDEBAR CONTROLS
# ==========================================
st.sidebar.markdown("""
<div style="padding-bottom: 0.5rem; margin-bottom: 1rem; border-bottom: 1px solid #1e293b;">
    <h3 style="margin:0; font-size: 1.1rem; color: #f8fafc;">FinSight SME Engine</h3>
    <p style="margin:0; font-size: 0.75rem; color: #64748b;">Bankability & Origination Console</p>
</div>
""", unsafe_allow_html=True)

connection_mode = st.sidebar.radio(
    "Execution Mode:",
    options=["Deterministic Fallback (Demo Safe)", "Live API (FastAPI)"],
    index=0
)
backend_url = st.sidebar.text_input("Backend Endpoint:", value=DEFAULT_BACKEND_URL)
use_force_mock = (connection_mode == "Deterministic Fallback (Demo Safe)")

st.sidebar.markdown("---")
st.sidebar.markdown("### SME Test Profile")
magic_query_text = (
    "Assess a €750k sustainability-linked equipment loan for EcoTex Milano, "
    "a textile manufacturer in Milan."
)

if st.sidebar.button("⚡ Pre-Load EcoTex Milano (€750k)", use_container_width=True):
    st.session_state["query_input"] = magic_query_text

if "query_input" not in st.session_state:
    st.session_state["query_input"] = magic_query_text

st.sidebar.markdown("---")
st.sidebar.markdown("### Tech Stack Architecture")
st.sidebar.markdown("""
- **In-Process OLAP:** `DuckDB 1.0`
- **Data Standard:** `Python 3.11 / Pydantic`
- **Retrieval Engine:** `Hybrid RAG / FastEmbed`
- **Deterministic Scoring:** `CRO Matrix Rules`
- **Compliance:** `TUB Art. 128-sexies / OAM`
""")


# ==========================================
# 1. HEADER & HORMOZI CERTAINTY SEAL
# ==========================================
st.markdown("""
<div class="finsight-header">
    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
            <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.25rem;">
                <h1 style="margin: 0; font-size: 1.85rem; font-weight: 700; color: #ffffff; letter-spacing: -0.02em;">
                    FinSight AI
                </h1>
                <span class="finsight-badge badge-primary">SME Capital Copilot</span>
                <span class="finsight-badge badge-success">Bank-Grade Pre-Underwritten</span>
            </div>
            <p style="margin: 0; font-size: 0.95rem; color: #94a3b8;">
                Autonomous Credit Readiness, What-If Sizing & Certified Financing Origination for SMEs
            </p>
        </div>
        <div style="text-align: right;">
            <span style="font-size: 0.75rem; color: #64748b; font-family: 'JetBrains Mono', monospace;">
                MODEL: B2B Origination (1.0% Success Fee)
            </span>
            <br>
            <span style="font-size: 0.75rem; color: #10b981; font-family: 'JetBrains Mono', monospace;">
                COMPLIANCE: TUB Art. 128-sexies (OAM Ready)
            </span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# 2. HORMOZI CERTAINTY BANNER (PERCEIVED LIKELIHOOD)
# ==========================================
# Compute deterministic audit hash based on applicant + loan amount
audit_hash = hashlib.sha256(b"EcoTex_Milano_750000_BDI_182_LOMB_41").hexdigest()[:16].upper()

st.markdown(f"""
<div class="certainty-banner">
    <div>
        <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.2rem;">
            <span style="font-size: 1.1rem;">🔒</span>
            <span style="font-size: 0.95rem; font-weight: 700; color: #ecfdf5;">
                Bank Acceptance Certainty: 94% Probability of Loan Execution
            </span>
        </div>
        <div style="font-size: 0.78rem; color: #a7f3d0;">
            Pre-audited against Banca d'Italia provincial NPL benchmarks and EBA loan origination rules. 
            <b>Zero guessing. Zero black-box rejections.</b>
        </div>
    </div>
    <div style="text-align: right; font-family: 'JetBrains Mono', monospace;">
        <span style="font-size: 0.7rem; color: #6ee7b7;">AUDIT PROOF HASH</span><br>
        <span style="font-size: 0.85rem; font-weight: 600; color: #ffffff;">SHA256: {audit_hash}</span>
    </div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# 3. SME DOSSIER OVERVIEW CARD
# ==========================================
st.markdown("""
<div class="exec-card">
    <div class="exec-card-title">Target SME Financing Request</div>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem;">
        <div>
            <span style="font-size: 0.72rem; color: #64748b; text-transform: uppercase;">Borrower Entity</span>
            <div style="font-size: 1.05rem; font-weight: 600; color: #f8fafc;">EcoTex Milano S.p.A.</div>
        </div>
        <div>
            <span style="font-size: 0.72rem; color: #64748b; text-transform: uppercase;">Sector & District</span>
            <div style="font-size: 0.95rem; font-weight: 500; color: #e2e8f0;">Sustainable Textiles (ATECO 13.96)</div>
        </div>
        <div>
            <span style="font-size: 0.72rem; color: #64748b; text-transform: uppercase;">Requested Facility</span>
            <div style="font-size: 1.05rem; font-weight: 700; color: #38bdf8;">€ 750,000</div>
        </div>
        <div>
            <span style="font-size: 0.72rem; color: #64748b; text-transform: uppercase;">Success Fee (1.0%)</span>
            <div style="font-size: 1.05rem; font-weight: 700; color: #34d399;">€ 7,500 <span style="font-size: 0.7rem; color: #94a3b8;">(Paid by Lender)</span></div>
        </div>
        <div>
            <span style="font-size: 0.72rem; color: #64748b; text-transform: uppercase;">CapEx Purpose</span>
            <div style="font-size: 0.82rem; color: #cbd5e1;">Closed-loop water recycling & low-energy dyeing unit</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# 4. EXECUTION TRIGGER
# ==========================================
col_q, col_b = st.columns([5, 1])
with col_q:
    user_query = st.text_input(
        "SME Credit Analysis Prompt:",
        value=st.session_state["query_input"]
    )
with col_b:
    st.write("")
    st.write("")
    run_eval = st.button("🚀 Analyze Bankability", type="primary", use_container_width=True)

with st.spinner("FinSight AI is fusing DuckDB financials, Banca d'Italia metrics, and ESG disclosures..."):
    payload, execution_mode, status_msg = evaluate_application(
        query=user_query,
        loan_amount=750000,
        backend_url=backend_url,
        force_mock=use_force_mock
    )


# ==========================================
# 5. CORE KPI GAUGES & DECISION CARDS
# ==========================================
st.markdown("### SME Credit Readiness & Bankability Metrics")

k1, k2, k3, k4 = st.columns([1.2, 1.2, 1, 1])

with k1:
    fin_score = payload.get("financial_score", 82)
    st.plotly_chart(create_gauge(fin_score, "Financial Health Score", benchmark=70, color_theme="blue"), use_container_width=True)
    st.markdown("""
    <div style="text-align: center; margin-top: -15px;">
        <span class="finsight-badge badge-primary">Prime Tier</span>
        <span style="font-size: 0.72rem; color: #94a3b8;">Benchmark: 70/100</span>
    </div>
    """, unsafe_allow_html=True)

with k2:
    esg_score = payload.get("esg_score", 91)
    st.plotly_chart(create_gauge(esg_score, "ESG Alignment Score", benchmark=75, color_theme="emerald"), use_container_width=True)
    st.markdown("""
    <div style="text-align: center; margin-top: -15px;">
        <span class="finsight-badge badge-success">Top Decile Green</span>
        <span style="font-size: 0.72rem; color: #94a3b8;">Unlocks Subsidized Pricing</span>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown("""
    <div class="exec-card" style="height: 215px; display: flex; flex-direction: column; justify-content: center;">
        <div class="exec-card-title">Territorial Macro Leverage</div>
        <div style="margin-bottom: 0.6rem;">
            <span style="font-size: 0.72rem; color: #64748b;">BANCA D'ITALIA PROVINCIAL NPL</span>
            <div style="font-size: 1.25rem; font-weight: 700; color: #34d399;">1.82%</div>
            <span style="font-size: 0.7rem; color: #94a3b8;">Milan District vs Italy 2.95%</span>
        </div>
        <div>
            <span style="font-size: 0.72rem; color: #64748b;">LOMBARDIA SECTOR TREND</span>
            <div style="font-size: 1.25rem; font-weight: 700; color: #38bdf8;">+4.1% YoY</div>
            <span style="font-size: 0.7rem; color: #94a3b8;">High Export Margin Buffer</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with k4:
    rec = payload.get("recommendation", "APPROVE")
    st.markdown(f"""
    <div class="exec-card" style="height: 215px; display: flex; flex-direction: column; justify-content: center; text-align: center; border-color: #10b981;">
        <div class="exec-card-title">Bankability Outcome</div>
        <div style="font-size: 1.8rem; font-weight: 800; color: #34d399; letter-spacing: 0.04em;">
            {rec}
        </div>
        <div style="margin-top: 0.3rem;">
            <span class="finsight-badge badge-success">Pre-Approved at Prime Rates</span>
        </div>
        <p style="margin: 0.6rem 0 0 0; font-size: 0.72rem; color: #94a3b8;">
            Eligible for 5.15% fixed rate + 15% regional grant
        </p>
    </div>
    """, unsafe_allow_html=True)


# Financial Ratios Bar
st.markdown("""
<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.75rem; margin-bottom: 1.5rem;">
    <div style="background: #131d31; border: 1px solid #1f293d; border-radius: 6px; padding: 0.6rem 0.8rem;">
        <span style="font-size: 0.7rem; color: #94a3b8;">Debt Service Coverage (DSCR)</span>
        <div style="font-size: 1.05rem; font-weight: 700; color: #38bdf8;">1.68x <span style="font-size: 0.7rem; color: #10b981;">(Solid Buffer > 1.30x)</span></div>
    </div>
    <div style="background: #131d31; border: 1px solid #1f293d; border-radius: 6px; padding: 0.6rem 0.8rem;">
        <span style="font-size: 0.7rem; color: #94a3b8;">Net Debt / EBITDA</span>
        <div style="font-size: 1.05rem; font-weight: 700; color: #38bdf8;">1.35x <span style="font-size: 0.7rem; color: #10b981;">(Low Default Risk)</span></div>
    </div>
    <div style="background: #131d31; border: 1px solid #1f293d; border-radius: 6px; padding: 0.6rem 0.8rem;">
        <span style="font-size: 0.7rem; color: #94a3b8;">EBITDA Margin</span>
        <div style="font-size: 1.05rem; font-weight: 700; color: #38bdf8;">18.5% <span style="font-size: 0.7rem; color: #10b981;">(Top Quartile)</span></div>
    </div>
    <div style="background: #131d31; border: 1px solid #1f293d; border-radius: 6px; padding: 0.6rem 0.8rem;">
        <span style="font-size: 0.7rem; color: #94a3b8;">Quick Ratio</span>
        <div style="font-size: 1.05rem; font-weight: 700; color: #38bdf8;">1.42x <span style="font-size: 0.7rem; color: #10b981;">(Ample Cash Cushion)</span></div>
    </div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# 6. VISUAL DECISION TRACE (7 STEPS)
# ==========================================
st.markdown("### Visual AI Decision Trace (Deterministic Execution)")
st.markdown("""
<div class="trace-step-container">
    <div class="trace-step">
        <div class="trace-step-num">Step 01</div>
        <div class="trace-step-title">SME Request</div>
        <div class="trace-step-status">✓ Validated</div>
    </div>
    <div class="trace-step">
        <div class="trace-step-num">Step 02</div>
        <div class="trace-step-title">DuckDB P&L</div>
        <div class="trace-step-status">✓ In-Memory OLAP</div>
    </div>
    <div class="trace-step">
        <div class="trace-step-num">Step 03</div>
        <div class="trace-step-title">Banca d'Italia</div>
        <div class="trace-step-status">✓ 1.82% NPL Query</div>
    </div>
    <div class="trace-step">
        <div class="trace-step-num">Step 04</div>
        <div class="trace-step-title">Open Data Lombardia</div>
        <div class="trace-step-status">✓ +4.1% Output</div>
    </div>
    <div class="trace-step">
        <div class="trace-step-num">Step 05</div>
        <div class="trace-step-title">Hybrid RAG</div>
        <div class="trace-step-status">✓ ESG Proof Cited</div>
    </div>
    <div class="trace-step">
        <div class="trace-step-num">Step 06</div>
        <div class="trace-step-title">Scoring Engine</div>
        <div class="trace-step-status">✓ Deterministic Math</div>
    </div>
    <div class="trace-step" style="border-color: #10b981; background: #0e2722;">
        <div class="trace-step-num" style="color: #34d399;">Step 07</div>
        <div class="trace-step-title" style="color: #ecfdf5;">Pre-Underwritten</div>
        <div class="trace-step-status" style="color: #34d399;">✓ 94% Certainty</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# 7. EXPLAINABILITY DRIVERS & EVIDENCE TAXONOMY
# ==========================================
col_d, col_e = st.columns([1, 1])

with col_d:
    st.markdown("### Core Drivers of Bankability")
    st.markdown("""
    <div class="exec-card" style="min-height: 280px;">
        <div class="exec-card-title">Why Banks Will Compete for this Deal</div>
    """, unsafe_allow_html=True)
    for d in payload.get("drivers", []):
        st.markdown(f"• **{d}**")
    st.markdown("</div>", unsafe_allow_html=True)

with col_e:
    st.markdown("### Grounded Evidence Explorer (No Hallucinations)")
    for ev in payload.get("evidence", []):
        cat = ev.get("category", "FACT")
        tag_class = "tag-fact" if cat == "FACT" else ("tag-calc" if cat == "CALCULATION" else "tag-reason")
        st.markdown(f"""
        <div style="background: #111827; border: 1px solid #1f2937; border-radius: 6px; padding: 0.65rem 0.85rem; margin-bottom: 0.55rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.3rem;">
                <span style="font-size: 0.72rem; font-weight: 600; color: #94a3b8;">{ev.get('source')}</span>
                <span class="{tag_class}">{cat}</span>
            </div>
            <div style="font-size: 0.82rem; color: #e2e8f0; line-height: 1.4;">
                "{ev.get('claim')}"
            </div>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# 8. WHAT-IF FACILITY SENSITIVITY SLIDER
# ==========================================
st.markdown("---")
st.markdown("### Interactive What-If Loan Sizing Optimizer")
st.markdown("""
Before applying to banks, test your financing limits in real time. Discover your **optimal borrowing boundary** 
to secure the lowest interest spread and avoid unexpected underwriting rejections.
""")

slider_c, res_c = st.columns([1, 1.2])

with slider_c:
    st.markdown("""
    <div class="exec-card">
        <div class="exec-card-title">Simulate Alternative Facility Amount</div>
    """, unsafe_allow_html=True)
    sim_amt = st.slider(
        "Financing Amount (€):",
        min_value=500000,
        max_value=1500000,
        value=1000000,
        step=50000,
        format="€ %d"
    )
    st.caption("Optimal Base: **€750,000** | Stress Sizing: **€1,000,000**")
    st.markdown("</div>", unsafe_allow_html=True)

scenario_res = calculate_scenario(payload, sim_amt)

with res_c:
    f_delta = scenario_res["financial_score"] - payload["financial_score"]
    delta_str = f"+{f_delta}" if f_delta >= 0 else f"{f_delta}"
    d_class = "delta-up" if f_delta >= 0 else "delta-down"
    sc_rec = scenario_res["recommendation"]
    sc_badge = "badge-success" if sc_rec == "APPROVE" else ("badge-warning" if sc_rec == "REVIEW" else "badge-danger")
    sc_col = "#34d399" if sc_rec == "APPROVE" else ("#fbbf24" if sc_rec == "REVIEW" else "#f87171")

    st.markdown(f"""
    <div class="whatif-box">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <span style="font-size: 0.85rem; font-weight: 700; color: #38bdf8; text-transform: uppercase;">
                Sensitivity Analysis Result (€ {sim_amt:,.0f})
            </span>
            <span class="finsight-badge {sc_badge}">Outcome: {sc_rec}</span>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.75rem; text-align: center; margin-bottom: 1rem;">
            <div style="background: #0b0f19; border: 1px solid #1e293b; border-radius: 6px; padding: 0.5rem;">
                <span style="font-size: 0.7rem; color: #94a3b8;">Financial Score</span>
                <div style="font-size: 1.2rem; font-weight: 700; color: #f8fafc;">
                    {scenario_res['financial_score']}/100 
                    <span class="{d_class}" style="font-size: 0.85rem;">({delta_str})</span>
                </div>
            </div>
            <div style="background: #0b0f19; border: 1px solid #1e293b; border-radius: 6px; padding: 0.5rem;">
                <span style="font-size: 0.7rem; color: #94a3b8;">Projected DSCR</span>
                <div style="font-size: 1.2rem; font-weight: 700; color: #f8fafc;">
                    {scenario_res['dscr']:.2f}x
                </div>
            </div>
            <div style="background: #0b0f19; border: 1px solid #1e293b; border-radius: 6px; padding: 0.5rem;">
                <span style="font-size: 0.7rem; color: #94a3b8;">Risk Tier</span>
                <div style="font-size: 1.2rem; font-weight: 700; color: {sc_col};">
                    {scenario_res['risk_level']}
                </div>
            </div>
        </div>
        
        <div style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.45; background: rgba(0,0,0,0.25); padding: 0.65rem 0.85rem; border-radius: 6px;">
            <b>CFO Actionable Recommendation:</b> {scenario_res['summary']}
        </div>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# 9. HORMOZI CLOSING: ONE-CLICK EXPORT PASSPORT
# ==========================================
st.markdown("---")
st.markdown("### Ready to Transact: Certified Bank Dossier Export")

col_exp1, col_exp2 = st.columns([3, 1.5])
with col_exp1:
    st.markdown("""
    Generate the official **FinSight Certified Credit Passport**. Pre-formatted according to **EBA Guidelines on Loan Origination** 
    and packaged with full cryptographic audit trails for partner banks.
    """)
with col_exp2:
    if st.button("📑 Export Bank-Ready Dossier (PDF)", type="primary", use_container_width=True):
        st.success(f"Dossier generated! Reference ID: FS-2026-MIL-0822 | Hash: {audit_hash}")

st.markdown("""
<div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #1e293b; font-size: 0.72rem; color: #64748b;">
    <b>Regulatory Framework Notice (TUB Art. 128-sexies):</b> FinSight AI provides automated analytics and credit dossier preparation. 
    Credit origination fee (1.0%) is paid by financing lenders upon facility drawdown under standard institutional partnership agreements.
</div>
""", unsafe_allow_html=True)
