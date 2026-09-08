"""
FinSight AI - Professional Pitch Deck Generator
===============================================
Generates a 16:9 widescreen, institutional-grade PowerPoint deck
tailored for hackathon judges and executive commercial banking leaders.
"""

import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def build_pitch_deck():
    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_slide_layout = prs.slide_layouts[6]

    # Color Palette Definitions
    BG_DARK = RGBColor(11, 15, 25)         # #0B0F19 Deep Obsidian
    CARD_BG = RGBColor(17, 24, 39)         # #111827 Dark Slate
    CARD_BORDER = RGBColor(31, 41, 55)     # #1F2937 Border Gray
    ACCENT_BLUE = RGBColor(56, 189, 248)   # #38BDF8 Ice Blue Accent
    PRIMARY_BLUE = RGBColor(37, 99, 235)   # #2563EB Royal Blue
    TEXT_WHITE = RGBColor(255, 255, 255)   # #FFFFFF Clean White
    TEXT_MUTED = RGBColor(148, 163, 184)   # #94A3B8 Slate Gray
    ACCENT_GREEN = RGBColor(16, 185, 129)  # #10B981 Emerald
    ACCENT_YELLOW = RGBColor(245, 158, 11) # #F59E0B Amber
    ACCENT_RED = RGBColor(239, 68, 68)     # #EF4444 Danger Red

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_DARK
        bg.line.color.rgb = BG_DARK
        return bg

    def add_header(slide, tag: str, title: str, subtitle: str = ""):
        # Category Tag
        tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.7), Inches(0.4))
        tf_tag = tag_box.text_frame
        tf_tag.word_wrap = True
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = tag.upper()
        p_tag.font.size = Pt(10)
        p_tag.font.bold = True
        p_tag.font.color.rgb = ACCENT_BLUE
        p_tag.font.name = "Arial"

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(11.7), Inches(0.8))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title
        p_title.font.size = Pt(24)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_WHITE
        p_title.font.name = "Arial"

        if subtitle:
            p_sub = tf_title.add_paragraph()
            p_sub.text = subtitle
            p_sub.font.size = Pt(13)
            p_sub.font.color.rgb = TEXT_MUTED
            p_sub.font.name = "Arial"

    def add_card(slide, left, top, width, height, title="", border_color=CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)

        if title:
            tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), width - Inches(0.4), Inches(0.5))
            p = tb.text_frame.paragraphs[0]
            p.text = title.upper()
            p.font.size = Pt(11)
            p.font.bold = True
            p.font.color.rgb = ACCENT_BLUE
            p.font.name = "Arial"
        return card

    # ==========================================================
    # SLIDE 1: TITLE / HOOK
    # ==========================================================
    s1 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s1)

    tb1 = s1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.3), Inches(3.8))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p_badge = tf1.paragraphs[0]
    p_badge.text = "AI2B HACKATHON 2026 • COMMERCIAL BANKING VERTICAL SLICE"
    p_badge.font.size = Pt(12)
    p_badge.font.bold = True
    p_badge.font.color.rgb = ACCENT_BLUE

    p_t1 = tf1.add_paragraph()
    p_t1.text = "FinSight AI"
    p_t1.font.size = Pt(54)
    p_t1.font.bold = True
    p_t1.font.color.rgb = TEXT_WHITE
    p_t1.space_after = Pt(10)

    p_sub1 = tf1.add_paragraph()
    p_sub1.text = "Autonomous Financial Intelligence & Credit Decision Engine"
    p_sub1.font.size = Pt(22)
    p_sub1.font.color.rgb = ACCENT_BLUE
    p_sub1.space_after = Pt(20)

    p_body1 = tf1.add_paragraph()
    p_body1.text = "Turning fragmented balance sheets, public economic data, and narrative ESG claims\ninto explainable, deterministic credit intelligence in under 10 seconds."
    p_body1.font.size = Pt(15)
    p_body1.font.color.rgb = TEXT_MUTED

    # Bottom Meta Bar
    add_card(s1, Inches(1.0), Inches(5.8), Inches(11.3), Inches(0.9))
    meta_box = s1.shapes.add_textbox(Inches(1.2), Inches(5.95), Inches(10.9), Inches(0.6))
    p_meta = meta_box.text_frame.paragraphs[0]
    p_meta.text = "TEAM: Loop Troops   |   CASE: EcoTex Milano (€750k Green Loan)   |   CORE PRINCIPLE: The LLM is NOT the calculator"
    p_meta.font.size = Pt(12)
    p_meta.font.bold = True
    p_meta.font.color.rgb = TEXT_WHITE

    # ==========================================================
    # SLIDE 2: THE PROBLEM / ECONOMIC TENSION (0:00 - 0:30)
    # ==========================================================
    s2 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s2)
    add_header(s2, "Market Friction & Opportunity", "The €400B Blindspot in SME Commercial Lending", 
               "Relationship Managers spend 3 weeks stitching fragmented evidence while loans stall.")

    cards_data = [
        ("Silo 1: Financial Statements", 
         "Proprietary ERP & Balance Sheets",
         "• Historical, backwards-looking data\n• Trapped in unstructured PDF reports\n• Manual ratio calculations prone to human latency\n• Takes 4 to 8 hours per dossier"),
        ("Silo 2: Macro & Regional Context", 
         "Public Benchmarks & Bank of Italy",
         "• Banca d'Italia credit default series rarely integrated\n• Regional open data (Lombardia) ignored\n• Underwriters miss local sector trends\n• Mispricing of regional risk spreads"),
        ("Silo 3: Sustainability & ESG", 
         "Narrative Audits & Green Taxonomy",
         "• Unverified sustainability claims\n• Compliance checklists create cognitive fatigue\n• No quantitative link between ESG and default risk\n• €400B green loan backlog across the EU")
    ]

    for idx, (tag, title, body) in enumerate(cards_data):
        left = Inches(0.8 + idx * 4.0)
        add_card(s2, left, Inches(2.2), Inches(3.7), Inches(4.5), title=tag)
        
        tb = s2.shapes.add_textbox(left + Inches(0.2), Inches(2.9), Inches(3.3), Inches(3.5))
        tf = tb.text_frame
        tf.word_wrap = True
        
        pt = tf.paragraphs[0]
        pt.text = title
        pt.font.size = Pt(14)
        pt.font.bold = True
        pt.font.color.rgb = TEXT_WHITE
        pt.space_after = Pt(12)
        
        for line in body.split("\n"):
            p = tf.add_paragraph()
            p.text = line
            p.font.size = Pt(12)
            p.font.color.rgb = TEXT_MUTED
            p.space_after = Pt(6)

    # ==========================================================
    # SLIDE 3: THE SOLUTION (0:30 - 1:00)
    # ==========================================================
    s3 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s3)
    add_header(s3, "Product Positioning", "FinSight AI: The Grounded Decision Engine",
               "An AI-powered co-pilot that evaluates credit, tests capital boundaries, and proves every claim.")

    sol_cards = [
        ("01 / Multi-Source Ingestion", "Unified Data Fabric", 
         "Ingests company balance sheets into DuckDB, queries live Banca d'Italia credit benchmarks, and syncs Open Data Lombardia sector output."),
        ("02 / Grounded Explainability", "Zero Black-Box Guessing", 
         "Every recommendation is backed by a verified audit trail separating verified FACT, deterministic CALCULATION, and synthesized REASONING."),
        ("03 / Instant Scenario Stress", "Capital Tipping Points", 
         "Interactive what-if sensitivity: instantly recalculates DSCR, leverage, and decision thresholds when facility sizing changes.")
    ]

    for idx, (tag, title, body) in enumerate(sol_cards):
        left = Inches(0.8 + idx * 4.0)
        add_card(s3, left, Inches(2.2), Inches(3.7), Inches(4.5), title=tag, border_color=PRIMARY_BLUE)
        
        tb = s3.shapes.add_textbox(left + Inches(0.25), Inches(2.9), Inches(3.2), Inches(3.5))
        tf = tb.text_frame
        tf.word_wrap = True
        
        pt = tf.paragraphs[0]
        pt.text = title
        pt.font.size = Pt(16)
        pt.font.bold = True
        pt.font.color.rgb = TEXT_WHITE
        pt.space_after = Pt(14)
        
        pb = tf.add_paragraph()
        pb.text = body
        pb.font.size = Pt(13)
        pb.font.color.rgb = TEXT_MUTED
        pb.line_spacing = 1.3

    # ==========================================================
    # SLIDE 4: ARCHITECTURE & THE GOLDEN RULE (1:00 - 1:45)
    # ==========================================================
    s4 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s4)
    add_header(s4, "System Architecture", "The Golden Rule: The LLM is NOT the Calculator",
               "Deterministic truth computes the score. The AI engine orchestrates and explains.")

    # Left Box: The Deterministic Engine
    add_card(s4, Inches(0.8), Inches(2.1), Inches(5.6), Inches(4.7), title="Deterministic Core (Zero Hallucination)", border_color=ACCENT_GREEN)
    tb_left = s4.shapes.add_textbox(Inches(1.0), Inches(2.8), Inches(5.2), Inches(3.8))
    tf_l = tb_left.text_frame
    tf_l.word_wrap = True
    
    pl1 = tf_l.paragraphs[0]
    pl1.text = "Mathematical & Rule-Based Analytics"
    pl1.font.size = Pt(15)
    pl1.font.bold = True
    pl1.font.color.rgb = ACCENT_GREEN
    pl1.space_after = Pt(10)
    
    l_points = [
        "• Structured Ingestion: DuckDB high-performance columnar engine",
        "• Quantitative Scoring: Liquidity (25%), Leverage (25%), Growth (20%), Sector (15%), Regional (15%)",
        "• Sensitivity Engine: Formulaic DSCR & Debt/EBITDA models",
        "• Regulatory Consistency: Same input guarantees exact same score every single execution run"
    ]
    for p in l_points:
        para = tf_l.add_paragraph()
        para.text = p
        para.font.size = Pt(12)
        para.font.color.rgb = TEXT_WHITE
        para.space_after = Pt(8)

    # Right Box: The AI & Retrieval Engine
    add_card(s4, Inches(6.8), Inches(2.1), Inches(5.7), Inches(4.7), title="AI & Evidence Engine (Semantic Rigor)", border_color=ACCENT_BLUE)
    tb_right = s4.shapes.add_textbox(Inches(7.0), Inches(2.8), Inches(5.3), Inches(3.8))
    tf_r = tb_right.text_frame
    tf_r.word_wrap = True

    pr1 = tf_r.paragraphs[0]
    pr1.text = "Context Synthesis & Tool Routing"
    pr1.font.size = Pt(15)
    pr1.font.bold = True
    pr1.font.color.rgb = ACCENT_BLUE
    pr1.space_after = Pt(10)

    r_points = [
        "• Hybrid RAG: Chunking & semantic search over audit disclosures",
        "• Public Benchmark Routing: Banca d'Italia + Open Data Lombardia",
        "• Synthesis Layer: Translates quantitative data into RM rationale",
        "• Strict Governance: Categorizes outputs into FACT, CALCULATION, and REASONING"
    ]
    for p in r_points:
        para = tf_r.add_paragraph()
        para.text = p
        para.font.size = Pt(12)
        para.font.color.rgb = TEXT_WHITE
        para.space_after = Pt(8)

    # ==========================================================
    # SLIDE 5: LIVE DEMO: ECOTEX MILANO BASE CASE (1:45 - 2:40)
    # ==========================================================
    s5 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s5)
    add_header(s5, "Live Execution Proof", "Base Case: EcoTex Milano €750k Facility Evaluation",
               "Evaluating equipment financing for sustainable dyeing & closed-loop water recycling.")

    # 4 Top KPI Cards
    kpis = [
        ("Financial Health", "82/100", "Safe (>70)", ACCENT_BLUE),
        ("ESG Alignment", "91/100", "Top Decile", ACCENT_GREEN),
        ("Regional Default Spread", "1.82%", "Milan vs IT 2.95%", ACCENT_YELLOW),
        ("Decision Output", "APPROVE", "87% Confidence", ACCENT_GREEN)
    ]

    for idx, (title, val, sub, color) in enumerate(kpis):
        left = Inches(0.8 + idx * 3.0)
        add_card(s5, left, Inches(2.0), Inches(2.8), Inches(1.8))
        
        tb = s5.shapes.add_textbox(left + Inches(0.15), Inches(2.1), Inches(2.5), Inches(1.6))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p0 = tf.paragraphs[0]
        p0.text = title.upper()
        p0.font.size = Pt(9)
        p0.font.color.rgb = TEXT_MUTED
        
        p1 = tf.add_paragraph()
        p1.text = val
        p1.font.size = Pt(24)
        p1.font.bold = True
        p1.font.color.rgb = color
        
        p2 = tf.add_paragraph()
        p2.text = sub
        p2.font.size = Pt(10)
        p2.font.color.rgb = TEXT_MUTED

    # Bottom Area: The 7-Step Decision Trace & Grounded Evidence
    add_card(s5, Inches(0.8), Inches(4.1), Inches(11.7), Inches(2.7), title="Visual AI Decision Trace & Evidence Grounding")
    tb_trace = s5.shapes.add_textbox(Inches(1.0), Inches(4.6), Inches(11.3), Inches(2.1))
    tf_t = tb_trace.text_frame
    tf_t.word_wrap = True

    steps = [
        "1. Ingestion: Request validated -> 2. DuckDB: €14.2M Rev, 18.5% EBITDA -> 3. BdI: Milan 1.82% NPL",
        "4. Lombardia: Sector +4.1% YoY -> 5. RAG: -42% Water Audit Verified -> 6. Deterministic Score -> 7. APPROVE"
    ]
    for s in steps:
        p = tf_t.add_paragraph()
        p.text = s
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = ACCENT_BLUE
        p.space_after = Pt(6)

    p_ev = tf_t.add_paragraph()
    p_ev.text = "Grounded Evidence: Banca d'Italia commercial credit database confirms Milanese default rates support standard pricing. EcoTex 2024 ESG audit validates project additionality and eligibility for regional transition capital subsidies."
    p_ev.font.size = Pt(11)
    p_ev.font.color.rgb = TEXT_MUTED

    # ==========================================================
    # SLIDE 6: INTERACTIVE WHAT-IF SENSITIVITY (2:40 - 3:30)
    # ==========================================================
    s6 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s6)
    add_header(s6, "Interactive Capital Sensitivity", "What-If Engine: Finding the Capital Tipping Point",
               "When the client asks for €1,000,000, what happens to risk, coverage, and approval?")

    # Left: Base Case €750k
    add_card(s6, Inches(0.8), Inches(2.2), Inches(5.6), Inches(4.5), title="Base Case Facility: €750,000", border_color=ACCENT_GREEN)
    tb_b = s6.shapes.add_textbox(Inches(1.0), Inches(2.9), Inches(5.2), Inches(3.6))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True

    p_b_head = tf_b.paragraphs[0]
    p_b_head.text = "Status: APPROVE (87% Confidence)"
    p_b_head.font.size = Pt(16)
    p_b_head.font.bold = True
    p_b_head.font.color.rgb = ACCENT_GREEN
    p_b_head.space_after = Pt(12)

    base_metrics = [
        "• Financial Health Score: 82 / 100",
        "• Projected DSCR: 1.68x (Resilient debt service buffer)",
        "• Net Debt / EBITDA: 1.35x (Conservative leverage)",
        "• Composite Risk: Medium Risk",
        "• Recommendation: Standard commercial loan committee approval"
    ]
    for bm in base_metrics:
        p = tf_b.add_paragraph()
        p.text = bm
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(6)

    # Right: Stressed Scenario €1,000,000
    add_card(s6, Inches(6.8), Inches(2.2), Inches(5.7), Inches(4.5), title="What-If Scenario: €1,000,000", border_color=ACCENT_YELLOW)
    tb_s = s6.shapes.add_textbox(Inches(7.0), Inches(2.9), Inches(5.3), Inches(3.6))
    tf_s = tb_s.text_frame
    tf_s.word_wrap = True

    p_s_head = tf_s.paragraphs[0]
    p_s_head.text = "Status: REVIEW (Underwriter Alert)"
    p_s_head.font.size = Pt(16)
    p_s_head.font.bold = True
    p_s_head.font.color.rgb = ACCENT_YELLOW
    p_s_head.space_after = Pt(12)

    scenario_metrics = [
        "• Financial Health Score: 74 / 100 (Drop of 8 points)",
        "• Projected DSCR: 1.28x (Breaches safe covenant threshold)",
        "• Net Debt / EBITDA: 1.95x (Elevated debt burden)",
        "• Composite Risk: High Risk Tier",
        "• Recommendation: Escalation required; requires covenant guarantees"
    ]
    for sm in scenario_metrics:
        p = tf_s.add_paragraph()
        p.text = sm
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(6)

    # ==========================================================
    # SLIDE 7: BUSINESS ROI & COMPLIANCE (3:30 - 4:15)
    # ==========================================================
    s7 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s7)
    add_header(s7, "Commercial Impact", "From 14 Days to 14 Seconds: Strategic Value",
               "Quantifiable efficiency, compliance assurance, and higher lending margins.")

    roi_cards = [
        ("Efficiency", "-85% Underwriting Time", 
         "Cuts preliminary credit assessment from 14 business days to under 15 seconds, allowing RMs to handle 4x deal volume without adding analyst headcount."),
        ("Compliance", "100% Audit Traceability", 
         "Fully compliant with EBA loan origination guidelines and EU CSRD reporting. Every claim is attributed to exact public and audited sources."),
        ("Risk Control", "Zero Calculator Hallucination", 
         "Eliminates generative AI liability. Credit committees gain deterministic mathematical safety combined with natural language intelligence.")
    ]

    for idx, (tag, title, body) in enumerate(roi_cards):
        left = Inches(0.8 + idx * 4.0)
        add_card(s7, left, Inches(2.2), Inches(3.7), Inches(4.5), title=tag, border_color=PRIMARY_BLUE)
        
        tb = s7.shapes.add_textbox(left + Inches(0.25), Inches(2.9), Inches(3.2), Inches(3.5))
        tf = tb.text_frame
        tf.word_wrap = True
        
        pt = tf.paragraphs[0]
        pt.text = title
        pt.font.size = Pt(16)
        pt.font.bold = True
        pt.font.color.rgb = TEXT_WHITE
        pt.space_after = Pt(14)
        
        pb = tf.add_paragraph()
        pb.text = body
        pb.font.size = Pt(13)
        pb.font.color.rgb = TEXT_MUTED
        pb.line_spacing = 1.3

    # ==========================================================
    # SLIDE 8: VISION & SCALE (4:15 - 5:00)
    # ==========================================================
    s8 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s8)
    add_header(s8, "Platform Vision", "The Horizon: Autonomous Portfolio Intelligence",
               "SME credit is our proving ground. The same engine expands across the bank.")

    horizon_cards = [
        ("Phase 1: Present Slice", "SME Credit Engine", 
         "• Single loan proposal analysis\n• DuckDB structured layer\n• Banca d'Italia & Lombardia data\n• Deterministic scoring & What-If"),
        ("Phase 2: Commercial Scale", "Portfolio Stress Testing", 
         "• Automated covenant monitoring\n• Sector-wide macro shock simulation\n• Continuous early-warning signals\n• Climate transition risk audit"),
        ("Phase 3: Wealth & Advisory", "Enterprise Intelligence", 
         "• Private wealth advisory co-pilot\n• Multi-asset liquidity optimization\n• Cross-border regulatory intelligence\n• Autonomous corporate deal structuring")
    ]

    for idx, (tag, title, body) in enumerate(horizon_cards):
        left = Inches(0.8 + idx * 4.0)
        add_card(s8, left, Inches(2.2), Inches(3.7), Inches(4.5), title=tag, border_color=ACCENT_BLUE if idx==0 else CARD_BORDER)
        
        tb = s8.shapes.add_textbox(left + Inches(0.25), Inches(2.9), Inches(3.2), Inches(3.5))
        tf = tb.text_frame
        tf.word_wrap = True
        
        pt = tf.paragraphs[0]
        pt.text = title
        pt.font.size = Pt(15)
        pt.font.bold = True
        pt.font.color.rgb = TEXT_WHITE
        pt.space_after = Pt(12)
        
        for line in body.split("\n"):
            p = tf.add_paragraph()
            p.text = line
            p.font.size = Pt(12)
            p.font.color.rgb = TEXT_MUTED
            p.space_after = Pt(6)

    # Save output presentation
    output_path = os.path.join(os.getcwd(), "presentation", "FinSight_AI_Pitch_Deck.pptx")
    prs.save(output_path)
    print(f"Presentation successfully created at: {output_path}")

if __name__ == "__main__":
    build_pitch_deck()
