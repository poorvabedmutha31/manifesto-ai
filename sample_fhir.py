"""
Sample FHIR R4 patient data — simulates what you'd pull from an EHR.
In production, this comes from the hospital's FHIR endpoint.
"""

SAMPLE_PATIENTS = {
    "patient_001": {
        "resourceType": "Bundle",
        "patient": {
            "resourceType": "Patient",
            "id": "patient-001",
            "name": [{"family": "Martinez", "given": ["Roberto", "J"]}],
            "gender": "male",
            "birthDate": "1962-03-15",
            "contact": [
                {
                    "relationship": [{"text": "Wife"}],
                    "name": {"family": "Martinez", "given": ["Sarah"]},
                    "telecom": [{"system": "phone", "value": "(555) 234-5678"}],
                }
            ],
        },
        "conditions": [
            {
                "resourceType": "Condition",
                "code": {"coding": [{"system": "http://hl7.org/fhir/sid/icd-10-cm", "code": "K21.0", "display": "GERD with esophagitis"}]},
                "clinicalStatus": {"coding": [{"code": "active"}]},
            },
            {
                "resourceType": "Condition",
                "code": {"coding": [{"system": "http://hl7.org/fhir/sid/icd-10-cm", "code": "Z95.5", "display": "Presence of coronary angioplasty implant and graft"}]},
                "clinicalStatus": {"coding": [{"code": "active"}]},
            },
            {
                "resourceType": "Condition",
                "code": {"coding": [{"system": "http://hl7.org/fhir/sid/icd-10-cm", "code": "G47.33", "display": "Obstructive sleep apnea"}]},
                "clinicalStatus": {"coding": [{"code": "active"}]},
            },
            {
                "resourceType": "Condition",
                "code": {"coding": [{"system": "http://hl7.org/fhir/sid/icd-10-cm", "code": "I25.10", "display": "Atherosclerotic heart disease"}]},
                "clinicalStatus": {"coding": [{"code": "active"}]},
            },
        ],
        "medications": [
            {
                "resourceType": "MedicationStatement",
                "medicationCodeableConcept": {
                    "coding": [{"system": "http://www.nlm.nih.gov/research/umls/rxnorm", "code": "32968", "display": "clopidogrel"}],
                    "text": "Plavix 75mg daily",
                },
                "dosage": [{"text": "75mg once daily", "route": {"text": "oral"}}],
                "status": "active",
            },
            {
                "resourceType": "MedicationStatement",
                "medicationCodeableConcept": {
                    "coding": [{"system": "http://www.nlm.nih.gov/research/umls/rxnorm", "code": "6918", "display": "metoprolol"}],
                    "text": "Metoprolol Succinate 50mg daily",
                },
                "dosage": [{"text": "50mg once daily", "route": {"text": "oral"}}],
                "status": "active",
            },
            {
                "resourceType": "MedicationStatement",
                "medicationCodeableConcept": {
                    "coding": [{"system": "http://www.nlm.nih.gov/research/umls/rxnorm", "code": "7646", "display": "omeprazole"}],
                    "text": "Omeprazole 40mg daily",
                },
                "dosage": [{"text": "40mg once daily before breakfast", "route": {"text": "oral"}}],
                "status": "active",
            },
        ],
        "allergies": [
            {
                "resourceType": "AllergyIntolerance",
                "clinicalStatus": {"coding": [{"code": "active"}]},
                "type": "allergy",
                "category": ["medication"],
                "criticality": "low",
                "code": {"coding": [{"display": "Penicillin"}], "text": "Penicillin"},
                "reaction": [{"manifestation": [{"text": "Rash"}], "severity": "mild"}],
            }
        ],
        "procedures_scheduled": [
            {
                "resourceType": "ServiceRequest",
                "code": {"coding": [{"system": "http://www.ama-assn.org/go/cpt", "code": "43239", "display": "EGD with biopsy"}]},
                "scheduledDateTime": "2026-06-05T08:30:00",
                "performer": [{"display": "Dr. Emily Chen, MD — Gastroenterology"}],
                "locationReference": {"display": "Endoscopy Suite 3"},
            }
        ],
        "vitals_recent": {
            "blood_pressure": "138/82",
            "heart_rate": 72,
            "weight_kg": 89,
            "height_cm": 175,
            "bmi": 29.1,
            "o2_sat": 96,
        },
        "labs_recent": {
            "hemoglobin": {"value": 13.8, "unit": "g/dL", "reference": "13.5-17.5"},
            "platelet_count": {"value": 245, "unit": "x10^3/uL", "reference": "150-400"},
            "inr": {"value": 1.1, "unit": "", "reference": "0.8-1.2"},
            "creatinine": {"value": 1.0, "unit": "mg/dL", "reference": "0.7-1.3"},
        },
    },
    "patient_002": {
        "resourceType": "Bundle",
        "patient": {
            "resourceType": "Patient",
            "id": "patient-002",
            "name": [{"family": "Thompson", "given": ["Margaret", "A"]}],
            "gender": "female",
            "birthDate": "1955-11-22",
            "contact": [
                {
                    "relationship": [{"text": "Daughter"}],
                    "name": {"family": "Thompson", "given": ["Jessica"]},
                    "telecom": [{"system": "phone", "value": "(555) 876-5432"}],
                }
            ],
        },
        "conditions": [
            {
                "resourceType": "Condition",
                "code": {"coding": [{"system": "http://hl7.org/fhir/sid/icd-10-cm", "code": "M17.11", "display": "Primary osteoarthritis, right knee"}]},
                "clinicalStatus": {"coding": [{"code": "active"}]},
            },
            {
                "resourceType": "Condition",
                "code": {"coding": [{"system": "http://hl7.org/fhir/sid/icd-10-cm", "code": "E11.9", "display": "Type 2 diabetes mellitus"}]},
                "clinicalStatus": {"coding": [{"code": "active"}]},
            },
            {
                "resourceType": "Condition",
                "code": {"coding": [{"system": "http://hl7.org/fhir/sid/icd-10-cm", "code": "I10", "display": "Essential hypertension"}]},
                "clinicalStatus": {"coding": [{"code": "active"}]},
            },
        ],
        "medications": [
            {
                "resourceType": "MedicationStatement",
                "medicationCodeableConcept": {
                    "coding": [{"system": "http://www.nlm.nih.gov/research/umls/rxnorm", "code": "855332", "display": "warfarin"}],
                    "text": "Warfarin 5mg daily",
                },
                "dosage": [{"text": "5mg once daily", "route": {"text": "oral"}}],
                "status": "active",
            },
            {
                "resourceType": "MedicationStatement",
                "medicationCodeableConcept": {
                    "coding": [{"system": "http://www.nlm.nih.gov/research/umls/rxnorm", "code": "6809", "display": "metformin"}],
                    "text": "Metformin 1000mg twice daily",
                },
                "dosage": [{"text": "1000mg twice daily", "route": {"text": "oral"}}],
                "status": "active",
            },
            {
                "resourceType": "MedicationStatement",
                "medicationCodeableConcept": {
                    "coding": [{"system": "http://www.nlm.nih.gov/research/umls/rxnorm", "code": "29046", "display": "lisinopril"}],
                    "text": "Lisinopril 20mg daily",
                },
                "dosage": [{"text": "20mg once daily", "route": {"text": "oral"}}],
                "status": "active",
            },
        ],
        "allergies": [
            {
                "resourceType": "AllergyIntolerance",
                "clinicalStatus": {"coding": [{"code": "active"}]},
                "type": "allergy",
                "category": ["medication"],
                "criticality": "high",
                "code": {"coding": [{"display": "Sulfonamide"}], "text": "Sulfonamide antibiotics"},
                "reaction": [{"manifestation": [{"text": "Anaphylaxis"}], "severity": "severe"}],
            },
            {
                "resourceType": "AllergyIntolerance",
                "clinicalStatus": {"coding": [{"code": "active"}]},
                "type": "intolerance",
                "category": ["food"],
                "criticality": "low",
                "code": {"coding": [{"display": "Latex"}], "text": "Latex"},
                "reaction": [{"manifestation": [{"text": "Contact dermatitis"}], "severity": "mild"}],
            },
        ],
        "procedures_scheduled": [
            {
                "resourceType": "ServiceRequest",
                "code": {"coding": [{"system": "http://www.ama-assn.org/go/cpt", "code": "27447", "display": "Total knee arthroplasty"}]},
                "scheduledDateTime": "2026-06-12T07:00:00",
                "performer": [{"display": "Dr. James Wright, MD — Orthopedic Surgery"}],
                "locationReference": {"display": "OR Suite 7"},
            }
        ],
        "vitals_recent": {
            "blood_pressure": "148/88",
            "heart_rate": 78,
            "weight_kg": 95,
            "height_cm": 163,
            "bmi": 35.7,
            "o2_sat": 95,
        },
        "labs_recent": {
            "hemoglobin": {"value": 12.1, "unit": "g/dL", "reference": "12.0-16.0"},
            "platelet_count": {"value": 198, "unit": "x10^3/uL", "reference": "150-400"},
            "inr": {"value": 2.3, "unit": "", "reference": "0.8-1.2"},
            "creatinine": {"value": 1.2, "unit": "mg/dL", "reference": "0.6-1.1"},
            "hba1c": {"value": 7.8, "unit": "%", "reference": "<7.0"},
            "glucose_fasting": {"value": 156, "unit": "mg/dL", "reference": "70-100"},
        },
    },
}


