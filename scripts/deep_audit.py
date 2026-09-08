import os
import sys

# Ensure workspace root is in sys.path
WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if WORKSPACE_ROOT not in sys.path:
    sys.path.insert(0, WORKSPACE_ROOT)

from app.duckdb_engine import (
    get_connection,
    calculate_deterministic_bankability,
    get_all_companies,
    get_table_preview,
    get_lakehouse_stats,
    parse_and_ingest_csv,
    parse_and_ingest_pdf
)
from app.api_client import evaluate_application, simulate_scenario_api, authenticate_api, upload_file_api
from app.pdf_generator import generate_credit_memorandum_pdf
import fitz

def test_all():
    print("=== 1. TESTING ALL 3 COMPANIES IN DUCKDB ===")
    for cid in ["ecotex", "meccanica", "agrobio"]:
        res = calculate_deterministic_bankability(cid, 750000)
        c_name = res["company"]
        dscr = res["dscr"]
        score = res["financial_score"]
        rec = res["recommendation"]
        print(f"Company: {c_name} | DSCR: {dscr} | Score: {score} | Rec: {rec}")
        assert res["dscr"] > 0, f"Invalid DSCR for {cid}"
        assert res["revenue"] > 0, f"Invalid revenue for {cid}"

    print("\n=== 2. TESTING PDF GENERATOR FOR ALL COMPANIES ===")
    for cid in ["ecotex", "meccanica", "agrobio"]:
        metrics = calculate_deterministic_bankability(cid, 500000)
        app_id = f"{cid.upper()}-2026-IT"
        pdf_bytes = generate_credit_memorandum_pdf(metrics, "TESTHASH12345678", app_id)
        assert len(pdf_bytes) > 5000, f"PDF too small for {cid}"
        assert pdf_bytes.startswith(b"%PDF-"), f"Invalid header for {cid}"
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        text = doc[0].get_text()
        assert app_id in text, f"Application ID not found in PDF for {cid}"
        print(f"PDF for {cid} verified! Length: {len(pdf_bytes)} bytes | Pages: {len(doc)}")

    print("\n=== 3. TESTING ALL LAKEHOUSE TABLES ===")
    tables = ["companies", "financial_statements", "bdi_provincial_credit", "lombardia_sectors", "document_chunks"]
    for t in tables:
        df = get_table_preview(t, limit=10)
        assert len(df) > 0, f"Table {t} is empty!"
        print(f"Table {t}: {len(df)} rows retrieved successfully")

    print("\n=== 4. TESTING CSV & PDF INGESTION ===")
    with open("data/sample_balance_sheet_cee_2024.csv", "rb") as f:
        csv_bytes = f.read()
    csv_res = parse_and_ingest_csv(csv_bytes, "sample_balance_sheet_cee_2024.csv", "ecotex")
    assert csv_res["status"] == "SUCCESS", "CSV Ingestion failed"
    print("CSV Ingestion:", csv_res["status"], "| File Hash:", csv_res["file_hash"])

    with open("data/sample_esg_audit_ecotex.pdf", "rb") as f:
        pdf_in_bytes = f.read()
    pdf_res = parse_and_ingest_pdf(pdf_in_bytes, "sample_esg_audit_ecotex.pdf", "ecotex")
    assert pdf_res["status"] == "SUCCESS", "PDF Ingestion failed"
    print("PDF Ingestion:", pdf_res["status"], "| Chunks created:", pdf_res["chunks_created"])

    print("\n=== 5. TESTING SCENARIO SIMULATION BOUNDS ===")
    for amt in [500000, 1000000, 1500000]:
        for rate in [0.035, 0.055, 0.08]:
            for tenor in [3, 5, 10]:
                sim = simulate_scenario_api("ecotex", amt, rate, tenor, force_mock=True)[0]
                assert "dscr" in sim and "financial_score" in sim and "sensitivity_curve" in sim
    print("All 27 simulation combinations passed successfully!")

    print("\n=== 6. TESTING AUTHENTICATION EDGE CASES ===")
    u1, m1, s1 = authenticate_api("cfo@ecotex.it", "cfo2026", "sme_borrower", force_mock=True)
    assert u1 is not None, "SME login failed"
    u2, m2, s2 = authenticate_api("underwriter@intesabancapmi.it", "bank2026", "bank_officer", force_mock=True)
    assert u2 is not None, "Bank login failed"
    u3, m3, s3 = authenticate_api("cfo@ecotex.it", "wrongpwd", "sme_borrower", force_mock=True)
    assert u3 is None, "Should reject wrong password"
    u4, m4, s4 = authenticate_api("cfo@ecotex.it", "cfo2026", "bank_officer", force_mock=True)
    assert u4 is None, "Should reject wrong role"
    print("Authentication security checks passed!")

    print("\n>>> ALL 6 AUDIT DOMAINS PASSED FLAWLESSLY! <<<")

if __name__ == "__main__":
    test_all()
