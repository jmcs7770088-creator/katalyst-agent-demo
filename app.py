import streamlit as st
import math

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
    if not text:
        return False
    return len(text.strip()) > 5

def katalyst_agent(query, drift):
    omega = establish_stillness_floor(drift)
    response = f"Katalyst processed: {query}"
    valid = verify_output(response)

    return omega, response, valid

# ========================
# UI
# ========================

st.title("⚡ Katalyst Stability Agent")

query = st.text_input("Enter your query")
noise = st.slider("Stochastic Noise", -1000.0, 1000.0, 0.0)

if st.button("Run Agent"):
    omega, response, valid = katalyst_agent(query, noise)

    st.write("### Results")
    st.write("Response:", response)
    st.write("Ω_G:", omega)
    st.write("Status:", "STABLE" if valid else "REJECTED")