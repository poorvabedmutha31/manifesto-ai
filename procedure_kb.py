"""
Procedure Knowledge Base — clinical ground truth for common procedures.
This simulates what would come from sources like OpenEvidence, UpToDate, etc.
In production, this would be backed by a clinical knowledge API.

Each procedure includes:
- Steps (ordered)
- Required inventory/equipment
- Required personnel
- Standard risks and contraindications
- Pre-procedure prep
- Post-procedure care
- Common complications
"""

PROCEDURES = {
    "43239": {
        "cpt_code": "43239",
        "name": "Upper GI Endoscopy (EGD) with Biopsy",
        "category": "Gastroenterology",
        "duration_minutes": 30,
        "anesthesia": "Moderate sedation (Propofol or Midazolam/Fentanyl)",
        "steps": [
            "Verify patient identity, consent, and NPO status",
            "Position patient in left lateral decubitus",
            "Administer topical pharyngeal anesthesia",
            "Induce moderate sedation per anesthesia protocol",
            "Insert gastroscope through mouth into esophagus",
            "Advance scope through esophagus, inspecting for abnormalities",
            "Enter stomach, insufflate air, inspect gastric mucosa",
            "Advance through pylorus into duodenum",
            "Perform targeted biopsies of suspicious lesions",
            "Withdraw scope systematically, re-inspecting on the way out",
            "Document findings with images",
            "Label specimens and send to pathology",
        ],
        "required_equipment": [
            {"item": "Gastroscope (adult)", "quantity": 1, "critical": True},
            {"item": "Biopsy forceps (standard)", "quantity": 2, "critical": True},
            {"item": "Bite block/mouth guard", "quantity": 1, "critical": True},
            {"item": "Topical anesthetic spray (Cetacaine/Hurricaine)", "quantity": 1, "critical": False},
            {"item": "Specimen containers with formalin", "quantity": 4, "critical": True},
            {"item": "Suction apparatus", "quantity": 1, "critical": True},
            {"item": "Pulse oximeter", "quantity": 1, "critical": True},
            {"item": "Capnography monitor", "quantity": 1, "critical": True},
            {"item": "Crash cart (in room or immediately adjacent)", "quantity": 1, "critical": True},
            {"item": "IV access supplies", "quantity": 1, "critical": True},
        ],
        "backup_equipment": [
            {"item": "Hemostatic clips (Resolution/QuickClip)", "trigger": "bleeding_risk", "critical": True},
            {"item": "Hot biopsy forceps", "trigger": "bleeding_risk", "critical": True},
            {"item": "Epinephrine injection (1:10000)", "trigger": "bleeding_risk", "critical": True},
            {"item": "Pediatric gastroscope", "trigger": "difficult_anatomy", "critical": False},
        ],
        "required_personnel": [
            {"role": "Gastroenterologist", "required": True, "responsibility": "Performs procedure"},
            {"role": "Anesthesiologist/CRNA", "required": True, "responsibility": "Sedation management"},
            {"role": "Endoscopy Nurse", "required": True, "responsibility": "Assists with instruments, monitors patient"},
            {"role": "Endoscopy Technician", "required": True, "responsibility": "Scope handling, room setup"},
            {"role": "Recovery Nurse", "required": True, "responsibility": "Post-procedure monitoring"},
        ],
        "pre_procedure_prep": [
            {"task": "NPO 8 hours (solids), 2 hours (clear liquids)", "timeframe": "8 hours before", "responsible": "Patient"},
            {"task": "Hold anticoagulants per protocol", "timeframe": "3-7 days before", "responsible": "Ordering physician", "condition": "on_blood_thinners"},
            {"task": "Review and document allergies", "timeframe": "Day before", "responsible": "Pre-op nurse"},
            {"task": "Confirm escort/driver availability", "timeframe": "Day before", "responsible": "Pre-op nurse", "condition": "sedation_planned"},
            {"task": "Verify labs (CBC, PT/INR if on anticoagulants)", "timeframe": "Within 30 days", "responsible": "Ordering physician"},
            {"task": "Obtain informed consent with procedure risks discussed", "timeframe": "Before sedation", "responsible": "Gastroenterologist"},
        ],
        "risks_and_contraindications": [
            {"risk": "Perforation", "incidence": "0.03%", "severity": "Critical"},
            {"risk": "Bleeding (post-biopsy)", "incidence": "0.5-1%", "severity": "High"},
            {"risk": "Aspiration", "incidence": "0.1%", "severity": "High"},
            {"risk": "Adverse sedation reaction", "incidence": "0.5%", "severity": "High"},
            {"risk": "Infection", "incidence": "<0.01%", "severity": "Moderate"},
            {"risk": "Cardiopulmonary event", "incidence": "0.5%", "severity": "Critical"},
        ],
        "contraindications_absolute": [
            "Suspected or known perforation",
            "Hemodynamic instability",
            "Uncooperative patient without sedation option",
            "Inadequate airway protection",
        ],
        "contraindications_relative": [
            "Recent myocardial infarction (<6 weeks)",
            "Severe coagulopathy (INR > 2.5)",
            "Large thoracic aortic aneurysm",
            "Zenker's diverticulum (increased perforation risk)",
        ],
        "post_procedure": [
            {"task": "Monitor in recovery until alert and stable vitals x 30 min", "responsible": "Recovery nurse"},
            {"task": "Check for signs of perforation (pain, fever, tachycardia)", "responsible": "Recovery nurse"},
            {"task": "Provide discharge instructions (no driving 24h, diet advancement)", "responsible": "Discharge nurse"},
            {"task": "Communicate biopsy results within 7-10 business days", "responsible": "Gastroenterologist"},
        ],
        "high_risk_factors": {
            "bleeding_risk": ["anticoagulant use", "antiplatelet therapy", "thrombocytopenia", "coagulopathy", "cirrhosis"],
            "aspiration_risk": ["gastroparesis", "bowel obstruction", "recent meal", "altered consciousness"],
            "perforation_risk": ["cervical osteophytes", "Zenker's diverticulum", "stricture", "prior radiation"],
            "sedation_risk": ["sleep apnea", "obesity BMI>40", "COPD", "advanced age >80"],
        },
    },
    "45378": {
        "cpt_code": "45378",
        "name": "Diagnostic Colonoscopy",
        "category": "Gastroenterology",
        "duration_minutes": 45,
        "anesthesia": "Moderate sedation or MAC",
        "steps": [
            "Verify patient identity, consent, and bowel prep adequacy",
            "Position patient in left lateral decubitus",
            "Perform digital rectal exam",
            "Induce moderate sedation",
            "Insert colonoscope and advance to cecum",
            "Confirm cecal intubation (appendiceal orifice, ileocecal valve)",
            "Withdraw scope slowly (minimum 6-minute withdrawal time)",
            "Inspect all mucosal surfaces during withdrawal",
            "Retroflexion in rectum to inspect distal rectum",
            "Document findings, Boston Bowel Prep Score",
        ],
        "required_equipment": [
            {"item": "Adult colonoscope", "quantity": 1, "critical": True},
            {"item": "CO2 insufflator", "quantity": 1, "critical": True},
            {"item": "Water irrigation pump", "quantity": 1, "critical": True},
            {"item": "Pulse oximeter", "quantity": 1, "critical": True},
            {"item": "Capnography monitor", "quantity": 1, "critical": True},
            {"item": "Suction apparatus", "quantity": 1, "critical": True},
            {"item": "Crash cart nearby", "quantity": 1, "critical": True},
        ],
        "backup_equipment": [
            {"item": "Snare (hot and cold)", "trigger": "polyp_found", "critical": True},
            {"item": "Hemostatic clips", "trigger": "bleeding_risk", "critical": True},
            {"item": "Epinephrine injection", "trigger": "bleeding_risk", "critical": True},
            {"item": "Pediatric colonoscope", "trigger": "difficult_anatomy", "critical": False},
        ],
        "required_personnel": [
            {"role": "Gastroenterologist", "required": True, "responsibility": "Performs procedure"},
            {"role": "Anesthesiologist/CRNA", "required": True, "responsibility": "Sedation management"},
            {"role": "Endoscopy Nurse", "required": True, "responsibility": "Assists with instruments"},
            {"role": "Endoscopy Technician", "required": True, "responsibility": "Scope and room"},
            {"role": "Recovery Nurse", "required": True, "responsibility": "Post-procedure care"},
        ],
        "pre_procedure_prep": [
            {"task": "Complete bowel preparation (split-dose PEG)", "timeframe": "Day before + morning of", "responsible": "Patient"},
            {"task": "Clear liquid diet day before procedure", "timeframe": "Day before", "responsible": "Patient"},
            {"task": "Hold anticoagulants per protocol", "timeframe": "3-7 days before", "responsible": "Ordering physician", "condition": "on_blood_thinners"},
            {"task": "Hold iron supplements 5 days before", "timeframe": "5 days before", "responsible": "Patient"},
            {"task": "Confirm escort/driver", "timeframe": "Day before", "responsible": "Pre-op nurse", "condition": "sedation_planned"},
            {"task": "Review labs if indicated", "timeframe": "Within 30 days", "responsible": "Ordering physician"},
        ],
        "risks_and_contraindications": [
            {"risk": "Perforation", "incidence": "0.05-0.1%", "severity": "Critical"},
            {"risk": "Post-polypectomy bleeding", "incidence": "1-2%", "severity": "High"},
            {"risk": "Post-polypectomy syndrome", "incidence": "0.5%", "severity": "Moderate"},
            {"risk": "Splenic injury", "incidence": "<0.01%", "severity": "Critical"},
            {"risk": "Adverse sedation event", "incidence": "0.5%", "severity": "High"},
        ],
        "contraindications_absolute": [
            "Suspected perforation",
            "Fulminant colitis",
            "Recent acute diverticulitis (<6 weeks)",
            "Hemodynamic instability",
        ],
        "contraindications_relative": [
            "Inadequate bowel preparation",
            "Recent myocardial infarction",
            "Severe coagulopathy",
            "Large abdominal aortic aneurysm",
        ],
        "post_procedure": [
            {"task": "Monitor recovery until fully awake and passing gas", "responsible": "Recovery nurse"},
            {"task": "Watch for signs of perforation x 2 hours", "responsible": "Recovery nurse"},
            {"task": "Provide diet and activity instructions", "responsible": "Discharge nurse"},
            {"task": "Schedule follow-up per polyp surveillance guidelines", "responsible": "Gastroenterologist"},
        ],
        "high_risk_factors": {
            "bleeding_risk": ["anticoagulant use", "antiplatelet therapy", "thrombocytopenia", "large polyps"],
            "perforation_risk": ["diverticular disease", "prior abdominal surgery", "radiation therapy", "stricture"],
            "sedation_risk": ["sleep apnea", "obesity", "COPD", "advanced age >80", "liver disease"],
            "incomplete_exam_risk": ["prior surgery", "severe diverticulosis", "redundant colon", "poor prep"],
        },
    },
    "27447": {
        "cpt_code": "27447",
        "name": "Total Knee Arthroplasty (Replacement)",
        "category": "Orthopedic Surgery",
        "duration_minutes": 120,
        "anesthesia": "General or Spinal/Epidural",
        "steps": [
            "Patient positioning (supine with knee flexed)",
            "Apply tourniquet to upper thigh",
            "Perform surgical time-out",
            "Make midline longitudinal incision",
            "Perform medial parapatellar arthrotomy",
            "Evert patella, expose joint surfaces",
            "Perform distal femoral cut with alignment guide",
            "Perform proximal tibial cut",
            "Size and trial femoral component",
            "Size and trial tibial component",
            "Assess alignment, balance, and ROM with trials",
            "Cement and implant final components",
            "Close in layers, apply sterile dressing",
            "Release tourniquet, confirm hemostasis",
        ],
        "required_equipment": [
            {"item": "Knee arthroplasty instrument set", "quantity": 1, "critical": True},
            {"item": "Knee implant system (femoral, tibial, poly insert)", "quantity": 1, "critical": True},
            {"item": "Bone cement (PMMA)", "quantity": 2, "critical": True},
            {"item": "Tourniquet system", "quantity": 1, "critical": True},
            {"item": "Surgical power tools (saw, drill)", "quantity": 1, "critical": True},
            {"item": "Pulse lavage irrigation", "quantity": 1, "critical": True},
            {"item": "Electrocautery", "quantity": 1, "critical": True},
            {"item": "Cell saver (if high blood loss expected)", "quantity": 1, "critical": False},
            {"item": "Intraoperative fluoroscopy (C-arm)", "quantity": 1, "critical": False},
        ],
        "backup_equipment": [
            {"item": "Constrained implant components", "trigger": "ligament_instability", "critical": True},
            {"item": "Stems/augments", "trigger": "bone_deficiency", "critical": True},
            {"item": "Tranexamic acid (TXA)", "trigger": "bleeding_risk", "critical": True},
            {"item": "Additional bone cement", "trigger": "revision_case", "critical": False},
        ],
        "required_personnel": [
            {"role": "Orthopedic Surgeon", "required": True, "responsibility": "Performs surgery"},
            {"role": "Surgical First Assistant", "required": True, "responsibility": "Assists with retraction, exposure"},
            {"role": "Anesthesiologist", "required": True, "responsibility": "Anesthesia and hemodynamic management"},
            {"role": "Scrub Nurse/Tech", "required": True, "responsibility": "Instrument passing, counts"},
            {"role": "Circulating Nurse", "required": True, "responsibility": "Room coordination, documentation"},
            {"role": "Implant Representative", "required": False, "responsibility": "Technical support for implant system"},
        ],
        "pre_procedure_prep": [
            {"task": "Preoperative medical clearance (cardiac, pulmonary)", "timeframe": "2-4 weeks before", "responsible": "Primary care/Cardiologist"},
            {"task": "Hold anticoagulants and NSAIDs", "timeframe": "5-7 days before", "responsible": "Surgeon"},
            {"task": "MRSA screening nasal swab", "timeframe": "1 week before", "responsible": "Pre-op clinic"},
            {"task": "Pre-operative chlorhexidine shower protocol", "timeframe": "Night before + morning of", "responsible": "Patient"},
            {"task": "Type and screen (blood bank)", "timeframe": "Day of surgery", "responsible": "Anesthesia"},
            {"task": "Confirm implant availability and sizing", "timeframe": "Day before", "responsible": "OR coordinator"},
            {"task": "VTE prophylaxis plan documented", "timeframe": "Pre-op", "responsible": "Surgeon"},
            {"task": "Physical therapy consult arranged for post-op day 0-1", "timeframe": "Pre-op", "responsible": "Care coordinator"},
        ],
        "risks_and_contraindications": [
            {"risk": "Deep vein thrombosis/PE", "incidence": "1-2%", "severity": "Critical"},
            {"risk": "Surgical site infection", "incidence": "1-2%", "severity": "High"},
            {"risk": "Periprosthetic fracture", "incidence": "0.5-1%", "severity": "High"},
            {"risk": "Nerve injury (peroneal)", "incidence": "0.3-1%", "severity": "High"},
            {"risk": "Implant loosening", "incidence": "5-10% at 15yr", "severity": "Moderate"},
            {"risk": "Stiffness/arthrofibrosis", "incidence": "5-10%", "severity": "Moderate"},
            {"risk": "Blood loss requiring transfusion", "incidence": "5-10%", "severity": "Moderate"},
        ],
        "contraindications_absolute": [
            "Active joint infection",
            "Severe peripheral vascular disease precluding healing",
            "Nonfunctional extensor mechanism",
        ],
        "contraindications_relative": [
            "Morbid obesity (BMI >40)",
            "Active skin infection near surgical site",
            "Severe osteoporosis",
            "Uncontrolled diabetes (HbA1c >8%)",
        ],
        "post_procedure": [
            {"task": "DVT prophylaxis (enoxaparin or aspirin per protocol)", "responsible": "Surgeon/Nursing"},
            {"task": "Weight-bearing as tolerated with walker", "responsible": "Physical therapy"},
            {"task": "Continuous passive motion or active ROM exercises", "responsible": "Physical therapy"},
            {"task": "Wound check at 2 weeks, staple removal", "responsible": "Surgeon"},
            {"task": "Monitor for infection signs (redness, drainage, fever)", "responsible": "Nursing/Patient"},
        ],
        "high_risk_factors": {
            "bleeding_risk": ["anticoagulant use", "liver disease", "thrombocytopenia"],
            "infection_risk": ["diabetes", "obesity", "immunosuppression", "prior joint infection", "smoking"],
            "vte_risk": ["prior DVT/PE", "malignancy", "immobility", "obesity", "hypercoagulable state"],
            "cardiac_risk": ["CAD", "CHF", "valvular disease", "recent MI", "uncontrolled hypertension"],
        },
    },
}


