"""
Medical data service — pulls real data from OpenFDA and RxNorm APIs.
No API keys required.
"""
import requests
from typing import Optional


OPENFDA_BASE = "https://api.fda.gov"
RXNAV_BASE = "https://rxnav.nlm.nih.gov/REST"


def search_drug_label(drug_name: str) -> Optional[dict]:
    """Get full prescribing info from openFDA drug labels."""
    try:
        resp = requests.get(
            f"{OPENFDA_BASE}/drug/label.json",
            params={
                "search": f'openfda.generic_name:"{drug_name}"',
                "limit": 1,
            },
            timeout=10,
        )
        if resp.status_code == 200:
            data = resp.json()
            if data.get("results"):
                return data["results"][0]
    except requests.RequestException:
        pass
    return None


def get_drug_warnings(drug_name: str) -> dict:
    """Extract warnings, contraindications, and interactions from FDA label."""
    label = search_drug_label(drug_name)
    if not label:
        return {}

    def first_or_empty(field):
        val = label.get(field, [])
        return val[0] if val else ""

    return {
        "warnings": first_or_empty("warnings"),
        "contraindications": first_or_empty("contraindications"),
        "drug_interactions": first_or_empty("drug_interactions"),
        "precautions": first_or_empty("precautions") or first_or_empty("warnings_and_cautions"),
        "adverse_reactions": first_or_empty("adverse_reactions"),
        "boxed_warning": first_or_empty("boxed_warning"),
        "dosage_and_administration": first_or_empty("dosage_and_administration"),
    }


def get_adverse_events(drug_name: str, limit: int = 10) -> list:
    """Get reported adverse events for a drug from FDA FAERS."""
    try:
        resp = requests.get(
            f"{OPENFDA_BASE}/drug/event.json",
            params={
                "search": f'patient.drug.openfda.generic_name:"{drug_name}"',
                "count": "patient.reaction.reactionmeddrapt.exact",
                "limit": limit,
            },
            timeout=10,
        )
        if resp.status_code == 200:
            data = resp.json()
            return data.get("results", [])
    except requests.RequestException:
        pass
    return []


def get_rxcui(drug_name: str) -> Optional[str]:
    """Get RxNorm concept ID for a drug."""
    try:
        resp = requests.get(
            f"{RXNAV_BASE}/rxcui.json",
            params={"name": drug_name},
            timeout=10,
        )
        if resp.status_code == 200:
            data = resp.json()
            ids = data.get("idGroup", {}).get("rxnormId", [])
            if ids:
                return ids[0]
    except requests.RequestException:
        pass
    return None


def get_drug_properties(rxcui: str) -> Optional[dict]:
    """Get drug properties from RxNorm."""
    try:
        resp = requests.get(
            f"{RXNAV_BASE}/rxcui/{rxcui}/properties.json",
            timeout=10,
        )
        if resp.status_code == 200:
            return resp.json().get("properties")
    except requests.RequestException:
        pass
    return None


def get_drug_classes(rxcui: str) -> list:
    """Get drug classification (e.g., anticoagulant, NSAID)."""
    try:
        resp = requests.get(
            f"{RXNAV_BASE}/rxclass/class/byRxcui.json",
            params={"rxcui": rxcui, "relaSource": "ATC"},
            timeout=10,
        )
        if resp.status_code == 200:
            data = resp.json()
            entries = data.get("rxclassDrugInfoList", {}).get("rxclassDrugInfo", [])
            return [
                {
                    "name": e.get("rxclassMinConceptItem", {}).get("className", ""),
                    "id": e.get("rxclassMinConceptItem", {}).get("classId", ""),
                }
                for e in entries
            ]
    except requests.RequestException:
        pass
    return []


def lookup_drug_full(drug_name: str) -> dict:
    """Complete drug lookup combining RxNorm + OpenFDA."""
    result = {
        "name": drug_name,
        "rxcui": None,
        "properties": None,
        "classes": [],
        "fda_warnings": {},
        "adverse_events": [],
    }

    rxcui = get_rxcui(drug_name)
    if rxcui:
        result["rxcui"] = rxcui
        result["properties"] = get_drug_properties(rxcui)
        result["classes"] = get_drug_classes(rxcui)

    result["fda_warnings"] = get_drug_warnings(drug_name)
    result["adverse_events"] = get_adverse_events(drug_name, limit=8)

    return result
