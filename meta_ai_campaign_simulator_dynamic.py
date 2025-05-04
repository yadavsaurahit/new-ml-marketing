
import streamlit as st
import random

st.set_page_config(page_title="Dynamic Meta AI Campaign Simulator", layout="centered")

st.title("📣 Dynamic Meta AI-Powered Campaign Simulator")
st.markdown("Personalise your Meta ad creative based on dynamic audience profiles.")

st.sidebar.header("🎯 Audience Targeting")
age_range = st.sidebar.slider("Age Range", 18, 65, (25, 40))
gender = st.sidebar.selectbox("Gender", ["All", "Male", "Female", "Other"])
interests = st.sidebar.multiselect("Interests", ["Fitness", "Technology", "Fashion", "Travel", "Food", "Finance"])
location = st.sidebar.text_input("Location", "New York")

# Determine dynamic creative type
if "Fashion" in interests or "Lifestyle" in interests:
    creative_type = "Lifestyle"
elif "Technology" in interests:
    creative_type = "Product"
elif "Finance" in interests:
    creative_type = "Testimonial"
else:
    creative_type = random.choice(["Lifestyle", "Product", "Testimonial"])

# Suggest dynamic headline and description
headline_options = {
    "Lifestyle": "Transform Your Daily Routine with Smart Choices",
    "Product": "Unlock the Power of Innovation in Your Pocket",
    "Testimonial": "See What Customers Are Saying About Us"
}

desc_options = {
    "Lifestyle": "Bring convenience and style together with a personalised touch.",
    "Product": "The latest in tech, tailored to your lifestyle and budget.",
    "Testimonial": "Real stories, real results. Discover how we’re changing lives."
}

headline = headline_options.get(creative_type, "Your Personalised Experience Awaits")
description = desc_options.get(creative_type, "Experience AI that adapts to your every need.")

st.header("📊 Simulation Output")
if st.button("Run AI Simulation"):
    reach = random.randint(10000, 75000)
    ctr = round(random.uniform(1.2, 4.8), 2)
    conversion_rate = round(random.uniform(0.6, 3.8), 2)
    cpc = round(random.uniform(0.25, 1.75), 2)

    st.subheader("🎥 Ad Preview")
    st.markdown(f"**Creative Type:** {creative_type}")
    st.image(f"{creative_type.lower()}.jpg", caption=creative_type, use_column_width=True)
    st.markdown(f"**Headline:** {headline}")
    st.markdown(f"**Description:** {description}")

    st.subheader("📈 AI-Driven Campaign Results")
    st.metric("Estimated Reach", f"{reach:,}")
    st.metric("Click Through Rate (CTR)", f"{ctr}%")
    st.metric("Conversion Rate", f"{conversion_rate}%")
    st.metric("Cost Per Click (CPC)", f"${cpc}")

st.markdown("---")
st.markdown("This version dynamically adjusts the ad creative based on selected interests.")
