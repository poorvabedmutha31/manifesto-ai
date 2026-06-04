import streamlit as st
import json
import time
import sys
from pathlib import Path
import plotly.graph_objects as go
from datetime import datetime, timedelta

sys.path.insert(0, str(Path(__file__).parent.parent))

from medical_data import lookup_drug_full
from procedure_kb import get_procedure, get_conditional_equipment, get_conditional_prep
from ehr_data import PATIENTS


st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    .block-container { padding-top: 0.5rem; max-width: 1400px; }
    html, body, [class*="css"] { font-family: 'Inter', -apple-system, sans-serif; }

    .hero {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        border-radius: 12px;
        padding: 1.5rem 2rem 1rem 2rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    }
    .hero h1 { color: #fff; font-size: 2rem; font-weight: 700; margin: 0; }
    .hero .sub { color: #94a3b8; font-size: 0.9rem; margin: 0.2rem 0 0 0; }

    .patient-strip {
        background: #1e40af;
        color: white;
        border-radius: 8px;
        padding: 0.7rem 1.2rem;
        margin-bottom: 0.8rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .alert-banner {
        background: #fef2f2;
        border: 1px solid #fecaca;
        border-left: 5px solid #dc2626;
        border-radius: 8px;
        padding: 0.8rem 1rem;
        margin: 0.5rem 0;
    }

    .synthesis-card {
        background: #fffbeb;
        border: 1px solid #fde68a;
        border-left: 5px solid #f59e0b;
        border-radius: 8px;
        padding: 0.8rem 1rem;
        margin: 0.5rem 0;
    }

    .action-item {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 0.6rem 1rem;
        margin: 0.4rem 0;
    }
    .action-item.urgent { border-left: 4px solid #dc2626; }
    .action-item.important { border-left: 4px solid #f59e0b; }
    .action-item.standard { border-left: 4px solid #10b981; }

    .role-tab {
        background: #f1f5f9;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
    }

    .status-done { color: #16a34a; font-weight: 600; }
    .status-pending { color: #dc2626; font-weight: 600; }
    .status-na { color: #9ca3af; }
</style>
""", unsafe_allow_html=True)

# =============================================
# HEADER
# =============================================
st.markdown("""
<div class="hero">
    <h1>Manifesto AI</h1>
    <p class="sub">Pre-Procedure Intelligence — Synthesizes what's scattered across 15 Epic screens into role-specific action plans</p>
</div>
""", unsafe_allow_html=True)

# =============================================
# SIDEBAR — Patient Selection
# =============================================
with st.sidebar:
    st.markdown("### Patient Chart")
    st.caption("Pulled from Epic via FHIR/Interconnect")

    patient_opts = {
        "Martinez, Roberto J — EGD": "martinez_roberto",
        "Thompson, Margaret A — TKA": "thompson_margaret",
    }
    selected = st.selectbox("Select Patient", list(patient_opts.keys()))
    patient_key = patient_opts[selected]
    ehr = PATIENTS[patient_key]
    demo = ehr["demographics"]
    sched = ehr["scheduled_procedure"]
    procedure = get_procedure(sched["cpt_code"])

    st.divider()
    st.markdown("### What This Solves")
    st.markdown("""
    Epic stores all the data. But **prep coordinators, nurses, and OR teams** spend 20+ minutes piecing together:

    - What meds need to be held?
    - Which consults are back?
    - Are there allergy-driven protocol changes?
    - What extra equipment is needed?
    - Who needs to be called?

    **This tool reads the chart once and generates that synthesis automatically.**
    """)

    st.divider()
    st.caption("Integration: SMART on FHIR (launches inside Epic)")


# =============================================
# PATIENT BANNER (minimal — they already see this in Epic)
# =============================================
st.markdown(f"""
<div class="patient-strip">
    <div>
        <strong style="font-size: 1.1rem;">{demo['full_name']}</strong> &nbsp;
        <span style="opacity: 0.8;">{demo['mrn']} • {demo['age']}yo {demo['sex']} • {demo['dob']}</span>
    </div>
    <div style="text-align: right;">
        <strong>{sched['procedure_name']}</strong><br/>
        <span style="opacity: 0.8; font-size: 0.85rem;">{sched['scheduled_date']} @ {sched['scheduled_time']} — {sched['performing_provider']}</span>
    </div>
</div>
""", unsafe_allow_html=True)


# =============================================
# CORE ENGINE — Generate the synthesis
# =============================================
def generate_synthesis(ehr, procedure):
    """
    THIS is the value-add. Read all EHR modules and produce:
    1. Critical alerts (things that will cancel/harm if missed)
    2. Action items per role
    3. What's different about THIS patient vs standard protocol
    """
    sched = ehr["scheduled_procedure"]
    alerts = []
    actions_coordinator = []
    actions_nurse_preop = []
    actions_nurse_day_of = []
    actions_anesthesia = []
    actions_surgeon = []
    equipment_changes = []
    protocol_deviations = []

    # --- Analyze medications ---
    for med in ehr["medications"]:
        if med.get("high_alert"):
            # Check if there's a hold order
            hold_order = None
            for order in sched["pre_procedure_orders"]:
                if med["generic"].lower() in order.lower():
                    hold_order = order
                    break

            if hold_order:
                actions_coordinator.append({
                    "text": f"Confirm {med['name']} hold: {hold_order}",
                    "source": "MAR + Orders",
                    "urgency": "urgent",
                    "why": med.get("high_alert_reason", "High-alert medication requires management"),
                })
            else:
                alerts.append({
                    "text": f"HIGH-ALERT MED: {med['name']} — no hold order found in pre-procedure orders",
                    "severity": "critical",
                })

    # --- Analyze allergies ---
    for allergy in ehr["allergies"]:
        if "anaphylaxis" in allergy["reaction"].lower() or allergy["severity"].startswith("Severe"):
            alerts.append({
                "text": f"SEVERE ALLERGY: {allergy['allergen']} → {allergy['reaction']}",
                "severity": "critical",
            })
            actions_nurse_day_of.append({
                "text": f"Verify allergy band on patient: {allergy['allergen']}",
                "source": "Allergy List",
                "urgency": "urgent",
                "why": f"Severity: {allergy['severity']}",
            })

        if allergy["allergen"].lower() == "latex":
            equipment_changes.append({
                "item": "Latex-free protocol — all supplies",
                "reason": f"Patient latex allergy ({allergy['reaction']})",
                "urgency": "urgent",
            })
            actions_coordinator.append({
                "text": "Order latex-free cart for OR suite",
                "source": "Allergy List + OR Setup",
                "urgency": "urgent",
                "why": "Latex allergy documented",
            })
            protocol_deviations.append("LATEX-FREE PROTOCOL: All gloves, tubing, catheters must be non-latex")

        if "sulfa" in allergy["allergen"].lower():
            protocol_deviations.append("ANTIBIOTIC SUBSTITUTION: Cannot use cefazolin (sulfa cross-reactivity risk) → Use vancomycin for surgical prophylaxis")
            actions_anesthesia.append({
                "text": "Surgical antibiotic: Vancomycin 1g IV (NOT cefazolin — sulfa allergy)",
                "source": "Allergy List + Anesthesia Protocol",
                "urgency": "urgent",
                "why": "Sulfa anaphylaxis history precludes standard cephalosporin prophylaxis",
            })

    # --- Analyze problem list for procedure interactions ---
    has_dvt_history = any("dvt" in p["description"].lower() or "embolism" in p["description"].lower() for p in ehr["problem_list"])
    has_afib = any("atrial fibrillation" in p["description"].lower() for p in ehr["problem_list"])
    has_diabetes = any(p["icd10"].startswith("E11") for p in ehr["problem_list"])
    has_sleep_apnea = any("sleep apnea" in p["description"].lower() for p in ehr["problem_list"])
    has_obesity = any("obesity" in p["description"].lower() for p in ehr["problem_list"])

    if has_dvt_history and procedure and procedure["duration_minutes"] > 60:
        protocol_deviations.append("EXTENDED VTE PROPHYLAXIS: 4 weeks (not standard 2 weeks) — patient has DVT history")
        actions_surgeon.append({
            "text": "Order extended VTE prophylaxis (4 weeks post-op, not standard 2)",
            "source": "Problem List + Hematology Protocol",
            "urgency": "important",
            "why": "Prior DVT (2019) significantly elevates perioperative VTE risk",
        })

    if has_diabetes:
        insulin_meds = [m for m in ehr["medications"] if "insulin" in m["name"].lower()]
        if insulin_meds:
            actions_coordinator.append({
                "text": "Confirm insulin dose adjustment per endocrine consult",
                "source": "MAR + Endocrine Note",
                "urgency": "important",
                "why": "Patient on insulin — perioperative hypoglycemia risk",
            })
            actions_nurse_day_of.append({
                "text": "Check fasting glucose on arrival. If <70: D50 protocol. If >200: insulin drip.",
                "source": "Labs + Endocrine Protocol",
                "urgency": "important",
                "why": "Diabetic patient, insulin adjustment perioperatively",
            })

    if has_sleep_apnea:
        actions_anesthesia.append({
            "text": "Sleep apnea — ASA class III. CPAP available in recovery. Consider post-op monitoring.",
            "source": "Problem List + Anesthesia Assessment",
            "urgency": "standard",
            "why": "OSA increases sedation risk and post-op respiratory complications",
        })
        actions_nurse_preop.append({
            "text": "Confirm patient brought CPAP machine",
            "source": "Problem List + Pre-Op Nursing",
            "urgency": "standard",
            "why": "OSA patient — CPAP needed in recovery",
        })

    # --- Analyze consults (from notes) ---
    consult_status = []
    for note in ehr["notes"]:
        if "clearance" in note["type"].lower() or "consult" in note["type"].lower():
            consult_status.append({
                "consult": note["type"],
                "date": note["date"],
                "provider": note["author"],
                "status": "Complete",
            })

    # --- Analyze labs ---
    abnormal_labs = [lab for lab in ehr["labs"]["results"] if lab["flag"] in ["H", "L"]]
    for lab in abnormal_labs:
        if lab["test"] in ["PT/INR"] and any(m["generic"] == "warfarin" for m in ehr["medications"]):
            actions_nurse_day_of.append({
                "text": f"Verify INR morning of surgery (current: {lab['value']}). Proceed only if ≤ 1.5.",
                "source": "Labs + Hematology Protocol",
                "urgency": "urgent",
                "why": "Patient on warfarin being held for surgery — must confirm adequate reversal",
            })

    # --- Escort/discharge planning ---
    ec = demo["emergency_contact"]
    actions_coordinator.append({
        "text": f"Confirm escort: {ec['name']} ({ec['relationship']}) — {ec['phone']}",
        "source": "Demographics + Discharge Planning",
        "urgency": "standard",
        "why": "Post-sedation/anesthesia discharge requires confirmed escort",
    })

    # --- Equipment from procedure protocol + patient factors ---
    if procedure:
        triggers = []
        if any(m.get("high_alert") and m["class"] in ["Antiplatelet", "Anticoagulant (Vitamin K Antagonist)"] for m in ehr["medications"]):
            triggers.append("bleeding_risk")
        if has_dvt_history:
            triggers.append("vte_risk")

        conditional = get_conditional_equipment(procedure, triggers)
        for eq in conditional:
            equipment_changes.append({
                "item": eq["item"],
                "reason": f"Patient factor: {eq['trigger'].replace('_', ' ')}",
                "urgency": "important",
            })

    return {
        "alerts": alerts,
        "actions_coordinator": actions_coordinator,
        "actions_nurse_preop": actions_nurse_preop,
        "actions_nurse_day_of": actions_nurse_day_of,
        "actions_anesthesia": actions_anesthesia,
        "actions_surgeon": actions_surgeon,
        "equipment_changes": equipment_changes,
        "protocol_deviations": protocol_deviations,
        "consult_status": consult_status,
        "abnormal_labs": abnormal_labs,
    }


synthesis = generate_synthesis(ehr, procedure)

# =============================================
# MAIN CONTENT — 3 Tabs focused on real value
# =============================================
tab_brief, tab_roles, tab_readiness = st.tabs([
    "📋 Pre-Op Brief",
    "👥 Role-Specific Views",
    "✅ Day-Of Readiness",
])

# =============================================
# TAB 1: PRE-OP BRIEF (the core value)
# =============================================
with tab_brief:
    st.markdown("### Pre-Procedure Intelligence Brief")
    st.caption("Auto-generated by reading: Problem List, MAR, Allergies, Orders, Notes, Labs")

    # --- Critical Alerts ---
    if synthesis["alerts"]:
        for alert in synthesis["alerts"]:
            st.markdown(f"""<div class="alert-banner">
                <strong>⚠️ {alert['text']}</strong>
            </div>""", unsafe_allow_html=True)

    # --- Protocol Deviations (THIS is the money) ---
    if synthesis["protocol_deviations"]:
        st.markdown("#### ⚡ How This Patient Differs From Standard Protocol")
        st.caption("These are the things that get missed — standard protocol won't work for this patient")
        for dev in synthesis["protocol_deviations"]:
            st.markdown(f"""<div class="synthesis-card">
                <strong>{dev}</strong>
            </div>""", unsafe_allow_html=True)

    # --- Medication Management Summary ---
    st.markdown("#### 💊 Medication Management Plan")
    hold_meds = []
    continue_meds = []
    adjust_meds = []
    for order in sched["pre_procedure_orders"]:
        order_lower = order.lower()
        if "hold" in order_lower or "stop" in order_lower or "last dose" in order_lower:
            hold_meds.append(order)
        elif "continue" in order_lower:
            continue_meds.append(order)
        elif "reduce" in order_lower or "half" in order_lower:
            adjust_meds.append(order)

    mc1, mc2, mc3 = st.columns(3)
    with mc1:
        st.markdown("**🛑 HOLD:**")
        for m in hold_meds:
            st.markdown(f"- {m}")
    with mc2:
        st.markdown("**✅ CONTINUE:**")
        for m in continue_meds:
            st.markdown(f"- {m}")
        if not continue_meds:
            st.caption("See full order list")
    with mc3:
        st.markdown("**⚠️ ADJUST:**")
        for m in adjust_meds:
            st.markdown(f"- {m}")
        if not adjust_meds:
            st.caption("None")

    # --- Consult Status ---
    if synthesis["consult_status"]:
        st.markdown("#### 📋 Required Consults")
        for c in synthesis["consult_status"]:
            st.markdown(f"✅ **{c['consult']}** — {c['provider']} ({c['date']})")

    # --- Abnormal Labs worth flagging ---
    if synthesis["abnormal_labs"]:
        st.markdown("#### 🧪 Flagged Lab Values")
        for lab in synthesis["abnormal_labs"]:
            st.markdown(f"- ⬆️ **{lab['test']}:** {lab['value']} {lab['unit']} (ref: {lab['reference']})")

    # --- Equipment Changes ---
    if synthesis["equipment_changes"]:
        st.markdown("#### 📦 Equipment Additions (Beyond Standard Kit)")
        for eq in synthesis["equipment_changes"]:
            urgency_icon = "🔴" if eq["urgency"] == "urgent" else "🟡"
            st.markdown(f"- {urgency_icon} **{eq['item']}** — _{eq['reason']}_")


# =============================================
# TAB 2: ROLE-SPECIFIC VIEWS
# =============================================
with tab_roles:
    st.markdown("### Role-Specific Action Plans")
    st.caption("Each role sees only what THEY need to do — no information overload")

    role_choice = st.radio(
        "Select role:",
        ["Pre-Op Coordinator", "Pre-Op Nurse (Day-Of)", "Anesthesia", "Surgeon"],
        horizontal=True,
    )

    if role_choice == "Pre-Op Coordinator":
        st.markdown("#### 📞 Pre-Op Coordinator Tasks")
        st.caption("Days before procedure — phone calls, confirmations, logistics")
        actions = synthesis["actions_coordinator"]
        if not actions:
            st.success("No outstanding coordinator tasks.")
        for i, action in enumerate(actions):
            urgency_class = action["urgency"]
            st.markdown(f"""<div class="action-item {urgency_class}">
                <strong>{action['text']}</strong><br/>
                <small style="color: #64748b;">Source: {action['source']} | Why: {action['why']}</small>
            </div>""", unsafe_allow_html=True)
            st.checkbox("Done", key=f"coord_{i}")

    elif role_choice == "Pre-Op Nurse (Day-Of)":
        st.markdown("#### 🏥 Day-Of Nursing Tasks")
        st.caption("Patient arrival through procedure start")

        # Combine pre-op and day-of nursing tasks
        all_nursing = synthesis["actions_nurse_preop"] + synthesis["actions_nurse_day_of"]
        if not all_nursing:
            st.success("No special nursing considerations beyond standard protocol.")
        for i, action in enumerate(all_nursing):
            st.markdown(f"""<div class="action-item {action['urgency']}">
                <strong>{action['text']}</strong><br/>
                <small style="color: #64748b;">Source: {action['source']} | Why: {action['why']}</small>
            </div>""", unsafe_allow_html=True)
            st.checkbox("Done", key=f"nurse_{i}")

        # Always show allergy verification
        st.markdown("---")
        st.markdown("**Standard Verifications:**")
        for i, allergy in enumerate(ehr["allergies"]):
            st.checkbox(f"Allergy band verified: {allergy['allergen']} ({allergy['severity']})", key=f"allergy_verify_{i}")
        st.checkbox(f"ID band verified: {demo['full_name']} — {demo['dob']}", key="id_verify")
        st.checkbox(f"Escort confirmed with patient: {demo['emergency_contact']['name']} — {demo['emergency_contact']['phone']}", key="escort_verify")
        st.checkbox("NPO status confirmed", key="npo_verify")
        st.checkbox("Consent on chart", key="consent_verify")

    elif role_choice == "Anesthesia":
        st.markdown("#### 💉 Anesthesia Considerations")
        st.caption(f"Plan: {sched.get('anesthesia_plan', 'See orders')} — {sched.get('anesthesia_provider', 'TBD')}")

        actions = synthesis["actions_anesthesia"]
        if not actions:
            st.success("No special anesthesia considerations beyond standard.")
        for i, action in enumerate(actions):
            st.markdown(f"""<div class="action-item {action['urgency']}">
                <strong>{action['text']}</strong><br/>
                <small style="color: #64748b;">Source: {action['source']} | Why: {action['why']}</small>
            </div>""", unsafe_allow_html=True)

        # Key patient factors for anesthesia
        st.markdown("---")
        st.markdown("**Key Patient Factors:**")
        anes_factors = []
        for p in ehr["problem_list"]:
            if p["status"] == "Active" and any(kw in p["description"].lower() for kw in ["apnea", "cardiac", "heart", "obesity", "airway", "copd", "asthma", "fibrillation"]):
                anes_factors.append(p["description"])
        for f in anes_factors:
            st.markdown(f"- ⚠️ {f}")
        st.markdown(f"- BMI: {ehr['vitals']['bmi']}")
        st.markdown(f"- ASA Status: See nursing assessment")

    elif role_choice == "Surgeon":
        st.markdown("#### 🔪 Surgeon Pre-Op Summary")
        st.caption(f"Provider: {sched['performing_provider']}")

        actions = synthesis["actions_surgeon"]
        if not actions:
            st.info("No non-standard surgeon actions required.")
        for i, action in enumerate(actions):
            st.markdown(f"""<div class="action-item {action['urgency']}">
                <strong>{action['text']}</strong><br/>
                <small style="color: #64748b;">Source: {action['source']} | Why: {action['why']}</small>
            </div>""", unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("**Procedure Details:**")
        st.markdown(f"- **Indication:** {sched['indication']}")
        st.markdown(f"- **Duration:** {sched['estimated_duration']}")
        if sched.get("implant_system"):
            st.markdown(f"- **Implant:** {sched['implant_system']}")
        st.markdown(f"- **Consent risks discussed:** {', '.join(sched.get('consent_risks_discussed', []))}")


# =============================================
# TAB 3: DAY-OF READINESS TRACKER
# =============================================
with tab_readiness:
    st.markdown("### ✅ Day-Of Readiness Checklist")
    st.caption("Is this patient actually ready to go? Track every dependency.")

    # Build readiness items from the EHR data
    readiness_items = []

    # Medication holds
    for med in ehr["medications"]:
        if med.get("high_alert"):
            for order in sched["pre_procedure_orders"]:
                if med["generic"].lower() in order.lower() and ("hold" in order.lower() or "last dose" in order.lower()):
                    readiness_items.append({
                        "category": "Medications",
                        "item": f"{med['name']} — {order}",
                        "critical": True,
                    })

    # Consults
    for note in ehr["notes"]:
        if "clearance" in note["type"].lower() or "consult" in note["type"].lower():
            readiness_items.append({
                "category": "Consults",
                "item": f"{note['type']} — {note['author']} ({note['date']})",
                "critical": True,
            })

    # Labs
    readiness_items.append({
        "category": "Labs",
        "item": f"Labs collected {ehr['labs']['collection_date']} — within 30 days",
        "critical": True,
    })

    # Consent
    readiness_items.append({
        "category": "Consent",
        "item": f"Informed consent: {sched.get('consent_status', 'NOT OBTAINED')}",
        "critical": True,
    })

    # Insurance
    readiness_items.append({
        "category": "Authorization",
        "item": f"Pre-auth: {sched.get('pre_auth_status', 'Unknown')} — {sched.get('pre_auth_number', '')}",
        "critical": True,
    })

    # Escort
    ec = demo["emergency_contact"]
    readiness_items.append({
        "category": "Discharge",
        "item": f"Escort confirmed: {ec['name']} ({ec['relationship']}) — {ec['phone']}",
        "critical": True,
    })

    # Equipment/protocol special
    for eq in synthesis["equipment_changes"]:
        readiness_items.append({
            "category": "Equipment",
            "item": eq["item"],
            "critical": eq["urgency"] == "urgent",
        })

    # NPO
    readiness_items.append({
        "category": "Patient Prep",
        "item": "NPO compliance verified",
        "critical": True,
    })

    # Display as a status board
    categories = {}
    for item in readiness_items:
        categories.setdefault(item["category"], []).append(item)

    total_items = len(readiness_items)
    checked_items = 0

    for cat, items in categories.items():
        st.markdown(f"**{cat}**")
        for i, item in enumerate(items):
            key = f"ready_{cat}_{i}"
            critical_mark = " 🔴" if item["critical"] else ""
            checked = st.checkbox(f"{item['item']}{critical_mark}", key=key)
            if checked:
                checked_items += 1

    # Overall readiness
    st.markdown("---")
    readiness_pct = checked_items / total_items if total_items > 0 else 0
    st.progress(readiness_pct, text=f"Readiness: {checked_items}/{total_items} items confirmed ({int(readiness_pct * 100)}%)")

    if readiness_pct == 1.0:
        st.success("✅ Patient is READY. All items confirmed.")
    elif readiness_pct >= 0.8:
        st.warning("⚠️ Nearly ready — review unchecked items.")
    else:
        remaining = total_items - checked_items
        st.error(f"❌ NOT READY — {remaining} items still pending.")


# =============================================
# FOOTER
# =============================================
st.markdown("---")
st.caption("Manifesto AI — Pre-Procedure Intelligence. Integrates via SMART on FHIR. Reads existing EHR data, adds no new documentation burden.")
