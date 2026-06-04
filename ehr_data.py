"""
Realistic Epic EHR data — simulates what you'd see pulling from
Epic's Hyperspace modules: Chart Review, MAR, Orders, Problem List,
Surgical History, Notes, etc.

This is structured the way Epic actually stores/displays it internally.
In production, these would come from FHIR endpoints or Epic Interconnect.
"""

PATIENTS = {
    "martinez_roberto": {
        # === DEMOGRAPHICS (Epic: Patient Header / Banner Bar) ===
        "demographics": {
            "mrn": "MRN-00847291",
            "full_name": "Martinez, Roberto J",
            "preferred_name": "Roberto",
            "dob": "1962-03-15",
            "age": 64,
            "sex": "Male",
            "gender_identity": "Male",
            "race": "Hispanic/Latino",
            "language": "English (Spanish-speaking)",
            "marital_status": "Married",
            "address": "4521 Maple Drive, San Diego, CA 92103",
            "phone_home": "(619) 555-1234",
            "phone_cell": "(619) 555-5678",
            "email": "rmartinez62@email.com",
            "insurance": {
                "primary": "Blue Cross Blue Shield - PPO",
                "member_id": "BCB992841003",
                "group": "SDGE-EMP-2024",
                "authorization": "AUTH-2026-04281 (Pre-auth obtained 05/22/2026)",
            },
            "pcp": "Dr. Amanda Foster, MD — Internal Medicine",
            "pcp_phone": "(619) 555-9900",
            "emergency_contact": {
                "name": "Sarah Martinez",
                "relationship": "Wife",
                "phone": "(619) 555-8765",
                "alt_phone": "(619) 555-4321",
            },
            "advance_directives": "Full Code",
            "code_status": "Full Code",
        },

        # === PROBLEM LIST (Epic: Problem List Activity) ===
        "problem_list": [
            {"icd10": "K21.0", "description": "Gastroesophageal reflux disease with esophagitis", "status": "Active", "onset": "2024-08-15", "noted_by": "Dr. Foster"},
            {"icd10": "Z95.5", "description": "Presence of coronary angioplasty implant and graft", "status": "Active", "onset": "2024-04-10", "noted_by": "Dr. Patel (Cardiology)"},
            {"icd10": "I25.10", "description": "Atherosclerotic heart disease of native coronary artery", "status": "Active", "onset": "2024-04-10", "noted_by": "Dr. Patel"},
            {"icd10": "G47.33", "description": "Obstructive sleep apnea (moderate)", "status": "Active", "onset": "2021-06-20", "noted_by": "Dr. Kim (Pulm)"},
            {"icd10": "E78.5", "description": "Hyperlipidemia, unspecified", "status": "Active", "onset": "2019-03-01", "noted_by": "Dr. Foster"},
            {"icd10": "I10", "description": "Essential hypertension", "status": "Active", "onset": "2018-11-15", "noted_by": "Dr. Foster"},
            {"icd10": "M54.5", "description": "Low back pain", "status": "Active", "onset": "2023-01-10", "noted_by": "Dr. Foster"},
            {"icd10": "F17.210", "description": "Nicotine dependence, cigarettes, uncomplicated", "status": "Resolved", "onset": "2000-01-01", "noted_by": "Dr. Foster", "resolved": "2019-05-01"},
        ],

        # === MEDICATION LIST (Epic: MAR / Medication Activity) ===
        "medications": [
            {
                "name": "clopidogrel (Plavix)",
                "generic": "clopidogrel",
                "dose": "75 mg",
                "route": "Oral",
                "frequency": "Daily",
                "prescriber": "Dr. Rajesh Patel (Cardiology)",
                "start_date": "2024-04-12",
                "indication": "Coronary stent — DAPT protocol",
                "sig": "Take 1 tablet by mouth once daily",
                "pharmacy": "CVS #4521 — (619) 555-7700",
                "refills_remaining": 3,
                "last_filled": "2026-05-01",
                "class": "Antiplatelet",
                "high_alert": True,
                "high_alert_reason": "Bleeding risk — do NOT discontinue without cardiology approval",
            },
            {
                "name": "metoprolol succinate (Toprol-XL)",
                "generic": "metoprolol",
                "dose": "50 mg",
                "route": "Oral",
                "frequency": "Daily",
                "prescriber": "Dr. Rajesh Patel (Cardiology)",
                "start_date": "2024-04-12",
                "indication": "Rate control, post-PCI",
                "sig": "Take 1 tablet by mouth once daily in the morning",
                "class": "Beta Blocker",
                "high_alert": False,
            },
            {
                "name": "atorvastatin (Lipitor)",
                "generic": "atorvastatin",
                "dose": "80 mg",
                "route": "Oral",
                "frequency": "Daily at bedtime",
                "prescriber": "Dr. Rajesh Patel (Cardiology)",
                "start_date": "2024-04-12",
                "indication": "High-intensity statin post-ACS",
                "sig": "Take 1 tablet by mouth at bedtime",
                "class": "Statin",
                "high_alert": False,
            },
            {
                "name": "omeprazole (Prilosec)",
                "generic": "omeprazole",
                "dose": "40 mg",
                "route": "Oral",
                "frequency": "Daily before breakfast",
                "prescriber": "Dr. Emily Chen (Gastroenterology)",
                "start_date": "2025-09-20",
                "indication": "GERD with esophagitis",
                "sig": "Take 1 capsule by mouth 30 minutes before breakfast",
                "class": "Proton Pump Inhibitor",
                "high_alert": False,
            },
            {
                "name": "lisinopril (Zestril)",
                "generic": "lisinopril",
                "dose": "10 mg",
                "route": "Oral",
                "frequency": "Daily",
                "prescriber": "Dr. Amanda Foster (PCP)",
                "start_date": "2018-12-01",
                "indication": "Hypertension, cardioprotective",
                "sig": "Take 1 tablet by mouth once daily",
                "class": "ACE Inhibitor",
                "high_alert": False,
            },
        ],

        # === ALLERGIES (Epic: Allergy Activity) ===
        "allergies": [
            {
                "allergen": "Penicillin",
                "type": "Medication",
                "reaction": "Rash (maculopapular)",
                "severity": "Mild",
                "status": "Active",
                "verified": True,
                "verified_date": "2024-04-10",
                "source": "Patient-reported, confirmed in prior records",
            },
            {
                "allergen": "Shellfish",
                "type": "Food",
                "reaction": "Hives, facial swelling",
                "severity": "Moderate",
                "status": "Active",
                "verified": True,
                "verified_date": "2019-08-15",
                "source": "ED visit 2019 — documented anaphylactoid reaction",
            },
        ],

        # === SURGICAL / PROCEDURE HISTORY (Epic: Surgical History) ===
        "surgical_history": [
            {
                "procedure": "Percutaneous Coronary Intervention (PCI) with DES placement",
                "date": "2024-04-10",
                "surgeon": "Dr. Rajesh Patel",
                "facility": "UC San Diego Medical Center",
                "details": "Single drug-eluting stent to LAD. Uncomplicated. DAPT initiated (ASA + Plavix). ASA discontinued after 3 months per protocol.",
                "anesthesia": "Conscious sedation (Midazolam/Fentanyl)",
            },
            {
                "procedure": "Appendectomy (laparoscopic)",
                "date": "2005-07-22",
                "surgeon": "Dr. Williams",
                "facility": "Scripps Memorial",
                "details": "Uncomplicated. No adverse anesthesia events.",
                "anesthesia": "General",
            },
        ],

        # === SCHEDULED PROCEDURE (Epic: Scheduling / Orders) ===
        "scheduled_procedure": {
            "procedure_name": "EGD (Esophagogastroduodenoscopy) with biopsy",
            "cpt_code": "43239",
            "scheduled_date": "2026-06-05",
            "scheduled_time": "08:30",
            "location": "Endoscopy Suite 3, GI Procedures Center",
            "performing_provider": "Dr. Emily Chen, MD — Gastroenterology",
            "referring_provider": "Dr. Amanda Foster, MD — Internal Medicine",
            "indication": "Persistent GERD symptoms despite maximal PPI therapy. Rule out Barrett's esophagus. Evaluate for H. pylori.",
            "pre_auth_status": "Authorized",
            "pre_auth_number": "AUTH-2026-04281",
            "estimated_duration": "20-30 minutes",
            "anesthesia_plan": "Monitored Anesthesia Care (MAC) with Propofol",
            "anesthesia_provider": "Dr. Michael Torres, MD — Anesthesiology",
            "pre_procedure_orders": [
                "NPO after midnight (clear liquids until 4:30 AM)",
                "Hold Plavix (clopidogrel) 5 days prior — LAST DOSE 05/31/2026",
                "Continue metoprolol, atorvastatin, lisinopril morning of with sip of water",
                "Continue omeprazole — will hold day of for pH testing",
                "Arrive at 07:00 for pre-procedure prep",
                "IV access — 20G or larger, right hand/forearm preferred",
                "Verify escort available for discharge",
            ],
            "consent_status": "Obtained — signed 05/28/2026",
            "consent_risks_discussed": [
                "Bleeding (increased risk given recent antiplatelet therapy)",
                "Perforation (<0.1%)",
                "Adverse reaction to sedation",
                "Aspiration",
                "Missed lesion",
            ],
        },

        # === RECENT NOTES (Epic: Notes Activity) ===
        "notes": [
            {
                "type": "GI Consultation Note",
                "date": "2026-05-15",
                "author": "Dr. Emily Chen, MD",
                "snippet": """
ASSESSMENT/PLAN:
64 yo male with persistent GERD symptoms x 6 months despite omeprazole 40mg daily.
Symptoms: daily heartburn, occasional regurgitation, mild dysphagia to solids.
No alarm symptoms (weight loss, GI bleeding, anemia).
Given duration of symptoms and incomplete response to PPI, recommend EGD with biopsy
to evaluate for Barrett's, eosinophilic esophagitis, and H. pylori.

MEDICATION CONSIDERATIONS:
- Patient on clopidogrel (Plavix) for DES placed 04/2024. Now >12 months post-stent.
- Per ASGE guidelines and cardiology approval (Dr. Patel contacted 05/14/2026),
  clopidogrel may be held for 5 days pre-procedure given low-risk stent status.
- Cardiology clearance obtained. Document in chart.
- Bleeding risk: MODERATE (given recent antiplatelet use, plan cold biopsy forceps,
  ensure hemostasis equipment available).
                """,
            },
            {
                "type": "Cardiology Clearance Note",
                "date": "2026-05-14",
                "author": "Dr. Rajesh Patel, MD",
                "snippet": """
Re: Roberto Martinez MRN-00847291
Procedure: EGD with biopsy — scheduled 06/05/2026

Patient is now 14 months post-PCI with DES to LAD.
Current regimen: Clopidogrel 75mg daily (ASA discontinued 07/2024 per protocol).
Stent is well-endothelialized at this point. Low risk for stent thrombosis with brief hold.

RECOMMENDATION: May hold clopidogrel for 5 days pre-procedure.
Last dose should be 05/31/2026. Resume immediately post-procedure (06/05/2026 evening).
No bridging anticoagulation required.

If unexpected high-risk pathology found requiring intervention, contact me immediately.
                """,
            },
            {
                "type": "Pre-Procedure Nursing Assessment",
                "date": "2026-05-28",
                "author": "RN Jessica Huang",
                "snippet": """
PHONE ASSESSMENT — Pre-procedure screening call:
- Patient confirms understanding of NPO instructions
- Clopidogrel hold discussed — patient will take last dose 05/31. Confirmed.
- Wife (Sarah) confirmed as driver/escort for 06/05
- Patient uses CPAP at home for sleep apnea — will bring to facility per protocol
- Allergies verified: Penicillin (rash), Shellfish (hives/swelling)
- Denies recent illness, fever, cough, COVID exposure
- Denies use of blood thinners other than Plavix (no ASA, no NSAIDs)
- Last colonoscopy: 2023, normal
- Weight: 196 lbs (89 kg) Height: 5'9" (175 cm)
- ASA Physical Status: III (cardiac history, sleep apnea)
                """,
            },
        ],

        # === LABS (Epic: Results Activity) ===
        "labs": {
            "collection_date": "2026-05-20",
            "ordered_by": "Dr. Emily Chen",
            "results": [
                {"test": "CBC - WBC", "value": 7.2, "unit": "x10^3/uL", "reference": "4.5-11.0", "flag": ""},
                {"test": "CBC - Hemoglobin", "value": 14.1, "unit": "g/dL", "reference": "13.5-17.5", "flag": ""},
                {"test": "CBC - Hematocrit", "value": 42.3, "unit": "%", "reference": "38.3-48.6", "flag": ""},
                {"test": "CBC - Platelets", "value": 245, "unit": "x10^3/uL", "reference": "150-400", "flag": ""},
                {"test": "BMP - Sodium", "value": 140, "unit": "mEq/L", "reference": "136-145", "flag": ""},
                {"test": "BMP - Potassium", "value": 4.2, "unit": "mEq/L", "reference": "3.5-5.1", "flag": ""},
                {"test": "BMP - Creatinine", "value": 1.0, "unit": "mg/dL", "reference": "0.7-1.3", "flag": ""},
                {"test": "BMP - Glucose", "value": 102, "unit": "mg/dL", "reference": "70-100", "flag": "H"},
                {"test": "PT/INR", "value": 1.1, "unit": "", "reference": "0.8-1.2", "flag": ""},
                {"test": "Type & Screen", "value": "O Positive", "unit": "", "reference": "N/A", "flag": ""},
            ],
        },

        # === VITALS (Epic: Flowsheet) ===
        "vitals": {
            "date": "2026-05-28",
            "blood_pressure": "138/82",
            "heart_rate": 72,
            "respiratory_rate": 16,
            "temperature": 98.4,
            "o2_saturation": 96,
            "weight_kg": 89,
            "height_cm": 175,
            "bmi": 29.1,
            "pain_score": 2,
            "pain_location": "Epigastric (burning)",
        },

        # === IMAGING (Epic: Imaging Activity) ===
        "imaging": [
            {
                "study": "Chest X-Ray (PA/Lateral)",
                "date": "2026-05-20",
                "result": "IMPRESSION: Heart size normal. Lungs clear. Coronary stent visualized in expected position. No acute cardiopulmonary process.",
                "ordered_by": "Dr. Foster",
            },
        ],
    },

    "thompson_margaret": {
        "demographics": {
            "mrn": "MRN-01293847",
            "full_name": "Thompson, Margaret A",
            "preferred_name": "Peggy",
            "dob": "1955-11-22",
            "age": 70,
            "sex": "Female",
            "gender_identity": "Female",
            "race": "White/Caucasian",
            "language": "English",
            "marital_status": "Widowed",
            "address": "892 Oak Lane, La Jolla, CA 92037",
            "phone_home": "(858) 555-2200",
            "phone_cell": "(858) 555-3311",
            "email": "peggyt55@email.com",
            "insurance": {
                "primary": "Medicare Part A & B",
                "member_id": "1EG4-TE5-MK72",
                "group": "N/A",
                "secondary": "AARP Supplemental Plan F",
                "authorization": "AUTH-2026-05102 (Pre-auth obtained 05/15/2026)",
            },
            "pcp": "Dr. Robert Kim, MD — Family Medicine",
            "pcp_phone": "(858) 555-4400",
            "emergency_contact": {
                "name": "Jessica Thompson",
                "relationship": "Daughter",
                "phone": "(858) 555-6677",
                "alt_phone": "(619) 555-8899",
            },
            "advance_directives": "Full Code (reviewed 01/2026)",
            "code_status": "Full Code",
        },

        "problem_list": [
            {"icd10": "M17.11", "description": "Primary osteoarthritis, right knee", "status": "Active", "onset": "2022-03-10", "noted_by": "Dr. Wright (Ortho)"},
            {"icd10": "E11.65", "description": "Type 2 diabetes mellitus with hyperglycemia", "status": "Active", "onset": "2015-08-20", "noted_by": "Dr. Kim"},
            {"icd10": "I10", "description": "Essential hypertension", "status": "Active", "onset": "2012-04-15", "noted_by": "Dr. Kim"},
            {"icd10": "I48.91", "description": "Atrial fibrillation, unspecified", "status": "Active", "onset": "2020-11-30", "noted_by": "Dr. Nakamura (Cards)"},
            {"icd10": "E78.5", "description": "Hyperlipidemia", "status": "Active", "onset": "2014-01-10", "noted_by": "Dr. Kim"},
            {"icd10": "N39.0", "description": "Urinary tract infection (recurrent)", "status": "Resolved", "onset": "2025-12-01", "noted_by": "Dr. Kim", "resolved": "2025-12-14"},
            {"icd10": "Z87.39", "description": "History of DVT, left lower extremity (2019)", "status": "Historical", "onset": "2019-06-15", "noted_by": "Dr. Nakamura"},
            {"icd10": "E66.01", "description": "Morbid obesity due to excess calories", "status": "Active", "onset": "2018-01-01", "noted_by": "Dr. Kim"},
        ],

        "medications": [
            {
                "name": "warfarin (Coumadin)",
                "generic": "warfarin",
                "dose": "5 mg",
                "route": "Oral",
                "frequency": "Daily (dose adjusted per INR)",
                "prescriber": "Dr. Nakamura (Cardiology)",
                "start_date": "2020-12-15",
                "indication": "Atrial fibrillation — CHA2DS2-VASc = 5",
                "sig": "Take as directed based on INR results",
                "class": "Anticoagulant (Vitamin K Antagonist)",
                "high_alert": True,
                "high_alert_reason": "Active anticoagulation — HIGH bleeding risk. INR must be monitored. Hold per surgical protocol.",
                "inr_target": "2.0-3.0",
                "last_inr": {"value": 2.3, "date": "2026-05-25"},
            },
            {
                "name": "metformin (Glucophage)",
                "generic": "metformin",
                "dose": "1000 mg",
                "route": "Oral",
                "frequency": "Twice daily with meals",
                "prescriber": "Dr. Robert Kim (PCP)",
                "start_date": "2015-09-01",
                "indication": "Type 2 diabetes",
                "sig": "Take 1 tablet by mouth twice daily with breakfast and dinner",
                "class": "Biguanide",
                "high_alert": False,
                "note": "Hold 48 hours before surgery if contrast dye planned",
            },
            {
                "name": "lisinopril (Zestril)",
                "generic": "lisinopril",
                "dose": "20 mg",
                "route": "Oral",
                "frequency": "Daily",
                "prescriber": "Dr. Robert Kim (PCP)",
                "start_date": "2012-05-01",
                "indication": "Hypertension, diabetic nephroprotection",
                "sig": "Take 1 tablet by mouth once daily",
                "class": "ACE Inhibitor",
                "high_alert": False,
            },
            {
                "name": "atorvastatin (Lipitor)",
                "generic": "atorvastatin",
                "dose": "40 mg",
                "route": "Oral",
                "frequency": "Daily at bedtime",
                "prescriber": "Dr. Robert Kim (PCP)",
                "start_date": "2014-02-01",
                "indication": "Hyperlipidemia, CV risk reduction",
                "sig": "Take 1 tablet by mouth at bedtime",
                "class": "Statin",
                "high_alert": False,
            },
            {
                "name": "insulin glargine (Lantus)",
                "generic": "insulin glargine",
                "dose": "22 units",
                "route": "Subcutaneous",
                "frequency": "Once daily at bedtime",
                "prescriber": "Dr. Robert Kim (PCP)",
                "start_date": "2023-03-15",
                "indication": "Type 2 DM — inadequate control with metformin alone",
                "sig": "Inject 22 units subcutaneously at bedtime",
                "class": "Long-acting Insulin",
                "high_alert": True,
                "high_alert_reason": "Insulin — hypoglycemia risk perioperatively. Adjust dose per surgical protocol.",
            },
            {
                "name": "acetaminophen (Tylenol)",
                "generic": "acetaminophen",
                "dose": "1000 mg",
                "route": "Oral",
                "frequency": "Every 6 hours as needed",
                "prescriber": "Dr. Wright (Orthopedics)",
                "start_date": "2025-11-01",
                "indication": "Knee pain",
                "sig": "Take 2 tablets (500mg each) by mouth every 6 hours as needed for pain. Max 3000mg/day.",
                "class": "Analgesic (non-opioid)",
                "high_alert": False,
            },
        ],

        "allergies": [
            {
                "allergen": "Sulfonamide antibiotics",
                "type": "Medication",
                "reaction": "Anaphylaxis (throat swelling, hypotension, urticaria)",
                "severity": "Severe — ANAPHYLAXIS",
                "status": "Active",
                "verified": True,
                "verified_date": "2020-01-10",
                "source": "ED visit 2008, confirmed by allergist 2020",
            },
            {
                "allergen": "Latex",
                "type": "Environmental",
                "reaction": "Contact dermatitis, hand swelling",
                "severity": "Moderate",
                "status": "Active",
                "verified": True,
                "verified_date": "2020-01-10",
                "source": "Occupational exposure (former nurse). Confirmed by patch testing.",
            },
            {
                "allergen": "Iodinated contrast dye",
                "type": "Medication",
                "reaction": "Flushing, mild bronchospasm",
                "severity": "Moderate",
                "status": "Active",
                "verified": True,
                "verified_date": "2022-11-01",
                "source": "Reaction during CT scan 2022. Pre-med protocol required if contrast needed.",
            },
        ],

        "surgical_history": [
            {
                "procedure": "Left knee arthroscopy with partial meniscectomy",
                "date": "2019-02-15",
                "surgeon": "Dr. James Wright",
                "facility": "Scripps La Jolla",
                "details": "Uncomplicated. Warfarin held 5 days pre-op, bridged with Lovenox. Resumed POD#1.",
                "anesthesia": "Spinal",
            },
            {
                "procedure": "Cholecystectomy (laparoscopic)",
                "date": "2011-09-08",
                "surgeon": "Dr. Park",
                "facility": "UCSD Medical Center",
                "details": "Uncomplicated. General anesthesia without adverse events.",
                "anesthesia": "General",
            },
            {
                "procedure": "Cesarean section x2",
                "date": "1985/1988",
                "surgeon": "Dr. Adams",
                "facility": "Sharp Memorial",
                "details": "Uncomplicated x2.",
                "anesthesia": "Spinal (both)",
            },
        ],

        "scheduled_procedure": {
            "procedure_name": "Total Knee Arthroplasty, Right",
            "cpt_code": "27447",
            "scheduled_date": "2026-06-12",
            "scheduled_time": "07:00",
            "location": "OR Suite 7, Main Hospital — 3rd Floor Surgical Wing",
            "performing_provider": "Dr. James Wright, MD — Orthopedic Surgery",
            "first_assist": "Dr. Kevin Park, MD — Orthopedic Surgery Fellow",
            "referring_provider": "Dr. Robert Kim, MD — Family Medicine",
            "indication": "Severe right knee osteoarthritis. Failed conservative management (PT, injections, bracing). Bone-on-bone medial compartment. Significant functional limitation.",
            "pre_auth_status": "Authorized",
            "pre_auth_number": "AUTH-2026-05102",
            "estimated_duration": "90-120 minutes",
            "anesthesia_plan": "Spinal with sedation (patient preference, prior good experience)",
            "anesthesia_provider": "Dr. Lisa Park, MD — Anesthesiology",
            "implant_system": "Smith & Nephew LEGION Total Knee System, size TBD intra-op",
            "implant_rep": "Mike Chen, Smith & Nephew — (858) 555-9900",
            "pre_procedure_orders": [
                "Hold warfarin 5 days prior — LAST DOSE 06/07/2026",
                "Bridge with enoxaparin (Lovenox) 1mg/kg BID starting 06/08/2026",
                "Last Lovenox dose: evening of 06/10/2026 (>24h before surgery)",
                "Hold metformin 48 hours before surgery (last dose 06/10/2026)",
                "Reduce Lantus to HALF dose (11 units) night before surgery",
                "NO Lantus morning of surgery",
                "Continue lisinopril and atorvastatin with sip of water morning of",
                "MRSA decolonization: Mupirocin nasal BID x 5 days pre-op (start 06/07)",
                "Chlorhexidine (Hibiclens) shower night before AND morning of surgery",
                "NPO after midnight",
                "Arrive at 05:00 for pre-op preparation",
                "TYPE AND CROSSMATCH — 2 units PRBCs on hold",
                "LATEX-FREE PROTOCOL — all supplies and gloves must be latex-free",
                "Pre-op antibiotics: Vancomycin 1g IV (sulfa allergy — cannot use cefazolin)",
            ],
            "consent_status": "Obtained — signed 05/20/2026",
            "consent_risks_discussed": [
                "Infection (1-2%)",
                "DVT/PE (1-2% with prophylaxis)",
                "Bleeding requiring transfusion (5-10%)",
                "Nerve/vessel injury",
                "Stiffness/limited ROM",
                "Need for revision surgery",
                "Anesthesia risks",
                "Death (<0.5%)",
            ],
        },

        "notes": [
            {
                "type": "Orthopedic Surgery Pre-Op Note",
                "date": "2026-05-20",
                "author": "Dr. James Wright, MD",
                "snippet": """
PRE-OPERATIVE ASSESSMENT:
70 yo female with severe R knee OA, bone-on-bone medial compartment.
Failed: 6 months PT, viscosupplementation x3, cortisone injections x2, unloader brace.
Functionally limited: uses walker, cannot climb stairs, nighttime pain.
BMI 35.7 — discussed weight-related surgical risk. Patient accepts risk.
HbA1c 7.8% — acceptable for surgery per our protocol (<8.0%).

HIGH-RISK FACTORS:
1. Warfarin for AFib — bridge with Lovenox per hematology protocol
2. History of DVT (2019) — ELEVATED VTE RISK. Extended prophylaxis x 4 weeks post-op.
3. Latex allergy — LATEX-FREE PROTOCOL MANDATORY
4. Sulfa allergy (anaphylaxis) — CANNOT use cefazolin. Use vancomycin for surgical prophylaxis.
5. Obesity (BMI 35.7) — increased infection risk, may need longer instruments
6. Diabetes on insulin — endocrine consult for perioperative glucose management

PLAN: Proceed with R TKA 06/12/2026. Smith & Nephew LEGION system.
                """,
            },
            {
                "type": "Hematology Consult — Anticoagulation Management",
                "date": "2026-05-22",
                "author": "Dr. Sarah Williams, MD — Hematology",
                "snippet": """
CONSULT: Perioperative anticoagulation management for R TKA

ASSESSMENT:
- Indication for warfarin: AFib with CHA2DS2-VASc = 5 (age, sex, HTN, DM, prior vascular)
- HAS-BLED score: 3 (moderate bleeding risk)
- History of DVT 2019 — additional VTE risk factor
- Surgery is HIGH bleeding risk

PLAN:
1. Hold warfarin 5 days pre-op (last dose 06/07/2026)
2. Bridge with enoxaparin 1mg/kg (90mg) BID starting 06/08
3. Last pre-op Lovenox dose: evening 06/10 (>24h before surgery)
4. Check INR morning of surgery — proceed if INR ≤ 1.5
5. Post-op: Restart Lovenox POD#1 if hemostasis adequate
6. Restart warfarin POD#1-2, overlap with Lovenox until INR therapeutic
7. Given DVT history: EXTENDED prophylaxis — 4 weeks total (vs standard 2 weeks)
8. Mechanical prophylaxis (SCDs) from admission until fully ambulatory
                """,
            },
            {
                "type": "Endocrinology Consult — Perioperative Glucose",
                "date": "2026-05-23",
                "author": "Dr. Priya Sharma, MD — Endocrinology",
                "snippet": """
CONSULT: Perioperative glucose management for R TKA

Current regimen: Metformin 1000 BID + Lantus 22u QHS
HbA1c: 7.8% (acceptable surgical range)
Fasting glucose trend: 130-160 mg/dL

PERIOPERATIVE PLAN:
1. Hold metformin 48h pre-op (lactic acidosis risk with anesthesia/contrast)
2. Night before surgery: Lantus at HALF dose (11 units)
3. Morning of surgery: NO insulin, NO metformin
4. Intra-op: D5W drip if glucose <100. Insulin drip if glucose >200.
5. Post-op: Sliding scale insulin until eating. Resume Lantus at full dose when tolerating meals.
6. Target glucose: 140-180 mg/dL perioperatively
7. Resume metformin when creatinine confirmed stable and eating (usually POD#2)
                """,
            },
            {
                "type": "Pre-Op Nursing Assessment",
                "date": "2026-05-28",
                "author": "RN Diane Cooper",
                "snippet": """
PRE-OP PHONE SCREENING:
- Patient confirms understanding of all medication holds
- Warfarin last dose confirmed: will take 06/07, then stop
- Lovenox self-injection teaching completed 05/25 — patient demonstrates proficiency
- MRSA swab result: NEGATIVE (05/22/2026)
- Chlorhexidine shower protocol reviewed — patient has Hibiclens at home
- Daughter (Jessica) confirmed as driver and support for post-op period
- Home setup: Patient lives in 1-story home, already has raised toilet seat and shower chair
- PT arranged: Home health PT starting POD#3, outpatient PT starting week 3
- Walker obtained
- LATEX ALLERGY FLAGGED — OR notified, latex-free cart ordered
- Surgical site marking: RIGHT KNEE — confirmed with patient
- Fall risk: MODERATE (age, walker use, post-surgical)
                """,
            },
        ],

        "labs": {
            "collection_date": "2026-05-25",
            "ordered_by": "Dr. Wright",
            "results": [
                {"test": "CBC - WBC", "value": 8.1, "unit": "x10^3/uL", "reference": "4.5-11.0", "flag": ""},
                {"test": "CBC - Hemoglobin", "value": 12.1, "unit": "g/dL", "reference": "12.0-16.0", "flag": ""},
                {"test": "CBC - Hematocrit", "value": 36.8, "unit": "%", "reference": "35.5-44.9", "flag": ""},
                {"test": "CBC - Platelets", "value": 198, "unit": "x10^3/uL", "reference": "150-400", "flag": ""},
                {"test": "BMP - Creatinine", "value": 1.2, "unit": "mg/dL", "reference": "0.6-1.1", "flag": "H"},
                {"test": "BMP - Glucose (fasting)", "value": 156, "unit": "mg/dL", "reference": "70-100", "flag": "H"},
                {"test": "BMP - Potassium", "value": 4.8, "unit": "mEq/L", "reference": "3.5-5.1", "flag": ""},
                {"test": "PT/INR", "value": 2.3, "unit": "", "reference": "2.0-3.0 (therapeutic)", "flag": ""},
                {"test": "HbA1c", "value": 7.8, "unit": "%", "reference": "<7.0", "flag": "H"},
                {"test": "Type & Crossmatch", "value": "A Positive — 2u PRBC available", "unit": "", "reference": "N/A", "flag": ""},
                {"test": "MRSA Nasal Screen", "value": "Negative", "unit": "", "reference": "Negative", "flag": ""},
                {"test": "UA - Urinalysis", "value": "Normal, no infection", "unit": "", "reference": "Normal", "flag": ""},
            ],
        },

        "vitals": {
            "date": "2026-05-28",
            "blood_pressure": "148/88",
            "heart_rate": 78,
            "respiratory_rate": 18,
            "temperature": 98.6,
            "o2_saturation": 95,
            "weight_kg": 95,
            "height_cm": 163,
            "bmi": 35.7,
            "pain_score": 7,
            "pain_location": "Right knee (constant, worse with weight-bearing)",
        },

        "imaging": [
            {
                "study": "X-Ray Right Knee (AP/Lateral/Sunrise)",
                "date": "2026-04-15",
                "result": "IMPRESSION: Severe tricompartmental osteoarthritis, most pronounced in medial compartment. Bone-on-bone medial joint space. Moderate osteophyte formation. Varus alignment ~8 degrees. No hardware, no acute fracture.",
                "ordered_by": "Dr. Wright",
            },
            {
                "study": "Chest X-Ray (PA/Lateral)",
                "date": "2026-05-25",
                "result": "IMPRESSION: Mild cardiomegaly. No acute infiltrate or effusion. Clear lungs. Acceptable for surgery.",
                "ordered_by": "Dr. Wright",
            },
            {
                "study": "EKG (12-lead)",
                "date": "2026-05-25",
                "result": "Atrial fibrillation with controlled ventricular rate (78 bpm). No acute ST changes. Old T-wave inversions V4-V6 (unchanged from prior).",
                "ordered_by": "Dr. L. Park (Anesthesia)",
            },
        ],
    },
}
