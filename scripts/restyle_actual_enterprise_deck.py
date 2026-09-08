"""
FinSight AI - Restyle Actual Enterprise Pitch Deck
===================================================
Reads the ACTUAL 'presentation/FinSight_AI_Pitch_Deck_Enterprise.pptx' (7 slides,
containing user's exact copy, photos of Francesco, Osama, Pallab, and Immagine 32),
and generates a NEW file 'presentation/FinSight_AI_Pitch_Deck_Frontier.pptx' without
modifying the source file.

Upgrades:
- Deep obsidian canvas (#06090E) with ambient radial back-glows
- Segoe UI for editorial typography + Consolas for tabular numbers and badges
- Linear/Stripe top-accent glow blades on all cards
- Neon circular badges for step numbers (01, 02, 03, 04)
- High-contrast visual hierarchy: 30pt-44pt Consolas numbers
- Sleek picture frames and role badges for team members on Slide 7
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN

def restyle_presentation():
    src_path = os.path.join("presentation", "FinSight_AI_Pitch_Deck_Enterprise.pptx")
    out_path = os.path.join("presentation", "FinSight_AI_Pitch_Deck_Frontier.pptx")
    
    prs = Presentation(src_path)
    print(f"Loaded source presentation with {len(prs.slides)} slides.")

    # High-Contrast Tier-1 Palette
    BG_OBSIDIAN = RGBColor(6, 9, 14)          # #06090E
    GLOW_CYAN = RGBColor(12, 28, 48)          # #0C1C30
    GLOW_EMERALD = RGBColor(9, 32, 28)        # #09201C
    GLOW_ROSE = RGBColor(35, 12, 20)          # #230C14

    CARD_BG = RGBColor(13, 19, 32)            # #0D1320
    CARD_BG_ALT = RGBColor(17, 24, 39)        # #111827
    CARD_BORDER = RGBColor(30, 41, 59)        # #1E293B
    CARD_BORDER_BRIGHT = RGBColor(51, 65, 85) # #334155

    CYAN_NEON = RGBColor(56, 189, 248)        # #38BDF8
    CYAN_DEEP = RGBColor(2, 132, 199)         # #0284C7
    EMERALD_NEON = RGBColor(52, 211, 153)     # #34D399
    EMERALD_DEEP = RGBColor(16, 185, 129)     # #10B981
    AMBER_WARN = RGBColor(245, 158, 11)       # #F59E0B
    AMBER_LIGHT = RGBColor(251, 191, 36)      # #FBBF24
    ROSE_DANGER = RGBColor(244, 63, 94)       # #F43F5E
    ROSE_LIGHT = RGBColor(251, 113, 133)      # #FB7185
    INDIGO_TECH = RGBColor(99, 102, 241)      # #6366F1
    PURPLE_REG = RGBColor(168, 85, 247)       # #A855F7

    TEXT_WHITE = RGBColor(255, 255, 255)      # #FFFFFF
    TEXT_LIGHT = RGBColor(241, 245, 249)      # #F1F5F9
    TEXT_MUTED = RGBColor(148, 163, 184)      # #94A3B8
    TEXT_DIM = RGBColor(100, 116, 139)        # #64748B

    # Slide Glow Configurations
    slide_glows = {
        0: (GLOW_CYAN, Inches(8.5), Inches(-1.5), Inches(6.5), Inches(6.0)),
        1: (GLOW_ROSE, Inches(8.5), Inches(-1.5), Inches(6.5), Inches(6.0)),
        2: (GLOW_CYAN, Inches(8.5), Inches(-1.5), Inches(6.5), Inches(6.0)),
        3: (GLOW_EMERALD, Inches(8.5), Inches(-1.5), Inches(6.5), Inches(6.0)),
        4: (GLOW_CYAN, Inches(8.5), Inches(-1.5), Inches(6.5), Inches(6.0)),
        5: (GLOW_EMERALD, Inches(8.5), Inches(-1.5), Inches(6.5), Inches(6.0)),
        6: (GLOW_CYAN, Inches(8.5), Inches(-1.5), Inches(6.5), Inches(6.0)),
    }

    # Iterate through each slide and enhance
    for s_idx, slide in enumerate(prs.slides):
        print(f"Enhancing Slide {s_idx + 1}...")

        # 1. Ensure solid background on the slide
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = BG_OBSIDIAN

        # 2. Add top ambient glow circle behind content (sent to back)
        g_col, gx, gy, gw, gh = slide_glows.get(s_idx, (GLOW_CYAN, Inches(8.5), Inches(-1.5), Inches(6.5), Inches(6.0)))
        glow = slide.shapes.add_shape(MSO_SHAPE.OVAL, gx, gy, gw, gh)
        glow.fill.solid()
        glow.fill.fore_color.rgb = g_col
        glow.line.fill.background()

        # Collect shapes that are cards (Rounded Rectangles) to add top accent glow blades
        card_shapes = []

        # 3. Restyle existing shapes on the slide
        for shape in slide.shapes:
            # Check for existing background ovals that were in the original template and restyle them
            if shape.name.startswith("Oval") and (shape.width.inches > 5.0 or shape.height.inches > 5.0):
                shape.fill.solid()
                shape.fill.fore_color.rgb = g_col
                shape.line.fill.background()
                continue

            # Restyle cards (Rounded Rectangles)
            if shape.shape_type == MSO_SHAPE.ROUNDED_RECTANGLE or "Rounded Rectangle" in shape.name:
                shape.fill.solid()
                shape.fill.fore_color.rgb = CARD_BG
                shape.line.color.rgb = CARD_BORDER
                shape.line.width = Pt(1.2)
                card_shapes.append(shape)

            # Restyle step circular nodes (small ovals like 01, 02, 03)
            elif shape.name.startswith("Oval") and shape.width.inches < 1.0 and shape.has_text_frame:
                shape.fill.solid()
                shape.fill.fore_color.rgb = RGBColor(15, 23, 42)
                shape.line.color.rgb = CYAN_NEON
                shape.line.width = Pt(1.5)
                for p in shape.text_frame.paragraphs:
                    p.alignment = PP_ALIGN.CENTER
                    for r in p.runs:
                        r.font.name = "Consolas"
                        r.font.bold = True
                        r.font.color.rgb = CYAN_NEON

            # Restyle chevrons and connectors
            elif "Chevron" in shape.name or shape.shape_type == MSO_SHAPE.CHEVRON:
                shape.fill.solid()
                shape.fill.fore_color.rgb = RGBColor(30, 41, 59)
                shape.line.color.rgb = CYAN_NEON
                shape.line.width = Pt(1.0)
            elif "Connector" in shape.name or shape.shape_type == 9: # Line
                shape.line.color.rgb = CARD_BORDER_BRIGHT
                shape.line.width = Pt(1.0)

            # Restyle Pictures (Team photos and Slide 4 Chart)
            elif shape.shape_type == 13: # Picture
                # On Slide 7 (Team): add subtle backing/border if needed
                shape.line.color.rgb = CYAN_DEEP
                shape.line.width = Pt(1.5)

            # Restyle Text
            if shape.has_text_frame:
                txt = shape.text_frame.text.strip()
                
                # Check for top header / logo: FINSIGHT AI
                if txt == "FINSIGHT AI":
                    for p in shape.text_frame.paragraphs:
                        for r in p.runs:
                            r.font.name = "Consolas"
                            r.font.bold = True
                            r.font.color.rgb = CYAN_NEON
                            r.font.size = Pt(10)

                # Check for page numbers: 02 / 6, 03 / 6, etc.
                elif "/" in txt and ("0" in txt or "6" in txt) and len(txt) <= 7:
                    for p in shape.text_frame.paragraphs:
                        for r in p.runs:
                            r.font.name = "Consolas"
                            r.font.bold = True
                            r.font.color.rgb = TEXT_DIM
                            r.font.size = Pt(9.5)

                # Check for Kicker / Tag (e.g. PROBLEM & MARKET FAILURE, ARCHITECTURE, etc.)
                elif txt in [
                    "AUTONOMOUS SME CREDIT READINESS & CAPITAL SIZING COPILOT",
                    "PROBLEM & MARKET FAILURE",
                    "ARCHITECTURE & DATA SOVEREIGNTY",
                    "LIVE PROOF & TIPPING POINT — ECOTEX MILANO",
                    "LIVE PROOF & TIPPING POINT – ECOTEX MILANO",
                    "BUSINESS MODEL",
                    "EXECUTION ROADMAP & VISION",
                    "US"
                ]:
                    for p in shape.text_frame.paragraphs:
                        for r in p.runs:
                            r.font.name = "Consolas"
                            r.font.bold = True
                            r.font.color.rgb = CYAN_NEON
                            r.font.size = Pt(9.5)

                # Check for Main Slide Title
                elif any(txt.startswith(prefix) for prefix in [
                    "FinSight AI: Pre-Underwriting",
                    "Why 40% of Creditworthy",
                    "The 4-Stage Deterministic",
                    "Optimizing Borrowing",
                    "Distribution Through",
                    "The 12-Month Path",
                    "Thank you"
                ]):
                    for p in shape.text_frame.paragraphs:
                        for r in p.runs:
                            r.font.name = "Segoe UI"
                            r.font.bold = True
                            r.font.color.rgb = TEXT_WHITE
                            if txt.startswith("FinSight AI:"):
                                r.font.size = Pt(38)
                            elif txt == "Thank you":
                                r.font.size = Pt(56)
                            else:
                                r.font.size = Pt(26)

                # Check for Hero Metric Numbers (Consolas, bold, glowing neon)
                elif txt in [
                    "40%", "3 WEEKS", "€10K+", "10K+",
                    "95 / 100", "1.82%", "APPROVE",
                    "0.5–1.0%", "0.5-1.0%", "120,000", ">20x",
                    "MONTH 1", "MONTH 3", "MONTH 12"
                ]:
                    # Determine accent color
                    if txt in ["40%", "€10K+", "10K+"]:
                        num_col = ROSE_LIGHT
                    elif txt in ["95 / 100", "APPROVE", "120,000"]:
                        num_col = EMERALD_NEON
                    elif txt in ["1.82%", "3 WEEKS"]:
                        num_col = AMBER_LIGHT
                    else:
                        num_col = CYAN_NEON

                    for p in shape.text_frame.paragraphs:
                        for r in p.runs:
                            r.font.name = "Consolas"
                            r.font.bold = True
                            r.font.color.rgb = num_col
                            r.font.size = Pt(32) if len(txt) > 6 else Pt(38)

                # Check for Card Titles / Section Headings
                elif txt in [
                    "THE INFORMATION VOID", "THE 3-WEEK BLACK BOX", "THE ESG PENALTY",
                    "DUCKDB LAKEHOUSE", "CENTRAL BANK FUSION", "DETERMINISTIC MATH", "GROUNDED RAG & SEAL",
                    "FINANCIAL HEALTH", "ESG ALIGNMENT", "MILAN PROVINCIAL NPL", "CERTIFIED OUTCOME",
                    "OPTIMAL BASE — €750K", "OPTIMAL BASE – €750K", "STRESS TEST — €1.0M+", "STRESS TEST – €1.0M+",
                    "MONETIZATION", "CHANNEL FLYWHEEL", "UNIT ECONOMICS",
                    "LOMBARDIA PILOT", "MULTI-LENDER MARKETPLACE", "CONTINUOUS TREASURY OS",
                    "IN-MEMORY DUCKDB 1.0", "BANCA D'ITALIA NPL FUSE", "EBA GL/2020/06 CERTIFIED",
                    "Colombini Francesco", "Osama Haider", "Pallab Mondal", "Data Science", "AI4ST"
                ]:
                    for p in shape.text_frame.paragraphs:
                        for r in p.runs:
                            if txt in ["Data Science", "AI4ST"]:
                                r.font.name = "Consolas"
                                r.font.bold = True
                                r.font.color.rgb = CYAN_NEON
                                r.font.size = Pt(11)
                            elif txt in ["Colombini Francesco", "Osama Haider", "Pallab Mondal"]:
                                r.font.name = "Segoe UI"
                                r.font.bold = True
                                r.font.color.rgb = TEXT_WHITE
                                r.font.size = Pt(16)
                            elif "OPTIMAL" in txt:
                                r.font.name = "Consolas"
                                r.font.bold = True
                                r.font.color.rgb = EMERALD_NEON
                                r.font.size = Pt(12)
                            elif "STRESS" in txt:
                                r.font.name = "Consolas"
                                r.font.bold = True
                                r.font.color.rgb = AMBER_LIGHT
                                r.font.size = Pt(12)
                            else:
                                r.font.name = "Segoe UI"
                                r.font.bold = True
                                r.font.color.rgb = TEXT_WHITE
                                r.font.size = Pt(13)

                # Check for Footnotes / URLs
                elif "http" in txt or txt.startswith("*"):
                    for p in shape.text_frame.paragraphs:
                        for r in p.runs:
                            r.font.name = "Consolas"
                            r.font.color.rgb = TEXT_DIM
                            r.font.size = Pt(8)

                # Standard Body text
                else:
                    for p in shape.text_frame.paragraphs:
                        for r in p.runs:
                            r.font.name = "Segoe UI"
                            r.font.color.rgb = TEXT_MUTED

        # 4. Add Linear/Stripe Top Accent Glow Blades to cards
        slide_accent_map = {
            0: [CYAN_NEON, EMERALD_DEEP, PURPLE_REG],
            1: [ROSE_DANGER, AMBER_WARN, ROSE_LIGHT],
            2: [CYAN_NEON, INDIGO_TECH, EMERALD_DEEP, PURPLE_REG],
            3: [CYAN_NEON, EMERALD_NEON, AMBER_WARN, EMERALD_DEEP, EMERALD_NEON, AMBER_WARN],
            4: [CYAN_NEON, EMERALD_NEON, PURPLE_REG],
            5: [EMERALD_NEON, CYAN_NEON, INDIGO_TECH],
            6: [CYAN_NEON, EMERALD_NEON, PURPLE_REG]
        }
        accents = slide_accent_map.get(s_idx, [CYAN_NEON, EMERALD_NEON, PURPLE_REG])

        for c_i, card in enumerate(card_shapes):
            accent_col = accents[c_i % len(accents)]
            blade = slide.shapes.add_shape(
                MSO_SHAPE.RECTANGLE,
                card.left + Inches(0.08),
                card.top + Inches(0.02),
                card.width - Inches(0.16),
                Inches(0.04)
            )
            blade.fill.solid()
            blade.fill.fore_color.rgb = accent_col
            blade.line.fill.background()

        # 5. Add elegant telemetry footer bar on slides 1-6
        if s_idx < 6:
            bar = slide.shapes.add_textbox(Inches(0.8), Inches(7.15), Inches(11.7), Inches(0.30))
            tf = bar.text_frame
            tf.margin_left = tf.margin_top = 0
            p = tf.paragraphs[0]
            p.text = "DUCKDB 1.0 IN-MEMORY OLAP  |  APPLICATION ID: ECOTEX-2026-IT  |  EBA/GL/2020/06 COMPLIANT  |  TUB ART. 128-SEXIES SEAL"
            p.font.size = Pt(8)
            p.font.bold = True
            p.font.color.rgb = RGBColor(70, 85, 105)
            p.font.name = "Consolas"

    # Save to the dedicated new file without touching the source file
    prs.save(out_path)
    print(f"Successfully saved restyled presentation to: {out_path}")
    return out_path

if __name__ == "__main__":
    restyle_presentation()
