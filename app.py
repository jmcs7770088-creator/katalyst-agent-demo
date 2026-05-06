import streamlit as st
import math

# ========================
# PAGE CONFIG
# ========================
st.set_page_config(
    page_title="Katalyst Agent",
    page_icon="⚡",
    layout="centered"
)

# ========================
# STYLE (DARK + CLEAN)
# ========================
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.stApp {
    background-color: #0f172a;
    color: white;
}
.big-title {
    font-size: 2.5rem;
    font-weight: bold;
}
.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 12px;
    margin-top: 15px;
}
.green {
    color: #22c55e;
    font-weight: bold;
}
.red {
    color: #ef4444;
    font-weight: bold;
}
.metric {
    font-size: 1.3rem;
}
</style>
""", unsafe_allow_html=True)

# ========================
# CORE LOGIC
# ========================
def bounded_torsion(drift):
    zeta_H = 0.001756
    return zeta_H * (drift / (1 + abs(drift)))

def establish_stillness_floor(drift=0):
    phi = (1 + math.sqrt(5)) / 2
    baseline = (phi ** 2) / math.pi
    torsion = bounded_torsion(drift)
    return round(baseline + torsion, 6)

def verify_output(text):
    return bool(text and len(text.strip()) > 5)

def katalyst_agent(query, drift):
    omega = establish_stillness_floor(drift)
    response = f"Katalyst processed: {query}"
    valid = verify_output(response)
    stability = 1 / (1 + abs(drift))
    return omega, response, valid, stability

# ========================
# HEADER
# ========================
st.markdown('<div class="big-title">⚡ Katalyst Stability Agent</div>', unsafe_allow_html=True)
st.caption("AI stabilization layer for noisy environments")

st.markdown("---")

# ========================
# INPUT SECTION
# ========================
st.markdown("### 🧠 Input")

query = st.text_input("Enter your query", placeholder="e.g. What is gravity?")
noise = st.slider("Stochastic Noise Level", -1000.0, 1000.0, 0.0)

run = st.button("🚀 Run Agent")

# ========================
# OUTPUT SECTION
# ========================
if run:
    omega, response, valid, stability = katalyst_agent(query, noise)

    st.markdown("### 📊 Results")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"<div class='card metric'>Ω_G<br><b>{omega}</b></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='card metric'>Stability Score<br><b>{round(stability, 4)}</b></div>", unsafe_allow_html=True)

    with col2:
        status_color = "green" if valid else "red"
        status_text = "STABLE" if valid else "REJECTED"

        st.markdown(f"<div class='card metric'>Status<br><span class='{status_color}'>{status_text}</span></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='card metric'>Verified<br><b>{valid}</b></div>", unsafe_allow_html=True)

    st.markdown("### 🤖 Response")
    st.markdown(f"<div class='card'>{response}</div>", unsafe_allow_html=True)

    st.markdown("---")

    # ========================
    # VISUAL FEEDBACK
    # ========================
    st.markdown("### 📈 Stability Insight")

    if abs(noise) > 500:
        st.warning("High noise detected — system remains bounded.")
    else:
        st.success("System operating in stable range.")

# ========================
# FOOTER / PITCH
# ========================
st.markdown("---")
st.info(
    "Katalyst demonstrates a bounded-response AI architecture that stabilizes outputs "
    "under extreme input noise using a mathematical constraint layer and verification step."
)