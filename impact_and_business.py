"""
Manifesto AI — Clinical Impact & Business Case
Run with: streamlit run impact_and_business.py
"""
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="Manifesto AI — Impact & Business Case",
    page_icon="📈",
    layout="wide",
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    .block-container { padding-top: 1rem; max-width: 1300px; }
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    .section-header {
        background: linear-gradient(135deg, #1e293b, #334155);
        border-radius: 12px;
        padding: 1.5rem 2rem;
        color: white;
        margin: 1.5rem 0 1rem 0;
    }
    .section-header h2 { color: white; margin: 0; }
    .section-header p { color: #94a3b8; margin: 0.3rem 0 0 0; }

    .stat-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        height: 100%;
    }
    .stat-big { font-size: 3rem; font-weight: 800; margin: 0; }
    .stat-label { font-size: 0.85rem; color: #64748b; margin-top: 0.3rem; }
    .stat-red { color: #dc2626; }
    .stat-blue { color: #2563eb; }
    .stat-green { color: #16a34a; }
    .stat-orange { color: #ea580c; }

    .impact-row {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 1rem 1.5rem;
        margin: 0.5rem 0;
    }

    .quote-block {
        border-left: 4px solid #3b82f6;
        padding: 1rem 1.5rem;
        background: #eff6ff;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# =============================================
# HEADER
# =============================================
st.markdown("""
<div class="section-header">
    <h2>Manifesto AI — Clinical Impact & Business Case</h2>
    <p>Why this matters clinically, operationally, and financially</p>
</div>
""", unsafe_allow_html=True)

# =============================================
# SECTION 1: CLINICAL IMPACT
# =============================================
st.markdown("---")
st.markdown("## 🏥 Clinical Impact")

st.markdown("""
<div class="quote-block">
"We have accumulated stupendous know-how... yet avoidable failures continue at a rate
that is unacceptable. The volume and complexity of what we know has exceeded our
individual ability to deliver it correctly, safely, or reliably."
<br/><br/>— <strong>Atul Gawande</strong>, The Checklist Manifesto
</div>
""", unsafe_allow_html=True)

# Key clinical stats
st.markdown("### The Harm Numbers")

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown("""
    <div class="stat-card">
        <p class="stat-big stat-red">44-98K</p>
        <p class="stat-label">Deaths/year from preventable medical errors in US hospitals (IOM)</p>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="stat-card">
        <p class="stat-big stat-red">4.8%</p>
        <p class="stat-label">Surgical adverse events attributable to communication failures (WHO)</p>
    </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown("""
    <div class="stat-card">
        <p class="stat-big stat-orange">70%</p>
        <p class="stat-label">Of sentinel events have communication as root cause (Joint Commission)</p>
    </div>
    """, unsafe_allow_html=True)
with c4:
    st.markdown("""
    <div class="stat-card">
        <p class="stat-big stat-orange">90%+</p>
        <p class="stat-label">BPA alert override rate — clinicians ignore EHR pop-ups (JAMIA 2019)</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("### What Manifesto AI Prevents")

st.markdown("""
| Failure Mode | How It Happens Today | How Manifesto AI Prevents It |
|---|---|---|
| **Wrong antibiotic given** | Sulfa allergy in allergy list, but standard cefazolin auto-ordered | Cross-references allergy × standard protocol → flags substitution |
| **Bleeding crisis in OR** | Patient on Plavix (MAR), biopsy scheduled (Orders) — but nobody pulled hemostatic clips | Connects antiplatelet therapy × procedure type → adds backup equipment to checklist |
| **Day-of cancellation** | INR not rechecked after warfarin hold. Discovered at 6AM in pre-op holding. | Readiness tracker flags: "INR recheck needed morning-of" as gating item |
| **Post-op DVT/PE** | History of DVT buried in Problem List. Standard 2-week prophylaxis given instead of 4. | Reads Problem List × procedure risk → flags extended prophylaxis requirement |
| **Perioperative hypoglycemia** | Insulin patient NPO. Nobody adjusted the dose. | Reads insulin in MAR × NPO order → generates "reduce to half dose" action item |
| **Latex reaction in OR** | Allergy documented but latex-free cart not ordered | Reads allergy list → generates equipment/setup protocol change |
""")

# Clinical evidence for checklists
st.markdown("### Evidence Base: Surgical Checklists Work")

evidence_data = {
    "Study": [
        "WHO Safe Surgery Checklist (Haynes et al., NEJM 2009)",
        "Michigan Keystone ICU (Pronovost, NEJM 2006)",
        "Safe Surgery 2015 (South Carolina)",
        "Ontario Surgical Quality (Urbach et al., NEJM 2014)",
    ],
    "Intervention": [
        "19-item surgical checklist",
        "5-step central line checklist",
        "Comprehensive surgical checklist",
        "Surgical safety checklist implementation",
    ],
    "Result": [
        "36% reduction in complications, 47% reduction in mortality",
        "66% reduction in central-line infections (nearly to zero)",
        "22% reduction in surgical mortality",
        "Complications fell from 3.86% to 3.13%",
    ],
}
st.dataframe(evidence_data, use_container_width=True, hide_index=True)

st.markdown("""
<div class="quote-block">
<strong>Key insight:</strong> These studies used <em>static</em> checklists — the same items for every patient.
Manifesto AI generates <em>dynamic, patient-specific</em> checklists that include items triggered by
the individual patient's medications, allergies, and history. The delta should be even larger.
</div>
""", unsafe_allow_html=True)

# =============================================
# SECTION 2: OPERATIONAL IMPACT
# =============================================
st.markdown("---")
st.markdown("""
<div class="section-header">
    <h2>⚙️ Operational Impact</h2>
    <p>Time saved, cancellations prevented, workflow efficiency</p>
</div>
""", unsafe_allow_html=True)

o1, o2, o3 = st.columns(3)
with o1:
    st.markdown("""
    <div class="stat-card">
        <p class="stat-big stat-blue">20 min</p>
        <p class="stat-label">Saved per patient for pre-op coordinators (chart review → auto-synthesis)</p>
    </div>
    """, unsafe_allow_html=True)
with o2:
    st.markdown("""
    <div class="stat-card">
        <p class="stat-big stat-blue">3-5%</p>
        <p class="stat-label">Day-of surgical cancellation rate (target: reduce by 50%+)</p>
    </div>
    """, unsafe_allow_html=True)
with o3:
    st.markdown("""
    <div class="stat-card">
        <p class="stat-big stat-blue">5 hrs</p>
        <p class="stat-label">Coordinator time reclaimed daily (20 min × 15 patients)</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("### Time Savings Model")

# Time savings chart
roles = ["Pre-Op Coordinator", "Pre-Op Nurse", "Anesthesiologist", "Surgeon", "OR Charge Nurse"]
time_before = [20, 12, 8, 5, 15]  # minutes per patient
time_after = [5, 4, 3, 2, 5]

fig = go.Figure()
fig.add_trace(go.Bar(name="Before (min/patient)", x=roles, y=time_before, marker_color="#ef4444"))
fig.add_trace(go.Bar(name="After (min/patient)", x=roles, y=time_after, marker_color="#22c55e"))
fig.update_layout(
    barmode="group",
    title="Time Spent on Pre-Op Chart Review & Synthesis",
    yaxis_title="Minutes per patient",
    height=350,
    margin=dict(l=40, r=40, t=60, b=40),
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("### Cancellation Prevention")

st.markdown("""
**Top reasons for day-of surgical cancellations (preventable by better pre-op coordination):**

| Reason | % of Cancellations | Can Manifesto Prevent? | How? |
|---|---|---|---|
| Incomplete pre-op workup | 28% | ✅ Yes | Readiness tracker flags missing items days before |
| NPO violation | 15% | ✅ Yes | Patient prep instructions generated with timing |
| Medication not held | 12% | ✅ Yes | Med hold orders surfaced prominently with dates |
| Missing consult/clearance | 11% | ✅ Yes | Consult status tracked in readiness view |
| No escort/driver | 8% | ✅ Yes | Escort confirmation as gating checklist item |
| Abnormal labs not addressed | 7% | ✅ Yes | Abnormal labs flagged with action thresholds |
| Patient refusal/no-show | 12% | ❌ No | Patient decision — not a coordination failure |
| Equipment unavailable | 7% | ✅ Partially | Patient-specific equipment flagged early |

**Total addressable: ~81% of day-of cancellations have coordination as a root cause.**
""")

# =============================================
# SECTION 3: BUSINESS CASE
# =============================================
st.markdown("---")
st.markdown("""
<div class="section-header">
    <h2>💰 Business Case</h2>
    <p>Revenue recovery, cost avoidance, and market opportunity</p>
</div>
""", unsafe_allow_html=True)

# Financial model
st.markdown("### Financial Impact Per Hospital")

st.markdown("#### Cost of a Single Surgical Cancellation")

fc1, fc2, fc3 = st.columns(3)
with fc1:
    st.metric("OR Time Wasted", "$62/min × 45 min = $2,790", help="Average OR minute cost including staff, overhead")
with fc2:
    st.metric("Staff Idle Cost", "~$1,500", help="Surgeon, anesthesiologist, nurses, techs standing idle")
with fc3:
    st.metric("Revenue Lost", "$5,000–$50,000", help="Depends on procedure. Joint replacement ~$30K, endoscopy ~$5K")

st.markdown("#### Annual Impact Model (Mid-Size Hospital: 10,000 surgeries/year)")

# Interactive model
st.markdown("**Adjust assumptions:**")
mod1, mod2, mod3 = st.columns(3)
with mod1:
    annual_surgeries = st.slider("Annual surgical volume", 3000, 30000, 10000, 1000)
with mod2:
    cancellation_rate = st.slider("Current cancellation rate (%)", 1.0, 8.0, 4.0, 0.5)
with mod3:
    reduction_target = st.slider("Target reduction (%)", 20, 70, 50, 5)

current_cancellations = int(annual_surgeries * cancellation_rate / 100)
prevented = int(current_cancellations * reduction_target / 100)
avg_revenue_per_case = 15000
revenue_recovered = prevented * avg_revenue_per_case
coord_time_saved_hours = (annual_surgeries * 15 / 60)  # 15 min saved per case
coord_fte_equivalent = coord_time_saved_hours / 2080

st.markdown("---")
r1, r2, r3, r4 = st.columns(4)
with r1:
    st.markdown(f"""
    <div class="stat-card">
        <p class="stat-big stat-red">{current_cancellations}</p>
        <p class="stat-label">Current annual cancellations</p>
    </div>
    """, unsafe_allow_html=True)
with r2:
    st.markdown(f"""
    <div class="stat-card">
        <p class="stat-big stat-green">{prevented}</p>
        <p class="stat-label">Cancellations prevented</p>
    </div>
    """, unsafe_allow_html=True)
with r3:
    st.markdown(f"""
    <div class="stat-card">
        <p class="stat-big stat-green">${revenue_recovered:,.0f}</p>
        <p class="stat-label">Revenue recovered annually</p>
    </div>
    """, unsafe_allow_html=True)
with r4:
    st.markdown(f"""
    <div class="stat-card">
        <p class="stat-big stat-blue">{coord_fte_equivalent:.1f}</p>
        <p class="stat-label">FTE equivalent time saved (coordinators)</p>
    </div>
    """, unsafe_allow_html=True)

# ROI visualization
st.markdown("### ROI Projection")

months = list(range(1, 13))
cumulative_savings = [revenue_recovered / 12 * m for m in months]
implementation_cost = 150000  # one-time
annual_license = 120000
cumulative_cost = [implementation_cost + (annual_license / 12 * m) for m in months]
net_value = [s - c for s, c in zip(cumulative_savings, cumulative_cost)]

fig = go.Figure()
fig.add_trace(go.Scatter(x=months, y=cumulative_savings, name="Cumulative Savings", line=dict(color="#22c55e", width=3)))
fig.add_trace(go.Scatter(x=months, y=cumulative_cost, name="Cumulative Cost", line=dict(color="#ef4444", width=3)))
fig.add_trace(go.Scatter(x=months, y=net_value, name="Net Value", line=dict(color="#3b82f6", width=2, dash="dash")))
fig.add_hline(y=0, line_dash="dot", line_color="gray")
fig.update_layout(
    title="12-Month ROI Projection",
    xaxis_title="Month",
    yaxis_title="Dollars ($)",
    height=350,
    margin=dict(l=40, r=40, t=60, b=40),
)
st.plotly_chart(fig, use_container_width=True)

# Breakeven
breakeven_month = None
for m, nv in zip(months, net_value):
    if nv >= 0:
        breakeven_month = m
        break

if breakeven_month:
    st.success(f"**Breakeven: Month {breakeven_month}** — system pays for itself in {breakeven_month} months")

# =============================================
# SECTION 4: MARKET OPPORTUNITY
# =============================================
st.markdown("---")
st.markdown("""
<div class="section-header">
    <h2>📊 Market Opportunity</h2>
    <p>TAM, SAM, SOM — and why the timing is right</p>
</div>
""", unsafe_allow_html=True)

mkt1, mkt2, mkt3 = st.columns(3)
with mkt1:
    st.markdown("""
    <div class="stat-card">
        <p class="stat-big stat-blue">$37B</p>
        <p class="stat-label"><strong>TAM</strong> — Annual cost of surgical inefficiency in US (delays, cancellations, complications)</p>
    </div>
    """, unsafe_allow_html=True)
with mkt2:
    st.markdown("""
    <div class="stat-card">
        <p class="stat-big stat-blue">$4.2B</p>
        <p class="stat-label"><strong>SAM</strong> — Perioperative software market (Fortune Business Insights 2024)</p>
    </div>
    """, unsafe_allow_html=True)
with mkt3:
    st.markdown("""
    <div class="stat-card">
        <p class="stat-big stat-blue">$180M</p>
        <p class="stat-label"><strong>SOM</strong> — 1,500 hospitals × $120K/year license (first 5 years)</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
### Why Now?

| Factor | Implication |
|---|---|
| **21st Century Cures Act (2021)** | Hospitals MUST expose FHIR APIs — no more information blocking. Integration is now legally mandated. |
| **Epic App Orchard maturity** | SMART on FHIR ecosystem is production-ready. 500+ apps already deployed this way. |
| **Alert fatigue crisis** | 90%+ BPA override rate means the current approach (pop-up alerts) has failed. Hospitals are looking for alternatives. |
| **Staffing shortage** | Nursing shortage means less time per patient for chart review. Automation of synthesis is no longer nice-to-have. |
| **Value-based care shift** | Payers penalizing complications and readmissions. Preventing one surgical complication saves $20-50K+ in downstream costs. |
""")

# =============================================
# SECTION 5: GO-TO-MARKET
# =============================================
st.markdown("---")
st.markdown("""
<div class="section-header">
    <h2>🚀 Go-to-Market Strategy</h2>
    <p>How we get from hackathon to hospitals</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
### Phase 1: Prove (Months 1-6)
- **Single hospital pilot** — one surgical service line (e.g., orthopedics or GI)
- **Metrics:** Coordinator time saved, cancellation rate delta, missed-item rate
- **Target:** 2-3 champion users (pre-op coordinator + OR charge nurse)
- **Cost to hospital:** Free pilot

### Phase 2: Validate (Months 6-12)
- **Expand to 2-3 service lines** at pilot hospital
- **Publish results** — time savings, cancellation reduction, near-miss prevention
- **Begin Epic App Orchard submission** process
- **Pricing model validated:** Per-OR-suite/month or per-case

### Phase 3: Scale (Year 2+)
- **Epic App Orchard listing** — available to all Epic hospitals
- **Sales through Epic's channel** — they actively promote high-value third-party apps
- **Expand to Cerner/Oracle Health** via same FHIR integration
- **Add specialties:** cardiac surgery, neurosurgery, transplant (highest complexity = highest value)

### Pricing Model
| Tier | Target | Price | Includes |
|---|---|---|---|
| **Starter** | Community hospital (5-10 ORs) | $8K/month | Up to 3 service lines, standard protocols |
| **Enterprise** | Academic medical center (20+ ORs) | $20K/month | Unlimited service lines, custom protocols, analytics |
| **Per-Case** | ASC / outpatient surgery center | $15/case | Pay-per-use, no commitment |
""")

# =============================================
# SECTION 6: COMPETITIVE ADVANTAGE
# =============================================
st.markdown("---")
st.markdown("""
<div class="section-header">
    <h2>🛡️ Defensibility</h2>
    <p>Why can't Epic just build this?</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
### The "Can't Epic Just Do This?" Question

**Short answer:** They could. They probably will eventually. But:

| Factor | Reality |
|---|---|
| **Epic's release cycle** | 3-year roadmap. Even if prioritized today, it's 2028+ before production. |
| **Epic's incentive** | They sell modules. A synthesis layer that REDUCES clicks is not aligned with their per-module billing model. |
| **Specialization** | Epic builds for 100% of workflows. We build for the specific pre-op synthesis gap. Depth > breadth. |
| **Iteration speed** | We can ship weekly. Epic ships quarterly at best. Clinical protocols change faster than Epic updates. |
| **Protocol maintenance** | We can update clinical protocols (drug interactions, guidelines) in real-time. Epic's CDS knowledge base updates lag months. |

### Real Moat: Clinical Intelligence Layer
- **Procedure protocol database** — curated, maintained, specialty-specific
- **Cross-reference rules engine** — the logic that connects meds × procedures × patient history
- **Workflow data** — we learn which items get missed most, which roles need what information
- **Network effects** — every hospital using us improves the protocol database for all

### Who's Tried and Failed?
| Company | What They Did | Why They Failed |
|---|---|---|
| Surgical checklist apps (various) | Static digital checklists | Not patient-specific. Same list for everyone = no value over paper. |
| CDS vendors (Zynx, Elsevier) | Evidence-based order sets | Embedded in Epic. Don't synthesize across modules. Still require manual interpretation. |
| OR management tools (Caselink, etc.) | Scheduling, block time, turnover | Operational focus. Don't read the patient chart. |

**Our differentiation: We read the FULL chart and generate patient-specific synthesis. Nobody else does this as a standalone, role-specific pre-op intelligence product.**
""")

# =============================================
# SECTION 7: THE ASK
# =============================================
st.markdown("---")
st.markdown("""
<div class="section-header" style="background: linear-gradient(135deg, #1e40af, #3b82f6);">
    <h2>The Ask</h2>
    <p>What we need to go from demo to deployed</p>
</div>
""", unsafe_allow_html=True)

a1, a2 = st.columns(2)
with a1:
    st.markdown("""
    ### Immediate Next Steps
    1. **Hospital partner** — one surgical service willing to pilot
    2. **Epic sandbox access** — to build against real FHIR endpoint
    3. **Clinical advisory board** — 2-3 surgeons + 2 pre-op coordinators
    4. **6 months runway** — to prove the time-savings and cancellation metrics

    ### Success Metrics (Pilot)
    - ≥50% reduction in coordinator chart-review time
    - ≥30% reduction in day-of cancellations
    - Zero missed high-alert medication interactions
    - NPS ≥ 70 from clinical users
    """)
with a2:
    st.markdown("""
    ### Why We Win
    - **No new documentation burden** — read-only from EHR
    - **Launches inside Epic** — no new login, no new system to learn
    - **Immediate ROI** — time savings measurable within 30 days
    - **Clinical safety floor** — prevents the errors that harm patients AND cost money
    - **Federally mandated interop** — FHIR access can't be blocked (Cures Act)

    ### What We're NOT
    - ❌ Not an EHR replacement
    - ❌ Not a clinical decision support tool (we don't prescribe)
    - ❌ Not adding documentation burden
    - ❌ Not competing with Epic for contracts
    - ✅ We're a value-add layer that makes existing data work harder
    """)

st.markdown("---")
st.caption("Manifesto AI — Pre-Procedure Intelligence. Reducing errors of inaptitude, one synthesis at a time.")
