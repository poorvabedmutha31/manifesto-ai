"""
Manifesto AI — Pitch Deck
Run with: streamlit run pitch_deck.py --server.port 8502
"""
import streamlit as st


st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    .block-container { padding-top: 1rem; max-width: 1200px; }
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    .slide {
        background: white;
        border-radius: 16px;
        padding: 2.5rem 3rem;
        margin: 1.5rem 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.06);
        border: 1px solid #e5e7eb;
        min-height: 400px;
    }
    .slide-dark {
        background: linear-gradient(135deg, #1e293b, #334155);
        color: white;
        border: none;
    }
    .slide-dark h1, .slide-dark h2, .slide-dark h3 { color: white; }
    .slide-dark p, .slide-dark li { color: #cbd5e1; }

    .slide-accent {
        background: linear-gradient(135deg, #1e40af, #3b82f6);
        color: white;
        border: none;
    }
    .slide-accent h1, .slide-accent h2, .slide-accent h3 { color: white; }
    .slide-accent p, .slide-accent li { color: #dbeafe; }

    .big-number { font-size: 4rem; font-weight: 800; color: #dc2626; margin: 0; }
    .big-number-blue { font-size: 4rem; font-weight: 800; color: #2563eb; margin: 0; }
    .big-number-green { font-size: 4rem; font-weight: 800; color: #16a34a; margin: 0; }
    .big-number-white { font-size: 4rem; font-weight: 800; color: white; margin: 0; }

    .comparison-table {
        width: 100%;
        border-collapse: collapse;
        margin: 1rem 0;
    }
    .comparison-table th {
        background: #f1f5f9;
        padding: 0.8rem 1rem;
        text-align: left;
        border-bottom: 2px solid #e2e8f0;
        font-weight: 600;
    }
    .comparison-table td {
        padding: 0.7rem 1rem;
        border-bottom: 1px solid #f1f5f9;
        vertical-align: top;
    }
    .comparison-table .epic-col { color: #64748b; }
    .comparison-table .us-col { color: #1e40af; font-weight: 500; }
</style>
""", unsafe_allow_html=True)

# =============================================
# SLIDE 1: TITLE
# =============================================
st.markdown("""
<div class="slide slide-dark" style="text-align: center; display: flex; flex-direction: column; justify-content: center;">
    <h1 style="font-size: 3.5rem; margin-bottom: 0.5rem;">Manifesto AI</h1>
    <p style="font-size: 1.4rem; color: #94a3b8; margin: 0.5rem 0;">Pre-Procedure Intelligence Layer for the EHR</p>
    <br/><br/>
    <p style="font-size: 1rem; color: #64748b;">
        We don't replace Epic. We read it — and generate the synthesis that<br/>
        currently lives in sticky notes and the surgeon's head.
    </p>
</div>
""", unsafe_allow_html=True)

# =============================================
# SLIDE 2: THE PROBLEM
# =============================================
st.markdown("""
<div class="slide">
    <h2>The Problem: Information Exists. Synthesis Doesn't.</h2>
</div>
""", unsafe_allow_html=True)

p1, p2, p3 = st.columns(3)
with p1:
    st.markdown("""
    <p class="big-number">15+</p>
    <p><strong>Epic screens</strong> a nurse must review to prep a surgical patient</p>
    """, unsafe_allow_html=True)
with p2:
    st.markdown("""
    <p class="big-number">20 min</p>
    <p><strong>Average time</strong> a pre-op coordinator spends per patient piecing together the plan</p>
    """, unsafe_allow_html=True)
with p3:
    st.markdown("""
    <p class="big-number">22%</p>
    <p><strong>of surgical delays</strong> are caused by incomplete pre-op preparation (AORN 2023)</p>
    """, unsafe_allow_html=True)

st.markdown("""
> **The data is all there.** The patient's Plavix is in the MAR. The stent is in the Problem List.
> The biopsy is in the procedure order. But **nobody connects those three facts** into
> "hemostatic clips need to be in the room" until someone manually thinks about it.
>
> — This is what Gawande calls an "error of inaptitude" — not a knowledge gap, but a synthesis gap.
""")

# =============================================
# SLIDE 3: WHAT EPIC DOES vs. WHAT WE DO
# =============================================
st.markdown("""
<div class="slide">
    <h2>Epic is a Data Warehouse. We're the Intelligence Layer.</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<table class="comparison-table">
    <tr>
        <th style="width: 25%;">Task</th>
        <th style="width: 37%;" class="epic-col">What Epic Does</th>
        <th style="width: 37%;" class="us-col">What We Add</th>
    </tr>
    <tr>
        <td><strong>Drug alerts</strong></td>
        <td class="epic-col">Fires individual BPA pop-ups (alert fatigue — 90%+ override rate)</td>
        <td class="us-col">Connects medication + procedure + history → specific action with context</td>
    </tr>
    <tr>
        <td><strong>Pre-op prep</strong></td>
        <td class="epic-col">Stores orders as a list. Coordinator manually interprets.</td>
        <td class="us-col">Generates role-specific task lists: what YOU need to do, and why</td>
    </tr>
    <tr>
        <td><strong>Protocol deviations</strong></td>
        <td class="epic-col">Doesn't flag when a patient DOESN'T fit standard protocol</td>
        <td class="us-col">Explicitly states: "Standard protocol won't work because..."</td>
    </tr>
    <tr>
        <td><strong>Readiness tracking</strong></td>
        <td class="epic-col">Each item (labs, consent, escort) is in a different module</td>
        <td class="us-col">Single view: is this patient actually ready to go? What's still pending?</td>
    </tr>
    <tr>
        <td><strong>Role-based views</strong></td>
        <td class="epic-col">Same chart view for everyone. Nurse sees surgeon's notes, surgeon sees nursing flowsheets.</td>
        <td class="us-col">Anesthesia sees anesthesia concerns. Nurse sees nursing tasks. No noise.</td>
    </tr>
</table>
""", unsafe_allow_html=True)

# =============================================
# SLIDE 4: HOW IT WORKS
# =============================================
st.markdown("""
<div class="slide slide-accent" style="text-align: center;">
    <h2>How It Works</h2>
    <br/>
    <p style="font-size: 1.1rem;">Launches inside Epic as a SMART on FHIR app.<br/>Zero new data entry. Zero documentation burden.</p>
</div>
""", unsafe_allow_html=True)

h1, h2, h3 = st.columns(3)
with h1:
    st.markdown("""
    ### 1. Read
    Pulls from Epic via FHIR:
    - MedicationRequest
    - AllergyIntolerance
    - Condition (Problem List)
    - Observation (Labs/Vitals)
    - ServiceRequest (Scheduled procedure)
    - DocumentReference (Notes)
    """)
with h2:
    st.markdown("""
    ### 2. Cross-Reference
    Engine logic:
    - Meds × Procedure type → hold/bridge plan
    - Allergies × Standard protocols → substitutions
    - History × Surgery risk → prophylaxis changes
    - Labs × Timing → readiness confirmation
    """)
with h3:
    st.markdown("""
    ### 3. Generate
    Outputs:
    - Protocol deviations (what's different for THIS patient)
    - Role-specific action lists
    - Day-of readiness tracker
    - Time-out script with patient-specific callouts
    """)

# =============================================
# SLIDE 5: EXAMPLE
# =============================================
st.markdown("""
<div class="slide">
    <h2>Real Example: What Gets Caught</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("""
**Patient:** Margaret Thompson, 70F, scheduled for Total Knee Arthroplasty

**What lives in separate Epic screens:**
- MAR: Warfarin 5mg daily (for AFib)
- Problem List: History of DVT (2019), Latex allergy, Type 2 DM on insulin
- Allergy List: Sulfonamide → Anaphylaxis
- Labs: INR 2.3, HbA1c 7.8%

**What our system synthesizes (that nobody else assembles automatically):**
""")

ex1, ex2 = st.columns(2)
with ex1:
    st.error("""
    **⚠️ CANNOT use standard antibiotic (cefazolin)**
    - Source: Sulfa allergy + Surgical prophylaxis protocol
    - Action: Vancomycin 1g IV instead
    - Why: Cephalosporin cross-reactivity risk with sulfa anaphylaxis
    """)
    st.warning("""
    **⚠️ Extended VTE prophylaxis required (4 weeks, not 2)**
    - Source: DVT history + Major joint surgery
    - Action: Enoxaparin extended protocol
    - Why: Recurrence risk 3x higher with standard duration
    """)
with ex2:
    st.warning("""
    **⚠️ Latex-free protocol for entire OR**
    - Source: Allergy list + OR setup
    - Action: Latex-free cart, all supplies verified
    - Why: Contact dermatitis → potential intra-op reaction
    """)
    st.info("""
    **ℹ️ Insulin dose adjustment perioperatively**
    - Source: MAR (Lantus 22u) + Endocrine consult
    - Action: Half dose night before, hold morning of
    - Why: Prevent perioperative hypoglycemia
    """)

st.markdown("""
> **None of these are individually hidden.** But assembling them requires reading 5 different
> modules and holding all the connections in your head — for every patient, every day.
> That's where things get dropped.
""")

# =============================================
# SLIDE 6: INTEGRATION
# =============================================
st.markdown("""
<div class="slide">
    <h2>Integration Strategy: Work WITH the EHR, Not Against It</h2>
</div>
""", unsafe_allow_html=True)

i1, i2 = st.columns(2)
with i1:
    st.markdown("""
    ### What We DON'T Do
    - ❌ Replace any Epic functionality
    - ❌ Create new documentation
    - ❌ Require new data entry
    - ❌ Store PHI outside the EHR
    - ❌ Modify the clinical record
    - ❌ Make clinical decisions
    """)
with i2:
    st.markdown("""
    ### What We DO
    - ✅ Launch as SMART on FHIR sidebar app
    - ✅ Read existing data (read-only access)
    - ✅ Generate actionable synthesis in real-time
    - ✅ Present role-specific views
    - ✅ Track readiness across modules
    - ✅ Integrate with Epic's existing workflow
    """)

st.markdown("""
**Technical integration path:**
1. Register as SMART on FHIR app (Epic App Orchard)
2. OAuth2 authorization — clinician launches from patient chart
3. Read FHIR resources (Patient, Condition, MedicationRequest, AllergyIntolerance, Observation, ServiceRequest)
4. Cross-reference against procedure protocols
5. Display synthesis in sidebar — clinician stays in Epic
""")

# =============================================
# SLIDE 7: MARKET & IMPACT
# =============================================
st.markdown("""
<div class="slide slide-dark">
    <h2>Impact & Market</h2>
</div>
""", unsafe_allow_html=True)

m1, m2, m3 = st.columns(3)
with m1:
    st.markdown("""
    <p class="big-number-white">$37B</p>
    <p style="color: #94a3b8;"><strong>Annual cost</strong> of surgical delays and cancellations in the US (Bain & Co, 2022)</p>
    """, unsafe_allow_html=True)
with m2:
    st.markdown("""
    <p class="big-number-white">3-5%</p>
    <p style="color: #94a3b8;"><strong>Day-of cancellation rate</strong> for elective surgeries — most due to prep failures</p>
    """, unsafe_allow_html=True)
with m3:
    st.markdown("""
    <p class="big-number-white">86%</p>
    <p style="color: #94a3b8;"><strong>of hospitals</strong> use Epic — and all have this synthesis gap</p>
    """, unsafe_allow_html=True)

st.markdown("""
**Target users:**
- Pre-op coordinators (save 20 min/patient × 15 patients/day = 5 hours/day)
- OR charge nurses (single readiness view vs. chart review)
- Anesthesiologists (relevant-only patient factors, not full chart)
- Surgeons (deviations from standard protocol highlighted)
""")

# =============================================
# SLIDE 8: ASK
# =============================================
st.markdown("""
<div class="slide slide-accent" style="text-align: center;">
    <h2 style="font-size: 2.5rem;">The Ask</h2>
    <br/>
    <p style="font-size: 1.2rem; color: #dbeafe;">
        We're not building a new EHR. We're building the <strong>intelligence layer</strong><br/>
        that sits on top of the data hospitals already have — and generates the synthesis<br/>
        that currently depends on human memory under stress.
    </p>
    <br/><br/>
    <p style="font-size: 1rem; color: #93c5fd;">
        Next step: Pilot with one surgical service line at one hospital.<br/>
        Measure: Pre-op coordinator time saved, day-of cancellation rate, and missed-item rate.
    </p>
</div>
""", unsafe_allow_html=True)

# =============================================
# APPENDIX
# =============================================
with st.expander("📎 Appendix: Technical Architecture"):
    st.markdown("""
    ```
    ┌─────────────────────────────────────────────────────────────┐
    │                    HOSPITAL NETWORK                          │
    │                                                             │
    │  ┌──────────┐     ┌────────────────┐     ┌─────────────┐  │
    │  │   Epic   │────▶│  FHIR Server   │────▶│ Manifesto   │  │
    │  │ Hyperspace│     │ (Interconnect) │     │ AI Engine   │  │
    │  └──────────┘     └────────────────┘     └──────┬──────┘  │
    │                                                  │         │
    │                                          ┌───────▼───────┐ │
    │                                          │  SMART App    │ │
    │                                          │  (in-browser) │ │
    │                                          └───────────────┘ │
    └─────────────────────────────────────────────────────────────┘
                              │
                    ┌─────────▼─────────┐
                    │ External APIs     │
                    │ (OpenFDA, RxNorm) │
                    │ Drug intelligence │
                    └───────────────────┘

    Data flow:
    1. Clinician opens patient chart in Epic
    2. Clicks "Manifesto AI" button (SMART launch)
    3. OAuth2 token grants read-only FHIR access
    4. Engine reads: Patient, Condition, MedicationRequest,
       AllergyIntolerance, Observation, ServiceRequest
    5. Cross-references against procedure protocol KB
    6. Optional: enriches with OpenFDA drug safety data
    7. Displays synthesis in Epic sidebar (iframe)
    8. NO data leaves hospital network (except optional FDA calls)
    ```
    """)

with st.expander("📎 Appendix: FHIR Resources Used"):
    st.markdown("""
    | FHIR Resource | Epic Module | What We Read |
    |---|---|---|
    | Patient | Demographics | Name, DOB, contacts, code status |
    | Condition | Problem List | Active diagnoses, ICD-10 codes |
    | MedicationRequest | MAR / Med List | Active meds, doses, prescribers |
    | AllergyIntolerance | Allergy List | Substances, reactions, severity |
    | Observation | Labs / Vitals | Recent results, vitals |
    | ServiceRequest | Orders / Scheduling | Scheduled procedure, pre-op orders |
    | DocumentReference | Notes | Consult notes, nursing assessments |
    """)

with st.expander("📎 Appendix: Competitive Landscape"):
    st.markdown("""
    | Product | What It Does | Gap |
    |---|---|---|
    | Epic BPA Alerts | Single drug/allergy alerts | No cross-reference, 90%+ override rate |
    | Surgical Scheduling (Epic OpTime) | Schedules OR time, equipment | Doesn't read patient chart for deviations |
    | Anesthesia pre-op (Epic) | Documents anesthesia assessment | Doesn't synthesize for the anesthesiologist |
    | Nurse checklist tools | Generic checklists | Not patient-specific, not adaptive |
    | **Manifesto AI** | **Reads ALL modules, generates patient-specific synthesis** | **This is the gap** |
    """)
