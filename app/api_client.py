"""
FinSight AI - Backend Integration Client & Fallback Protocol
============================================================
Handles HTTP communication between the Streamlit UI and the FastAPI backend.

INSTRUCTIONS FOR TEAMMATE B (Backend / AI Engine):
--------------------------------------------------
1. Your FastAPI server should run at `http://localhost:8000` (or configured URL).
2. Endpoint: `POST /evaluate`
3. Request Body format:
   {
       "query": "Assess a €750k sustainability-linked equipment loan for EcoTex Milano...",
       "loan_amount": 750000
   }
4. Response Body format: Must match the JSON schema in `app/mock_data.py` (and Section 15 of PROJECT_2.md).
5. If your backend is offline, under development, or returns an error, this client
   AUTOMATICALLY engages the deterministic fallback to prevent UI crashes.
"""

import requests
from typing import Dict, Any, Tuple
from app.mock_data import get_base_demo_payload, calculate_scenario


DEFAULT_BACKEND_URL = "http://localhost:8000"


def evaluate_application(
    query: str,
    loan_amount: int = 750000,
    backend_url: str = DEFAULT_BACKEND_URL,
    force_mock: bool = False,
    timeout_seconds: float = 4.0
) -> Tuple[Dict[str, Any], str, str]:
    """
    Evaluates an SME financing application.
    
    Returns:
        (payload: Dict[str, Any], mode: str, status_message: str)
        - mode: "LIVE_API" or "DETERMINISTIC_FALLBACK"
        - status_message: Informative status string for credit officers/engineers.
    """
    if force_mock:
        payload = get_base_demo_payload()
        if loan_amount != 750000:
            scenario_res = calculate_scenario(payload, loan_amount)
            payload["scenario"] = scenario_res
        return payload, "DETERMINISTIC_FALLBACK", "Operating in safe deterministic fallback mode (Zero external dependency)."

    target_endpoint = f"{backend_url.rstrip('/')}/evaluate"
    request_data = {
        "query": query,
        "loan_amount": loan_amount
    }

    try:
        response = requests.post(
            target_endpoint,
            json=request_data,
            headers={"Content-Type": "application/json"},
            timeout=timeout_seconds
        )
        
        if response.status_code == 200:
            data = response.json()
            # Ensure scenario key exists
            if "scenario" not in data:
                data["scenario"] = calculate_scenario(data, 1000000)
            return data, "LIVE_API", f"Successfully evaluated via FastAPI backend ({target_endpoint})."
        else:
            # Backend returned 4xx or 5xx (Section 21 Error Handling)
            fallback = get_base_demo_payload()
            return (
                fallback,
                "DETERMINISTIC_FALLBACK",
                f"Backend returned HTTP {response.status_code}. Seamlessly engaged deterministic fallback."
            )

    except requests.exceptions.RequestException as exc:
        # Connection refused, timeout, or DNS failure
        fallback = get_base_demo_payload()
        return (
            fallback,
            "DETERMINISTIC_FALLBACK",
            f"Backend unreachable at {target_endpoint} ({type(exc).__name__}). Engaged deterministic fallback."
        )
