"""
FinSight AI - Ultra-Modern Frontier Executive Pitch Deck
=========================================================
Strictly 6 slides, world-class startup design inspired by Linear, Stripe, and Ramp.
Deep obsidian canvas (#06090E), vibrant tech cyan (#38BDF8) & institutional emerald (#10B981).
Features top accent glow bars, pill badges, massive tabular metrics (Consolas),
vector covenant headroom visualizer, and side-by-side market asymmetry cards.
"""

import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN

def build_pitch_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # World-Class Color Palette matching Streamlit Frontend
    BG_OBSIDIAN = RGBColor(6, 9, 14)          # #06090E Deep Canvas
    CARD_BG = RGBColor(13, 19, 32)            # #0D1320 Surface Glass
    CARD_SURFACE_ALT = RGBColor(17, 24, 39)   # #111827 Dark Slate
    CARD_BORDER = RGBColor(30, 41, 59)        # #1E293B Subtle Hairline
    
    CYAN_PRIMARY = RGBColor(56, 189, 248)     # #38BDF8 Vibrant Cyan
    CYAN_DEEP = RGBColor(2, 132, 199)         # #0284C7 Linear Blue
    EMERALD_SAFE = RGBColor(16, 185, 129)     # #10B981 Institutional Emerald
    EMERALD_LIGHT = RGBColor(52, 211, 153)    # #34D399 Glow Emerald
    AMBER_WATCH = RGBColor(245, 158, 11)      # #F59E0B Watchlist Amber
    ROSE_BREACH = RGBColor(244, 63, 94)       # #F43F5E Risk Rose
    INDIGO_ACCENT = RGBColor(99, 102, 241)    # #6366F1 Tech Indigo
    PURPLE_ACCENT = RGBColor(168, 85, 247)    # #A855F7 Regulatory Purple

    TEXT_WHITE = RGBColor(255, 255, 255)      # #FFFFFF Pure
    TEXT_LIGHT = RGBColor(241, 245, 249)      # #F1F5F9 Off-white
    TEXT_MUTED = RGBColor(148, 163, 184)      # #94A3B8 Slate Muted
    TEXT_DIM = RGBColor(100, 116, 139)        # #64748B Dim Slate

    def set_slide_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_OBSIDIAN
        bg.line.color.rgb = BG_OBSIDIAN
        return bg

    def add_header(slide, kicker: str, title: str, subtitle: str = ""):
        # Kicker Badge Pill
        pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.38), Inches(3.4), Inches(0.28))
        pill.fill.solid()
        pill.fill.fore_color.rgb = RGBColor(15, 23, 42)
        pill.line.color.rgb = CYAN_PRIMARY
        pill.line.width = Pt(1.0)
        p_tf = pill.text_frame
        p_tf.word_wrap = False
        p_tf.margin_left = Inches(0.1)
        p_tf.margin_top = Inches(0.02)
        p = p_tf.paragraphs[0]
        p.text = f"●  {kicker.upper()}"
        p.font.size = Pt(8.5)
        p.font.bold = True
        p.font.color.rgb = CYAN_PRIMARY
        p.font.name = "Consolas"

        # Main Title & Subtitle box
        t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.72), Inches(11.7), Inches(1.15))
        tf = t_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p_title = tf.paragraphs[0]
        p_title.text = title
        p_title.font.size = Pt(25)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_WHITE
        p_title.font.name = "Segoe UI"
        p_title.space_after = Pt(4)

        if subtitle:
            p_sub = tf.add_paragraph()
            p_sub.text = subtitle
            p_sub.font.size = Pt(12)
            p_sub.font.color.rgb = TEXT_MUTED
            p_sub.font.name = "Segoe UI"

    def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=CARD_BORDER, top_accent=None):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.2)

        # Linear/Stripe style top accent glow bar
        if top_accent:
            accent_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left + Inches(0.08), top + Inches(0.02), width - Inches(0.16), Inches(0.035))
            accent_bar.fill.solid()
            accent_bar.fill.fore_color.rgb = top_accent
            accent_bar.line.color.rgb = top_accent

        return card

    def add_footer_telemetry(slide, active_id="ECOTEX-2026-IT"):
        bar = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(11.7), Inches(0.35))
        tf = bar.text_frame
        tf.margin_left = tf.margin_top = 0
        p = tf.paragraphs[0]
        p.text = f"DUCKDB 1.0 IN-MEMORY OLAP  |  APPLICATION ID: {active_id}  |  EBA/GL/2020/06 COMPLIANT  |  TUB ART. 128-SEXIES SEAL"
        p.font.size = Pt(8.5)
        p.font.bold = True
        p.font.color.rgb = TEXT_DIM
        p.font.name = "Consolas"

    # ==========================================================
    # SLIDE 1: INTRIGUE HOOK & PRODUCT VISION
    # ==========================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s1)

    # Ambient Top Badge Pill
    top_badge = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.8), Inches(6.2), Inches(0.38))
    top_badge.fill.solid()
    top_badge.fill.fore_color.rgb = RGBColor(15, 23, 42)
    top_badge.line.color.rgb = CYAN_PRIMARY
    top_badge.line.width = Pt(1.2)
    tb_tf = top_badge.text_frame
    tb_tf.margin_left = Inches(0.15)
    tb_tf.margin_top = Inches(0.04)
    p_b = tb_tf.paragraphs[0]
    p_b.text = "⚡ DUCKDB IN-MEMORY OLAP ENGINE  //  LATENCY < 4ms  //  EBA COMPLIANT"
    p_b.font.size = Pt(9)
    p_b.font.bold = True
    p_b.font.color.rgb = CYAN_PRIMARY
    p_b.font.name = "Consolas"

    # Main Hero Title
    hero_box = s1.shapes.add_textbox(Inches(0.8), Inches(1.35), Inches(11.7), Inches(3.2))
    htf = hero_box.text_frame
    htf.word_wrap = True
    htf.margin_left = htf.margin_top = 0

    p_hero = htf.paragraphs[0]
    p_hero.text = "FinSight AI"
    p_hero.font.size = Pt(56)
    p_hero.font.bold = True
    p_hero.font.color.rgb = TEXT_WHITE
    p_hero.font.name = "Segoe UI"
    p_hero.space_after = Pt(4)

    p_sub = htf.add_paragraph()
    p_sub.text = "The Autonomous SME Credit Readiness & Capital Sizing Copilot"
    p_sub.font.size = Pt(22)
    p_sub.font.bold = True
    p_sub.font.color.rgb = CYAN_PRIMARY
    p_sub.font.name = "Segoe UI"
    p_sub.space_after = Pt(14)

    p_desc = htf.add_paragraph()
    p_desc.text = "Eliminating the 3-week borrowing black box for European SMEs.\nFusing statutory balance sheets, Banca d'Italia provincial default data, and ESG disclosures\ninto an institutional, pre-underwritten credit dossier in 14 seconds."
    p_desc.font.size = Pt(14)
    p_desc.font.color.rgb = TEXT_MUTED
    p_desc.font.name = "Segoe UI"

    # 3 Stat Cards on Slide 1
    s1_stats = [
        ("EXECUTION LATENCY", "14s", "vs 21 Days Bank Processing", CYAN_PRIMARY),
        ("UNDERWRITING CERTAINTY", "94%", "Banca d'Italia Pre-Audited", EMERALD_SAFE),
        ("ACCIDENTAL BLACK BOX", "0%", "Deterministic DuckDB Engine", EMERALD_LIGHT)
    ]
    for idx, (label, val, sub, col) in enumerate(s1_stats):
        left = Inches(0.8 + idx * 3.95)
        add_card(s1, left, Inches(4.7), Inches(3.8), Inches(1.6), top_accent=col)
        tb = s1.shapes.add_textbox(left + Inches(0.25), Inches(4.85), Inches(3.3), Inches(1.3))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = 0
        p0 = tf.paragraphs[0]
        p0.text = label
        p0.font.size = Pt(8.5)
        p0.font.bold = True
        p0.font.color.rgb = TEXT_DIM
        p0.font.name = "Consolas"
        p1 = tf.add_paragraph()
        p1.text = val
        p1.font.size = Pt(38)
        p1.font.bold = True
        p1.font.color.rgb = col
        p1.font.name = "Consolas"
        p2 = tf.add_paragraph()
        p2.text = sub
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = TEXT_MUTED
        p2.font.name = "Segoe UI"

    # Proving Case Callout Banner
    add_card(s1, Inches(0.8), Inches(6.5), Inches(11.7), Inches(0.55), bg_color=CARD_SURFACE_ALT, border_color=CYAN_DEEP)
    cb = s1.shapes.add_textbox(Inches(1.0), Inches(6.58), Inches(11.3), Inches(0.4))
    cb_tf = cb.text_frame
    cb_tf.margin_left = cb_tf.margin_top = 0
    p_c = cb_tf.paragraphs[0]
    p_c.text = "PROVING CASE: EcoTex Milano S.p.A. (€750k CapEx Facility)  |  DISTRIBUTION: 120,000 Italian Corporate Accounting Firms  |  TEAM: Loop Troops"
    p_c.font.size = Pt(9.5)
    p_c.font.bold = True
    p_c.font.color.rgb = TEXT_LIGHT
    p_c.font.name = "Consolas"


    # ==========================================================
    # SLIDE 2: THE MARKET ASYMMETRY — BLACK BOX VS FINSIGHT
    # ==========================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s2)
    add_header(s2, "Market Friction & Information Asymmetry",
               "Why 40% of Sound SMEs Face Rejection or Rate Spikes",
               "Borrowers apply blindfolded; banks spend weeks manually re-keying data into spreadsheets.")

    # Left Card: The Status Quo (Negative/Risk Tone)
    add_card(s2, Inches(0.8), Inches(2.0), Inches(5.7), Inches(4.8), top_accent=ROSE_BREACH)
    tb_left = s2.shapes.add_textbox(Inches(1.1), Inches(2.15), Inches(5.1), Inches(4.5))
    tf_l = tb_left.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = tf_l.margin_top = 0

    p = tf_l.paragraphs[0]
    p.text = "THE STATUS QUO // 21-DAY BLACK BOX"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = ROSE_BREACH
    p.font.name = "Consolas"

    p = tf_l.add_paragraph()
    p.text = "Borrowing in the Dark"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.font.name = "Segoe UI"
    p.space_after = Pt(12)

    points_l = [
        ("The Information Vacuum", "SMEs have zero visibility into credit scoring rules before applying, triggering preventable rejections and margin surcharges."),
        ("The 3-Week Bureaucratic Drag", "Manual financial re-keying and document assembly stalls CapEx investments; market opportunities vanish while loans sit in underwriting."),
        ("Unmonetized ESG Investments", "SMEs invest tens of thousands in decarbonization without proof, missing -45 bps rate subsidies and regional transition grants.")
    ]
    for head, body in points_l:
        p = tf_l.add_paragraph()
        p.text = f"✖  {head}"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = ROSE_BREACH
        p.font.name = "Segoe UI"
        p = tf_l.add_paragraph()
        p.text = body
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_MUTED
        p.font.name = "Segoe UI"
        p.space_after = Pt(8)

    # Right Card: The FinSight Engine (Positive/Solution Tone)
    add_card(s2, Inches(6.8), Inches(2.0), Inches(5.7), Inches(4.8), top_accent=EMERALD_SAFE)
    tb_right = s2.shapes.add_textbox(Inches(7.1), Inches(2.15), Inches(5.1), Inches(4.5))
    tf_r = tb_right.text_frame
    tf_r.word_wrap = True
    tf_r.margin_left = tf_r.margin_top = 0

    p = tf_r.paragraphs[0]
    p.text = "FINSIGHT AI // DETERMINISTIC CERTAINTY"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = EMERALD_SAFE
    p.font.name = "Consolas"

    p = tf_r.add_paragraph()
    p.text = "The Algorithmic Advantage"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.font.name = "Segoe UI"
    p.space_after = Pt(12)

    points_r = [
        ("Instant Pre-Underwriting (14s)", "In-memory DuckDB parses official CEE balance sheets in RAM, computing exact DSCR, leverage, and solvency benchmarks before bank submission."),
        ("Banca d'Italia Macro Fusion", "Integrates provincial default rates (Milan NPL: 1.82%) and Lombardia sector trends (+4.1%) directly into credit bargaining leverage."),
        ("Capitalized Green Proof", "Vector RAG extracts verified ISO and ZDHC audit disclosures to secure subsidized prime rates (-45 bps) and regional grants.")
    ]
    for head, body in points_r:
        p = tf_r.add_paragraph()
        p.text = f"✔  {head}"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = EMERALD_LIGHT
        p.font.name = "Segoe UI"
        p = tf_r.add_paragraph()
        p.text = body
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_MUTED
        p.font.name = "Segoe UI"
        p.space_after = Pt(8)

    add_footer_telemetry(s2)


    # ==========================================================
    # SLIDE 3: PROPRIETARY ARCHITECTURE — THE GLASS BOX MOAT
    # ==========================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s3)
    add_header(s3, "Proprietary Mechanism & Tech Stack",
               "The 4-Pillar Glass Box: In-Memory, Deterministic, Auditable",
               "Golden Rule: The LLM is NEVER the financial calculator. Pure deterministic math in DuckDB; AI synthesizes evidence.")

    arch_pillars = [
        ("01 / IN-MEMORY OLAP", "DuckDB 1.0", "< 4ms Query",
         "• Columnar SQL engine running locally in RAM.\n• Ingests Italian statutory CEE CSVs & PDFs.\n• Total data sovereignty: sensitive accounting records never leave the local environment.\n• Zero latency cloud dependencies.",
         CYAN_PRIMARY),
        ("02 / MACRO FUSION", "Banca d'Italia", "1.82% NPL",
         "• Live query of central bank provincial credit default benchmarks.\n• Syncs with Open Data Lombardia sector growth (+4.1% YoY).\n• Turns regional economic strength into immediate rate bargaining power.",
         INDIGO_ACCENT),
        ("03 / DETERMINISTIC MATH", "Python / Pydantic", "100% Exact",
         "• Mathematical computation of DSCR (3.37x), Net Debt / EBITDA (1.24x), and Quick Ratios.\n• Bank-grade credit scoring rules executed with hard-coded formulas.\n• Zero mathematical hallucination.",
         EMERALD_SAFE),
        ("04 / REGULATORY PDF", "EBA / OAM Dossier", "SHA-256 Seal",
         "• Institutional vector PDF Credit Memorandum compliant with EBA/GL/2020/06.\n• TUB Art. 128-sexies integrity seal.\n• Dual workspace linking SME CFO and Bank Underwriter through Application ID.",
         PURPLE_ACCENT)
    ]

    for idx, (tag, title, badge_txt, body, accent_c) in enumerate(arch_pillars):
        left = Inches(0.8 + idx * 2.97)
        add_card(s3, left, Inches(2.0), Inches(2.8), Inches(4.8), top_accent=accent_c)
        tb = s3.shapes.add_textbox(left + Inches(0.2), Inches(2.15), Inches(2.4), Inches(4.5))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = 0

        p0 = tf.paragraphs[0]
        p0.text = tag
        p0.font.size = Pt(8.5)
        p0.font.bold = True
        p0.font.color.rgb = accent_c
        p0.font.name = "Consolas"

        p1 = tf.add_paragraph()
        p1.text = title
        p1.font.size = Pt(16)
        p1.font.bold = True
        p1.font.color.rgb = TEXT_WHITE
        p1.font.name = "Segoe UI"

        # Mini Badge
        p_b = tf.add_paragraph()
        p_b.text = f"[{badge_txt}]"
        p_b.font.size = Pt(9.5)
        p_b.font.bold = True
        p_b.font.color.rgb = accent_c
        p_b.font.name = "Consolas"
        p_b.space_after = Pt(10)

        for line in body.split("\n"):
            p = tf.add_paragraph()
            p.text = line
            p.font.size = Pt(10)
            p.font.color.rgb = TEXT_MUTED
            p.font.name = "Segoe UI"
            p.space_after = Pt(4)

    add_footer_telemetry(s3)


    # ==========================================================
    # SLIDE 4: LIVE DEMO ANCHOR: ECOTEX MILANO PROVING CASE
    # ==========================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s4)
    add_header(s4, "Live Demonstration & Stress Lab",
               "EcoTex Milano: Ingestion, Scoring & Capital Sizing Lab",
               "Live Case Study (ID: ECOTEX-2026-IT): €750k CapEx sustainability facility evaluated in 14 seconds.")

    # Top 4 Quantitative Hero Tiles
    kpis = [
        ("REQUESTED FACILITY", "€ 750,000", "5.15% Prime SLL Rate", CYAN_PRIMARY),
        ("POST-DEBT DSCR", "3.37x", "Covenant Floor: > 1.30x", EMERALD_SAFE),
        ("HEALTH SCORE", "97 / 100", "Prime Solvency Tier", TEXT_WHITE),
        ("BANKABILITY OUTCOME", "APPROVE", "Pre-Approved by Algorithm", EMERALD_LIGHT)
    ]
    for idx, (label, val, sub, col) in enumerate(kpis):
        left = Inches(0.8 + idx * 2.97)
        add_card(s4, left, Inches(2.0), Inches(2.8), Inches(1.5), top_accent=col)
        tb = s4.shapes.add_textbox(left + Inches(0.2), Inches(2.12), Inches(2.4), Inches(1.3))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = 0
        p0 = tf.paragraphs[0]
        p0.text = label
        p0.font.size = Pt(8.5)
        p0.font.bold = True
        p0.font.color.rgb = TEXT_DIM
        p0.font.name = "Consolas"
        p1 = tf.add_paragraph()
        p1.text = val
        p1.font.size = Pt(24)
        p1.font.bold = True
        p1.font.color.rgb = col
        p1.font.name = "Consolas"
        p2 = tf.add_paragraph()
        p2.text = sub
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = TEXT_MUTED
        p2.font.name = "Segoe UI"

    # Middle Card: Vector Covenant Headroom Visualization
    add_card(s4, Inches(0.8), Inches(3.7), Inches(11.7), Inches(1.2), top_accent=CYAN_PRIMARY)
    tb_head = s4.shapes.add_textbox(Inches(1.0), Inches(3.78), Inches(11.3), Inches(1.0))
    tf_h = tb_head.text_frame
    tf_h.word_wrap = True
    tf_h.margin_left = tf_h.margin_top = 0
    p = tf_h.paragraphs[0]
    p.text = "COVENANT HEADROOM GAUGE // SOLVENCY ABSORPTION BUFFER"
    p.font.size = Pt(9)
    p.font.bold = True
    p.font.color.rgb = CYAN_PRIMARY
    p.font.name = "Consolas"

    # Vector Headroom Bar Graphic directly in PPTX!
    bar_left = Inches(1.0)
    bar_top = Inches(4.12)
    bar_w = Inches(11.3)
    bar_h = Inches(0.22)

    # 3 Color Bands: Rose (0 - 1.0x), Amber (1.0 - 1.30x), Emerald (1.30x - 4.0x)
    band_rose = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, bar_left, bar_top, bar_w * 0.25, bar_h)
    band_rose.fill.solid()
    band_rose.fill.fore_color.rgb = RGBColor(127, 29, 29)
    band_rose.line.fill.background()

    band_amber = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, bar_left + bar_w * 0.25, bar_top, bar_w * 0.075, bar_h)
    band_amber.fill.solid()
    band_amber.fill.fore_color.rgb = RGBColor(180, 83, 9)
    band_amber.line.fill.background()

    band_emerald = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, bar_left + bar_w * 0.325, bar_top, bar_w * 0.675, bar_h)
    band_emerald.fill.solid()
    band_emerald.fill.fore_color.rgb = RGBColor(6, 95, 70)
    band_emerald.line.fill.background()

    # Active Marker at 3.37x (approx 84% of 4.0x scale)
    marker = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, bar_left + bar_w * 0.84, bar_top - Inches(0.04), Inches(0.06), bar_h + Inches(0.08))
    marker.fill.solid()
    marker.fill.fore_color.rgb = TEXT_WHITE
    marker.line.fill.background()

    # Covenant Threshold Line at 1.30x (32.5% of scale)
    cov_line = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, bar_left + bar_w * 0.325, bar_top - Inches(0.04), Inches(0.04), bar_h + Inches(0.08))
    cov_line.fill.solid()
    cov_line.fill.fore_color.rgb = AMBER_WATCH
    cov_line.line.fill.background()

    # Headroom text annotation
    tb_anno = s4.shapes.add_textbox(Inches(1.0), Inches(4.42), Inches(11.3), Inches(0.35))
    tf_a = tb_anno.text_frame
    tf_a.margin_left = tf_a.margin_top = 0
    p_a = tf_a.paragraphs[0]
    p_a.text = "● Buffer Solvibilità: +2.07x sopra soglia covenant (1.30x)  |  Resiste a shock EBITDA fino a -61.4% prima del default  |  Scala: 0.0x → 4.0x"
    p_a.font.size = Pt(8.5)
    p_a.font.color.rgb = EMERALD_LIGHT
    p_a.font.name = "Consolas"

    # Bottom Area: What-If Stress Callout & Prescriptive CFO Action
    add_card(s4, Inches(0.8), Inches(5.1), Inches(11.7), Inches(1.7), top_accent=AMBER_WATCH)
    tb_w = s4.shapes.add_textbox(Inches(1.0), Inches(5.22), Inches(11.3), Inches(1.5))
    tf_w = tb_w.text_frame
    tf_w.word_wrap = True
    tf_w.margin_left = tf_w.margin_top = 0

    pw1 = tf_w.paragraphs[0]
    pw1.text = "SENSITIVITY EXPERIMENT // THE €1.0M TIPPING POINT"
    pw1.font.size = Pt(9.5)
    pw1.font.bold = True
    pw1.font.color.rgb = AMBER_WATCH
    pw1.font.name = "Consolas"
    pw1.space_after = Pt(3)

    pw2 = tf_w.add_paragraph()
    pw2.text = "• BASE CASE (€750k): DSCR 3.37x | Health Score 97/100 | Pre-Approved at prime 5.15% fixed rate + €112k regional green grant."
    pw2.font.size = Pt(11)
    pw2.font.bold = True
    pw2.font.color.rgb = EMERALD_LIGHT
    pw2.font.name = "Segoe UI"
    pw2.space_after = Pt(2)

    pw3 = tf_w.add_paragraph()
    pw3.text = "• STRESS CASE (€1.0M+): DSCR drops to 1.28x | Net Debt/EBITDA expands to 2.25x | Pushes file into bank REVIEW watchlist."
    pw3.font.size = Pt(11)
    pw3.font.bold = True
    pw3.font.color.rgb = ROSE_BREACH
    pw3.font.name = "Segoe UI"
    pw3.space_after = Pt(4)

    pw4 = tf_w.add_paragraph()
    pw4.text = "💡 ACTIONABLE CFO RECOMMENDATION: Cap senior bank debt at €750k to preserve prime pricing. Fund the remaining €250k through Lombardia Green Transition Grant, guaranteeing 100% delibera approval."
    pw4.font.size = Pt(11)
    pw4.font.bold = True
    pw4.font.color.rgb = TEXT_WHITE
    pw4.font.name = "Segoe UI"

    add_footer_telemetry(s4)


    # ==========================================================
    # SLIDE 5: BUSINESS MODEL & UNIT ECONOMICS
    # ==========================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s5)
    add_header(s5, "Commercial Strategy & Distribution",
               "Business Model: B2B2C Accountant Flywheel & Zero Direct CAC",
               "High margins, self-funding transaction economics, and distribution leveraged through 120,000 corporate accounting firms.")

    bm_pillars = [
        ("TRANSACTION PRICING", "Freemium + Success Fee", "€3,500 - €7,500",
         "• Free Bankability Scan: Instant diagnostic to onboard SMEs at zero acquisition cost.\n• Success Fee upon Loan Drawdown: 0.5% - 1.0% paid only when funds hit the SME's account.\n• Average deal revenue: €5,000.\n• Pure ROI for the SME: Unlocked -45 bps rate discount pays for FinSight 3x over.",
         CYAN_PRIMARY),
        ("DISTRIBUTION CHANNEL", "B2B2C Accountant Flywheel", "120,000 Firms",
         "• Italy has 120,000 corporate accounting firms (Commercialisti) advising SMEs.\n• Accountants manage SME credit applications but lack algorithmic underwriting tools.\n• FinSight provides a white-label 'Credit Readiness Console'.\n• 1 Accounting Partner = 25+ SME loan dossiers annually.\n• Slashes blended CAC to < €250.",
         EMERALD_SAFE),
        ("UNIT ECONOMICS", "Capital Efficient Scale", "20x+ LTV / CAC",
         "• Target Facility Size: €500k - €1.5M\n• Average Net Revenue per Deal: €5,000\n• Customer Acquisition Cost (CAC): €250\n• LTV / CAC Ratio: > 20x\n• Gross Margin: 92% (pure software & compute)\n• Highly cash-flow generative from pilot cohort with zero working capital lockup.",
         PURPLE_ACCENT)
    ]

    for idx, (kicker, title, big_stat, body, accent_c) in enumerate(bm_pillars):
        left = Inches(0.8 + idx * 4.0)
        add_card(s5, left, Inches(2.0), Inches(3.7), Inches(4.8), top_accent=accent_c)
        tb = s5.shapes.add_textbox(left + Inches(0.25), Inches(2.15), Inches(3.2), Inches(4.5))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = 0

        p0 = tf.paragraphs[0]
        p0.text = kicker
        p0.font.size = Pt(8.5)
        p0.font.bold = True
        p0.font.color.rgb = accent_c
        p0.font.name = "Consolas"

        p1 = tf.add_paragraph()
        p1.text = title
        p1.font.size = Pt(17)
        p1.font.bold = True
        p1.font.color.rgb = TEXT_WHITE
        p1.font.name = "Segoe UI"

        p_stat = tf.add_paragraph()
        p_stat.text = big_stat
        p_stat.font.size = Pt(28)
        p_stat.font.bold = True
        p_stat.font.color.rgb = accent_c
        p_stat.font.name = "Consolas"
        p_stat.space_after = Pt(10)

        for line in body.split("\n"):
            p = tf.add_paragraph()
            p.text = line
            p.font.size = Pt(10.5)
            p.font.color.rgb = TEXT_MUTED
            p.font.name = "Segoe UI"
            p.space_after = Pt(5)

    add_footer_telemetry(s5)


    # ==========================================================
    # SLIDE 6: 3-STEP ROLLOUT & STRATEGIC ROADMAP
    # ==========================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s6)
    add_header(s6, "Implementation Roadmap",
               "Execution Plan: From Lombardia Pilot to Pan-European Gateway",
               "A focused 3-step operational rollout driving rapid volume and regulatory defensibility.")

    roadmap_steps = [
        ("PHASE 1 // DAYS 1 - 30", "Lombardia Manufacturing Pilot", "€ 25M Volume",
         "• Deploy with 5 pilot manufacturing accounting firms in Milan and Brescia.\n• Benchmark 50 live SME equipment loan dossiers.\n• Direct integration with 3 regional cooperative and commercial banks.\n• Metric: 100% formal acceptance rate for FinSight-certified dossiers.",
         EMERALD_SAFE),
        ("PHASE 2 // DAYS 31 - 90", "Multi-Bank Marketplace", "€ 100M Volume",
         "• Expand distribution via regional industrial associations (Confindustria).\n• Onboard 15 commercial banks and digital private credit funds.\n• Launch automated regional green grant matching engine.\n• Deploy Bank Credit Underwriter portal for institutional portfolio monitoring.",
         CYAN_PRIMARY),
        ("PHASE 3 // MONTHS 4 - 12", "SME Treasury & Capital OS", "€ 500M+ Run-Rate",
         "• Expand from loan origination to continuous SME treasury intelligence.\n• Automated quarterly covenant health monitoring & working capital optimization.\n• The definitive capital readiness operating system for European SMEs.\n• Pan-European expansion into DACH and France under EBA-harmonized rules.",
         INDIGO_ACCENT)
    ]

    for idx, (kicker, title, big_stat, body, accent_c) in enumerate(roadmap_steps):
        left = Inches(0.8 + idx * 4.0)
        add_card(s6, left, Inches(2.0), Inches(3.7), Inches(4.8), top_accent=accent_c)
        tb = s6.shapes.add_textbox(left + Inches(0.25), Inches(2.15), Inches(3.2), Inches(4.5))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = 0

        p0 = tf.paragraphs[0]
        p0.text = kicker
        p0.font.size = Pt(8.5)
        p0.font.bold = True
        p0.font.color.rgb = accent_c
        p0.font.name = "Consolas"

        p1 = tf.add_paragraph()
        p1.text = title
        p1.font.size = Pt(17)
        p1.font.bold = True
        p1.font.color.rgb = TEXT_WHITE
        p1.font.name = "Segoe UI"

        p_stat = tf.add_paragraph()
        p_stat.text = big_stat
        p_stat.font.size = Pt(28)
        p_stat.font.bold = True
        p_stat.font.color.rgb = accent_c
        p_stat.font.name = "Consolas"
        p_stat.space_after = Pt(10)

        for line in body.split("\n"):
            p = tf.add_paragraph()
            p.text = line
            p.font.size = Pt(10.5)
            p.font.color.rgb = TEXT_MUTED
            p.font.name = "Segoe UI"
            p.space_after = Pt(5)

    add_footer_telemetry(s6)

    # Save to both target file paths
    output_path = os.path.join(os.getcwd(), "presentation", "FinSight_AI_Pitch_Deck.pptx")
    alt_path = os.path.join(os.getcwd(), "presentation", "FinSight_AI_Pitch_Deck_Enterprise.pptx")
    
    saved_paths = []
    for path in [output_path, alt_path]:
        try:
            prs.save(path)
            saved_paths.append(path)
            print(f"Presentation saved successfully at: {path}")
        except PermissionError:
            print(f"File locked: {path}")
    
    return saved_paths

if __name__ == "__main__":
    build_pitch_deck()
