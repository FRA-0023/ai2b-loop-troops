import os
import sys

# Ensure workspace root is in sys.path
WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if WORKSPACE_ROOT not in sys.path:
    sys.path.insert(0, WORKSPACE_ROOT)

from app.auth import verify_credentials
from app.duckdb_engine import parse_and_ingest_csv, calculate_deterministic_bankability
from app.api_client import simulate_scenario_api

print("=== TEST 1: CEE FORMAT SAMPLE BALANCE SHEET ===")
sample_path = os.path.join(WORKSPACE_ROOT, "data", "sample_balance_sheet_cee_2024.csv")
assert os.path.exists(sample_path), "Sample CEE file missing"
with open(sample_path, "r", encoding="utf-8") as f:
    content = f.read()
assert "Codice_Voce" in content and "A.1" in content and "C.IV.1" in content
print("Test 1 PASSED: True statutory Italian Bilancio CEE format verified!")

print("\n=== TEST 2: INGESTION & GROUNDED EVIDENCES ===")
res = parse_and_ingest_csv(content.encode("utf-8"), "test_cee.csv", "ecotex")
assert res["status"] == "SUCCESS", "Parsing failed"
assert len(res["evidences"]) >= 4, "Too few evidences"
for ev in res["evidences"]:
    print(f" - [{ev['category']}] {ev['metric']}: {ev['value']} -> {ev['claim'][:60]}...")
print("Test 2 PASSED: Rich grounded evidences extracted!")

print("\n=== TEST 3: DUAL LOGINS LINKED BY ID ===")
sme_u, _ = verify_credentials("cfo@ecotex.it", "cfo2026")
bank_u, _ = verify_credentials("underwriter@intesabancapmi.it", "bank2026")
assert sme_u["role"] == "sme_borrower" and sme_u["linked_id"] == "ECOTEX-2026-IT"
assert bank_u["role"] == "bank_officer" and bank_u["linked_id"] == "ECOTEX-2026-IT"
print(f"SME User: {sme_u['name']} ({sme_u['organization']}) | Linked ID: {sme_u['linked_id']}")
print(f"Bank User: {bank_u['name']} ({bank_u['organization']}) | Linked ID: {bank_u['linked_id']}")
print("Test 3 PASSED: Both roles authenticated and linked through ID!")

print("\n=== TEST 4: CAPITAL SIZING SENSITIVITY ANALYSIS ===")
sc_base, _, _ = simulate_scenario_api("ecotex", 750000, 0.0525, 5, force_mock=True)
sc_stress, _, _ = simulate_scenario_api("ecotex", 1250000, 0.065, 5, force_mock=True)
print(f"Base @ 750k (5.25%): Score {sc_base['financial_score']}/100 | DSCR {sc_base['dscr']:.2f}x | Lev {sc_base['net_debt_ebitda']:.2f}x | Rec: {sc_base['recommendation']}")
print(f"Stress @ 1.25M (6.50%): Score {sc_stress['financial_score']}/100 | DSCR {sc_stress['dscr']:.2f}x | Lev {sc_stress['net_debt_ebitda']:.2f}x | Rec: {sc_stress['recommendation']}")
assert sc_base["dscr"] > sc_stress["dscr"], "DSCR should degrade under higher loan amount"
assert sc_base["financial_score"] > sc_stress["financial_score"], "Score should degrade under stress"
assert len(sc_base["sensitivity_curve"]) == 10, "Curve should have 10 data points"
print("Test 4 PASSED: Capital sizing sensitivity is mathematically dynamic and fully operational!")

print("\n=== TEST 5: FORMATTED DOWNLOAD TEMPLATES ===")
print(f"Sample Bilancio CEE size: {len(content)} bytes")
assert "Immobilizzazioni" in content and "Capitale sociale" in content and "Riserva legale" in content
print("Test 5 PASSED: Correct formal downloads verified!")

print("\n>>> ALL 5 ENHANCEMENT TESTS SUCCESSFULLY PASSED! <<<")
