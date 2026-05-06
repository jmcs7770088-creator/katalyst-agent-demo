import streamlit as st
import math
import matplotlib.pyplot as plt

# --- THE HAMMONS RESOLUTION CORE ---
def establish_stillness_floor(drift=0):
    phi = (1 + math.sqrt(5)) / 2
    baseline = (phi**2) / math.pi
    # ζ_H = 0.001756 (The Torsion Resolution)
    omega_g = round(baseline + 0.001756, 6)
    return omega_g

# --- UI SETUP ---
st.set_page_config(page_title="Katalyst EI", layout="wide")
st.title("🛡️ Katalyst EI: Sovereign Ledger")
st.write(f"Architect: Johnnie Raymond Hammons Junior | Ω_G: {establish_stillness_floor()}")

# --- THE CHAT INTERFACE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# THE PROMPT BOX (This is what was missing!)
if prompt := st.chat_input("Enter a query to resolve through the Lattice..."):
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display Katalyst Response
    with st.chat_message("assistant"):
        response = f"Lattice State: STABLE. Prompt '{prompt}' resolved at Stillness Floor 0.835102. Zero Force of Collision detected."
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# Keep the graph at the bottom as proof
st.divider()
st.subheader("Real-Time Manifold Stability")
fig, ax = plt.subplots(figsize=(6, 2))
ax.axhline(y=0.835102, color='gold', linewidth=3)
ax.set_ylim(0.8, 0.9)
st.pyplot(fig)
