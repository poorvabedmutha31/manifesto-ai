"""
Patient data parser — extracts structured information from unstructured
clinical notes, AVS text, and scribed data.
"""
import re
from typing import Optional


BLOOD_THINNERS = {
    "plavix": "clopidogrel",
    "clopidogrel": "clopidogrel",
    "warfarin": "warfarin",
    "coumadin": "warfarin",
    "eliquis": "apixaban",
    "apixaban": "apixaban",
    "xarelto": "rivaroxaban",
    "rivaroxaban": "rivaroxaban",
    "pradaxa": "dabigatran",
    "dabigatran": "dabigatran",
    "heparin": "heparin",
    "lovenox": "enoxaparin",
    "enoxaparin": "enoxaparin",
    "aspirin": "aspirin",
    "brilinta": "ticagrelor",
    "ticagrelor": "ticagrelor",
    "effient": "prasugrel",
    "prasugrel": "prasugrel",
}

NSAIDS = {
    "ibuprofen": "ibuprofen",
    "advil": "ibuprofen",
    "motrin": "ibuprofen",
    "naproxen": "naproxen",
    "aleve": "naproxen",
    "celecoxib": "celecoxib",
    "celebrex": "celecoxib",
    "meloxicam": "meloxicam",
    "diclofenac": "diclofenac",
    "indomethacin": "indomethacin",
}

RISK_KEYWORDS = {
    "bleeding_risk": ["blood thinner", "anticoagulant", "antiplatelet", "bleeding disorder", "hemophilia", "low platelet"],
    "cardiac_risk": ["stent", "heart attack", "mi ", "myocardial infarction", "cabg", "bypass", "heart failure", "chf", "afib", "atrial fibrillation", "pacemaker", "defibrillator"],
    "sedation_risk": ["sleep apnea", "cpap", "bipap", "obesity", "copd", "emphysema", "asthma"],
    "infection_risk": ["diabetes", "immunosuppressed", "transplant", "chemotherapy", "hiv", "aids", "steroid"],
    "vte_risk": ["dvt", "deep vein thrombosis", "pulmonary embolism", "pe ", "blood clot", "factor v leiden"],
}


def extract_medications(text: str) -> dict:
    """Extract medications found in text, categorized."""
    text_lower = text.lower()
    found_blood_thinners = {}
    found_nsaids = {}
    found_other = []

    for brand, generic in BLOOD_THINNERS.items():
        if brand in text_lower:
            found_blood_thinners[generic] = brand

    for brand, generic in NSAIDS.items():
        if brand in text_lower:
            found_nsaids[generic] = brand

    med_patterns = [
        r"(?:takes?|taking|on|prescribed|using)\s+(?:daily\s+)?(\w+)",
        r"(\w+)\s+(?:\d+\s*mg|\d+\s*mcg)",
    ]
    for pattern in med_patterns:
        matches = re.findall(pattern, text_lower)
        for match in matches:
            if match not in BLOOD_THINNERS and match not in NSAIDS and len(match) > 3:
                found_other.append(match)

    return {
        "blood_thinners": found_blood_thinners,
        "nsaids": found_nsaids,
        "other": list(set(found_other)),
    }


def extract_allergies(text: str) -> list:
    """Extract allergies from clinical text."""
    allergies = []
    patterns = [
        r"(?:allergic to|allergy to|allergies?[:\s]+)([^.;]+)",
        r"(\w+)\s+allergy",
        r"allergy[:\s]+(\w+)",
    ]
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for m in matches:
            cleaned = m.strip().rstrip(",")
            if cleaned and len(cleaned) > 2 and cleaned.lower() not in ["no", "none", "nkda"]:
                allergies.append(cleaned)
    return list(set(allergies))


def extract_risk_factors(text: str) -> dict:
    """Identify risk factor categories present in the text."""
    text_lower = text.lower()
    triggered = {}
    for category, keywords in RISK_KEYWORDS.items():
        found = [kw for kw in keywords if kw in text_lower]
        if found:
            triggered[category] = found
    return triggered


def extract_escort_info(text: str) -> Optional[dict]:
    """Extract driver/escort information."""
    patterns = [
        (r"(?:wife|husband|partner|daughter|son|friend|brother|sister|mother|father),?\s+(\w+),?\s+(?:will\s+)?(?:drive|pick|transport|take)", "after_relation"),
        (r"(\w+)(?:'s)?\s+(?:wife|husband|partner|daughter|son|friend|brother|sister|mother|father)[\w\s,]*(?:will\s+)?(?:drive|pick|transport|take)", "before_relation"),
        (r"(?:drive|pick|transport|take)\s+(?:him|her|patient)\s+home.*?(?:by|with)\s+(\w+)", "after_verb"),
        (r"(?:escort|driver|ride)[:\s]+(\w+)", "labeled"),
    ]
    for pattern, style in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            name = match.group(1)
            if name.lower() in ("patient", "the", "his", "her", "my", "will"):
                continue
            relation_match = re.search(
                r"(wife|husband|partner|daughter|son|friend|brother|sister|mother|father)",
                text, re.IGNORECASE,
            )
            return {
                "name": name.capitalize(),
                "relation": relation_match.group(1) if relation_match else "contact",
            }
    return None


def extract_age(text: str) -> Optional[int]:
    """Extract patient age."""
    match = re.search(r"(?:age[:\s]+|(\d{1,3})\s*(?:year|yr|y/?o))", text, re.IGNORECASE)
    if match and match.group(1):
        age = int(match.group(1))
        if 0 < age < 120:
            return age
    return None


def parse_patient_context(scribe_notes: str, icd_codes=None, age=None) -> dict:
    """Full parse of patient context from clinical notes."""
    medications = extract_medications(scribe_notes)
    allergies = extract_allergies(scribe_notes)
    risk_factors = extract_risk_factors(scribe_notes)
    escort = extract_escort_info(scribe_notes)

    if medications["blood_thinners"]:
        risk_factors.setdefault("bleeding_risk", []).append("antiplatelet/anticoagulant therapy")

    if age and age > 80:
        risk_factors.setdefault("sedation_risk", []).append("advanced age >80")

    conditions = []
    if medications["blood_thinners"]:
        conditions.append("on_blood_thinners")
    conditions.append("sedation_planned")

    active_triggers = []
    if "bleeding_risk" in risk_factors:
        active_triggers.append("bleeding_risk")
    if "cardiac_risk" in risk_factors:
        active_triggers.append("cardiac_risk")
    if "sedation_risk" in risk_factors:
        active_triggers.append("sedation_risk")
    if "infection_risk" in risk_factors:
        active_triggers.append("infection_risk")
    if "vte_risk" in risk_factors:
        active_triggers.append("vte_risk")

    return {
        "age": age,
        "medications": medications,
        "allergies": allergies,
        "risk_factors": risk_factors,
        "escort": escort,
        "conditions": conditions,
        "active_triggers": active_triggers,
        "all_meds_for_lookup": list(medications["blood_thinners"].values()) + list(medications["nsaids"].values()),
    }