def get_procedure(cpt_code: str):
    return PROCEDURES.get(cpt_code)


def list_procedures() -> list:
    return [
        {"cpt_code": p["cpt_code"], "name": p["name"], "category": p["category"]}
        for p in PROCEDURES.values()
    ]


def get_applicable_risks(procedure, patient_factors):
    """Given patient factors, return which high-risk categories are triggered."""
    triggered = []
    for category, factors in procedure.get("high_risk_factors", {}).items():
        matched = [f for f in factors if any(pf.lower() in f.lower() for pf in patient_factors)]
        if matched:
            triggered.append({
                "category": category.replace("_", " ").title(),
                "matched_factors": matched,
                "patient_triggers": [pf for pf in patient_factors if any(pf.lower() in f.lower() for f in factors)],
            })
    return triggered


def get_conditional_equipment(procedure, triggers):
    """Get backup equipment that should be added based on triggers."""
    needed = []
    for equip in procedure.get("backup_equipment", []):
        if equip["trigger"] in triggers:
            needed.append(equip)
    return needed


def get_conditional_prep(procedure, conditions):
    """Get prep items that apply based on patient conditions."""
    items = []
    for prep in procedure.get("pre_procedure_prep", []):
        condition = prep.get("condition")
        if condition is None or condition in conditions:
            items.append(prep)
    return items