def parse_fhir_bundle(bundle):
    """Convert FHIR bundle into our internal patient format."""
    patient = bundle["patient"]
    name_parts = patient["name"][0]
    full_name = f"{' '.join(name_parts.get('given', []))} {name_parts.get('family', '')}"

    birth_year = int(patient["birthDate"].split("-")[0])
    age = 2026 - birth_year

    contact = None
    if patient.get("contact"):
        c = patient["contact"][0]
        contact = {
            "name": " ".join(c["name"].get("given", [])) + " " + c["name"].get("family", ""),
            "relation": c["relationship"][0]["text"],
            "phone": c["telecom"][0]["value"] if c.get("telecom") else "",
        }

    conditions = []
    icd_codes = []
    for cond in bundle.get("conditions", []):
        coding = cond["code"]["coding"][0]
        conditions.append(coding["display"])
        icd_codes.append(f"{coding['code']} ({coding['display']})")

    medications = []
    med_names = []
    for med in bundle.get("medications", []):
        mc = med["medicationCodeableConcept"]
        medications.append({
            "name": mc["text"],
            "generic": mc["coding"][0]["display"],
            "rxcui": mc["coding"][0]["code"],
            "dosage": med["dosage"][0]["text"] if med.get("dosage") else "",
            "status": med.get("status", "active"),
        })
        med_names.append(mc["coding"][0]["display"])

    allergies = []
    for allergy in bundle.get("allergies", []):
        allergies.append({
            "substance": allergy["code"]["text"],
            "reaction": allergy["reaction"][0]["manifestation"][0]["text"] if allergy.get("reaction") else "Unknown",
            "severity": allergy["reaction"][0].get("severity", "unknown") if allergy.get("reaction") else "unknown",
            "criticality": allergy.get("criticality", "unknown"),
        })

    scheduled = None
    if bundle.get("procedures_scheduled"):
        sched = bundle["procedures_scheduled"][0]
        scheduled = {
            "cpt_code": sched["code"]["coding"][0]["code"],
            "name": sched["code"]["coding"][0]["display"],
            "datetime": sched.get("scheduledDateTime", ""),
            "performer": sched["performer"][0]["display"] if sched.get("performer") else "",
            "location": sched.get("locationReference", {}).get("display", ""),
        }

    return {
        "full_name": full_name.strip(),
        "age": age,
        "gender": patient.get("gender", ""),
        "contact": contact,
        "conditions": conditions,
        "icd_codes": icd_codes,
        "medications": medications,
        "med_names": med_names,
        "allergies": allergies,
        "scheduled_procedure": scheduled,
        "vitals": bundle.get("vitals_recent", {}),
        "labs": bundle.get("labs_recent", {}),
    }
