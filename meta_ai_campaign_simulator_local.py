
import streamlit as st
import random

st.set_page_config(page_title="Meta AI Campaign Simulator", layout="centered")

st.title("📣 Meta AI-Powered Campaign Simulator")
st.markdown("Simulate real-time AI-powered personalisation for Meta Ads.")

st.sidebar.header("🎯 Audience Targeting")
age_range = st.sidebar.slider("Age Range", 18, 65, (25, 45))
gender = st.sidebar.selectbox("Gender", ["All", "Male", "Female", "Other"])
interests = st.sidebar.multiselect("Interests", ["Fitness", "Technology", "Fashion", "Travel", "Food", "Finance"])
location = st.sidebar.text_input("Location", "New York")

st.sidebar.header("🖼️ Ad Creative")
creative_type = st.sidebar.selectbox("Creative Type", ["Lifestyle", "Product", "Testimonial"])
headline = st.sidebar.text_input("Ad Headline", "Discover the Future of Personalisation")
description = st.sidebar.text_area("Ad Description", "Experience AI that tailors every touchpoint to your audience.")

st.header("📊 Simulation Output")
if st.button("Run AI Simulation"):
    reach = random.randint(5000, 50000)
    ctr = round(random.uniform(1.0, 5.0), 2)
    conversion_rate = round(random.uniform(0.5, 3.5), 2)
    cpc = round(random.uniform(0.3, 2.0), 2)

    st.subheader("🎥 Ad Preview")
    st.markdown(f"**Headline:** {headline}")
    st.markdown(f"**Description:** {description}")
    image_file = f"{creative_type.lower()}.jpg"
    st.image(image_file, caption=creative_type, use_column_width=True)

    st.subheader("📈 AI-Driven Campaign Results")
    st.metric("Estimated Reach", f"{reach:,}")
    st.metric("Click Through Rate (CTR)", f"{ctr}%")
    st.metric("Conversion Rate", f"{conversion_rate}%")
    st.metric("Cost Per Click (CPC)", f"${cpc}")

st.markdown("---")
st.markdown("Upload local image files named `lifestyle.jpg`, `product.jpg`, and `testimonial.jpg` in the same directory for ad previews.")
