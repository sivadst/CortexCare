import streamlit as st

from utils.why_engine import generate_reason
from utils.recommend import recommend

st.set_page_config(page_title="CortexCare AI", layout="centered")

st.title("🧠 CortexCare")
st.caption("Understand your stress. Take control.")

# Temporary model (we’ll replace later)
# For now simulate prediction
def fake_model(data):
    score = 0
    if data["sleep_hours"] < 6:
        score += 2
    if data["screen_time"] > 6:
        score += 2
    if data["peer_pressure"] > 7:
        score += 2

    if score >= 4:
        return "HIGH"
    elif score >= 2:
        return "MEDIUM"
    else:
        return "LOW"

# Inputs
sleep = st.slider("Sleep Hours", 0, 10)
screen = st.slider("Screen Time (hrs)", 0, 12)
peer = st.slider("Peer Pressure (0–10)", 0, 10)
gpa = st.slider("GPA", 0.0, 10.0)

if st.button("Analyze Stress"):

    input_data = {
        "sleep_hours": sleep,
        "screen_time": screen,
        "peer_pressure": peer,
        "gpa": gpa
    }

    # Prediction
    prediction = fake_model(input_data)

    st.subheader(f"Stress Level: {prediction}")

    # WHY
    reasons = generate_reason(input_data)
    st.write("### Why are you stressed?")
    for r in reasons:
        st.write(f"- {r}")

    # RECOMMENDATION
    tips = recommend(input_data)
    st.write("### What should you do tonight?")
    for t in tips:
        st.write(f"👉 {t}")

    # TREND GRAPH
    st.write("### Stress Trend (Last 7 Days)")
    trend = [2, 3, 4, 3, 5, 6, len(reasons)]
    st.line_chart(trend)
