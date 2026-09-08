# FinSight AI - 3 to 5 Minute Hackathon Pitch & Live Demo Script

**Event**: AI2B Hackathon 2026  
**Product**: FinSight AI (Autonomous Financial Intelligence & Decision Engine)  
**Team**: Loop Troops  
**Format**: 8-Slide Pitch Deck + Live Streamlit Interactive Demo  
**Target Persona / Audience**: Senior Hackathon Judges, Bank Executives, Credit Officers  

---

## Pitch Timing Architecture (3:30 - 4:45 Target)

| Segment | Timing | Anchor & Visual Action | Core Message / Frame Control |
|---|---|---|---|
| **1. Hook & Problem** | 0:00 - 0:35 | Slide 1 & 2 | The €400B Blindspot: Commercial underwriting is crippled by siloed data and 3-week delays. |
| **2. Solution** | 0:35 - 1:05 | Slide 3 | FinSight AI: Grounded decision engine turning weeks into 14 seconds. |
| **3. Architecture & Golden Rule** | 1:05 - 1:45 | Slide 4 | The LLM is NEVER the calculator. Deterministic truth + explainable AI. |
| **4. Live Demo (Base Case)** | 1:45 - 2:40 | Switch to Streamlit UI | EcoTex Milano €750k request. 7-step trace, 82/100 Health, 91/100 ESG, APPROVE. |
| **5. Live Demo (What-If Tipping Point)** | 2:40 - 3:30 | Streamlit Slider to €1.0M | Real-time stress test: DSCR drops to 1.28x, Score drops to 74, decision shifts to REVIEW. |
| **6. Economic ROI & Compliance** | 3:30 - 4:15 | Slide 7 | 85% time reduction, 100% audit trail, EBA & CSRD compliant. |
| **7. Platform Vision & Close** | 4:15 - 4:45 | Slide 8 | Scaling from SME credit to autonomous portfolio intelligence. |

---

## Word-For-Word Speaker Script & Stage Directions

### [0:00 - 0:35] Slide 1 & 2: The €400B Blindspot
*(Stand tall. Direct eye contact with the lead judge. No filler words. Begin immediately with economic tension.)*

> **"Judges, every single year, European banks leave over €400 billion on the table or misprice risk because commercial credit underwriting is stuck in three disconnected silos.**
>
> **On one side, relationship managers have historical balance sheets trapped in unreadable PDF audits. On another, public macroeconomic data—like Banca d'Italia credit default benchmarks and regional sector statistics—sits completely ignored in separate portals. And finally, green transition claims are treated as unverified marketing copy.**
>
> **The result? Evaluating a simple €750,000 SME equipment loan takes up to three weeks of manual analyst grunt work. That latency is an operational hemorrhage."**

---

### [0:35 - 1:05] Slide 3: The Solution
*(Transition slide with calm authority.)*

> **"This is why we built FinSight AI—an autonomous financial intelligence and credit decision engine for commercial banking.**
>
> **FinSight unifies proprietary company accounts, live central bank benchmarks, and regional economic indicators into a grounded, explainable credit decision in under 14 seconds.**
>
> **It doesn’t just output a number; it shows the credit committee exactly *why* the decision was made, proves every claim with verifiable citations, and simulates alternative capital structures in real time."**

---

### [1:05 - 1:45] Slide 4: Architectural Golden Rule
*(Adopt a serious, risk-aware tone. Bankers fear generative hallucinations; neutralize that fear now.)*

> **"Before showing you the software, here is the architectural principle that sets FinSight apart from every generic AI tool on the market:**
>
> **The LLM is NEVER the financial calculator.**
>
> **We never allow an LLM to guess a debt-service ratio or hallucinate a default score. In FinSight, 100% of the math—liquidity ratios, leverage, and multi-factor health scores—is executed deterministically inside DuckDB and Python analytical engines.**
>
> **The AI layer is strictly an orchestrator and synthesis engine: it routes queries to verified public sources, extracts audited evidence via hybrid RAG, and translates mathematical truth into executive underwriting clarity."**

---

### [1:45 - 2:40] LIVE DEMO: Base Case (€750,000 Facility)
*(Alt-Tab smoothly to the running Streamlit dashboard: `http://localhost:8501`. Point with mouse cursor to the Application Dossier card.)*

