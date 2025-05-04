
import streamlit as st
import random
import time

st.set_page_config(page_title="Meta AI Campaign Simulator", layout="wide")

st.title("📱 Meta AI-Powered Campaign Simulator")
st.markdown("Simulate AI-personalised ad campaigns on Meta platforms using target audience inputs and ad creatives.")

# Sidebar for customer profile inputs
st.sidebar.header("🎯 Audience Targeting")
age_range = st.sidebar.slider("Age Range", 18, 65, (25, 40))
gender = st.sidebar.multiselect("Gender", ["Male", "Female", "Non-Binary"], default=["Male", "Female"])
interests = st.sidebar.multiselect(
    "Interests",
    ["Fitness", "Fashion", "Tech", "Parenting", "Finance", "Gaming", "Travel", "Food"],
    default=["Tech", "Travel"]
)
location = st.sidebar.selectbox("Location", ["North America", "Europe", "Asia", "Latin America", "Middle East", "Africa"])

# Image creatives and ad copy selection
st.header("🖼️ Select Ad Creatives & Messaging")
col1, col2 = st.columns(2)

with col1:
    creative_type = st.selectbox("Choose Ad Creative Style", ["Lifestyle Image", "Product Close-up", "User Testimonial"])
    st.image(f"https://placehold.co/300x200?text={creative_type.replace(' ', '+')}", caption=f"{creative_type}")

with col2:
    ad_copy = st.selectbox("Select Ad Headline", [
        "Upgrade your lifestyle with AI-powered tech",
        "Explore destinations tailored for you",
        "Discover smarter ways to save and invest",
        "Your next favourite look is here!"
    ])
    st.text_area("Ad Description", value="Experience a new way of shopping with recommendations just for you.")

# Simulation button
st.markdown("---")
if st.button("🚀 Run Campaign Simulation"):
    with st.spinner("Generating AI campaign results..."):
        time.sleep(2)

    st.header("📊 AI Campaign Outcome Simulation")

    reach = random.randint(20000, 100000)
    ctr = round(random.uniform(1.2, 4.5), 2)
    conv_rate = round(random.uniform(0.8, 3.0), 2)
    cost_per_result = round(random.uniform(0.20, 1.50), 2)

    st.metric("Estimated Reach", f"{reach:,} users")
    st.metric("Click-Through Rate (CTR)", f"{ctr}%")
    st.metric("Conversion Rate", f"{conv_rate}%")
    st.metric("Cost per Result", f"${cost_per_result}")

    st.success("✅ Simulation Complete")

st.markdown("---")
st.caption("This simulator provides a mock representation of how Meta AI might optimise ad targeting and creative performance.")
