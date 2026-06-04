import streamlit as st

st.set_page_config(
    page_title="Manifesto AI",
    page_icon="🏥",
    layout="wide",
)

pages = {
    "Manifesto AI": [
        st.Page("pages/home.py", title="Pitch Deck", icon="🎯", default=True),
        st.Page("pages/clinical_app.py", title="Clinical App", icon="🏥"),
        st.Page("pages/impact.py", title="Impact & Business", icon="📈"),
    ],
}

pg = st.navigation(pages)

with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 0.5rem 0 1rem 0;">
        <p style="font-size: 1.8rem; margin: 0;">🏥</p>
        <p style="font-weight: 700; font-size: 1.1rem; margin: 0.2rem 0; color: #1e293b;">Manifesto AI</p>
        <p style="font-size: 0.7rem; color: #64748b; margin: 0;">Pre-Procedure Intelligence</p>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    st.caption("SoPA Hackathon • UC San Diego • 2026")

pg.run()