> **"Let's see it live on our institutional terminal.**
>
> **Here is EcoTex Milano S.p.A., a technical textile manufacturer in Milan requesting a €750,000 facility for water-recycling and energy-efficient machinery.**
>
> *(Click '⚡ Quick-Load EcoTex Milano' or '🚀 Evaluate')*
>
> **Watch our Visual AI Decision Trace at the center:**
> 1. Ingestion validates the proposal.
> 2. DuckDB extracts €14.2M audited revenues and an 18.5% EBITDA margin.
> 3. We pull Banca d'Italia’s commercial credit series: Milan's NPL default rate is 1.82%, outperforming the national average of 2.95%.
> 4. Open Data Lombardia verifies that technical textile turnover grew 4.1% year-on-year.
> 5. Our RAG engine extracts the audited 42% water consumption reduction certificate.
>
> **Look at the gauges:**
> - Financial Health Score: **82/100** (Solidly Investment Grade).
> - ESG Alignment Score: **91/100** (Full EU Taxonomy compliance).
> - Recommendation: **APPROVE with 87% statistical confidence.**
>
> **And notice our Grounded Evidence Explorer below: every claim is tagged as a verified FACT, a formulaic CALCULATION, or reasoned SYNTHESIS. Zero black-box liability."**

---

### [2:40 - 3:30] LIVE DEMO: What-If Sensitivity (The €1.0M Tipping Point)
*(Place your hand on the trackpad. Move the What-If slider from €750,000 to €1,000,000.)*

> **"Now, here is where traditional underwriting breaks down. Suppose the client calls and asks:**
>
> *'Can you increase our facility from €750k to €1,000,000?'*
>
> **Normally, that request restarts a 2-week underwriting loop. With FinSight, the credit officer simply moves the capital slider to €1.0M.**
>
> *(Drag slider to €1,000,000)*
>
> **Look at the instant deterministic recalculation:**
> - Projected Debt Service Coverage (DSCR) drops from 1.68x down to **1.28x**, breaching our bank’s covenant buffer.
> - Financial Health Score drops 8 points to **74/100**.
> - The recommendation instantly flips from **APPROVE to REVIEW**, automatically generating the specific covenant requirements needed before approval.
>
> **This gives relationship managers instant, interactive capital boundary control right in front of the borrower."**

---

### [3:30 - 4:15] Slide 7: Economic ROI & Defensibility
*(Alt-Tab back to Slide 7 of the pitch deck.)*

> **"What does this mean for a mid-sized commercial bank handling 15,000 SME applications a year?**
>
> 1. **85% Cycle Time Reduction**: Underwriting preliminary assessment drops from 14 business days to under 15 seconds. Relationship managers handle four times the volume without increasing head-count.
> 2. **100% Audit Compliance**: Complete adherence to EBA loan origination guidelines and upcoming EU CSRD transparency standards. Every credit decision has a deterministic trail.
> 3. **Mathematical Safety**: By strictly separating deterministic calculation from semantic explanation, we eliminate the AI hallucination risk that keeps bank risk committees awake at night."**

---

### [4:15 - 4:45] Slide 8: Platform Horizon & Closing
*(Direct, confident finish. Frame the platform as inevitable.)*

> **"Today’s vertical slice proves the SME credit engine. But this is just the foundation.**
>
> **The exact same architecture—DuckDB columnar storage, public economic benchmarks, deterministic scoring, and scenario simulation—scales naturally into continuous portfolio stress testing, automated covenant monitoring, and private wealth advisory.**
>
> **FinSight turns fragmented financial data into explainable, grounded intelligence. Thank you, and we look forward to your questions."**

---

## Rapid Q&A Defense Cheat Sheet (Anticipating Judge Objections)

### Q1: "Why shouldn't we just use ChatGPT or Claude with a custom prompt to evaluate the loan?"
> **Answer**: "Because LLMs cannot be trusted to do financial mathematics or credit scoring. If you ask an LLM to calculate a DSCR on a €1M facility with a 5.25% amortization schedule, it will generate a plausible-sounding number that is often mathematically wrong. In regulated banking, that is an existential compliance liability. In FinSight, 100% of the math is executed deterministically by Python and DuckDB; the LLM is only used to synthesize explanations and ground textual evidence."

### Q2: "Where does the regional data come from, and how fresh is it?"
> **Answer**: "We ingest two primary public streams: Banca d'Italia provincial credit default series (NPL rates by province and sector) and Open Data Lombardia enterprise census indicators. These provide regional macroeconomic risk context that banks typically have to purchase through expensive proprietary rating bureaus."

### Q3: "How does the system ensure zero downtime if the LLM API experiences rate limits or network issues?"
> **Answer**: "We designed FinSight with an antifragile dual-mode architecture. In the event of an API timeout, rate limit, or network severance, the client automatically engages our deterministic fallback protocol, returning validated benchmark payloads and continuing to run the local math engine without a single UI freeze or crash."
