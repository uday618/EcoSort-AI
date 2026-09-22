import streamlit as st

st.set_page_config(
    page_title="EcoSort AI",
    page_icon="♻️",
    layout="centered"
)

st.title("♻️ EcoSort AI")
st.subheader("Smart Waste Segregation Assistant")
st.write("AI-powered guidance for responsible waste management.")
st.info("SDG 12 – Responsible Consumption and Production")

waste_data = {
    "banana": ("Wet / Organic Waste", "🍌",
               "Place it in the wet/organic waste bin or compost it where available."),
    "food": ("Wet / Organic Waste", "🥗",
             "Place food waste in the wet/organic waste stream."),
    "vegetable": ("Wet / Organic Waste", "🥬",
                  "Vegetable scraps can generally go into organic/compostable waste."),
    "plastic bottle": ("Dry / Recyclable Waste", "♻️",
                       "Empty the bottle and place it in the appropriate recyclable waste stream."),
    "paper": ("Dry / Recyclable Waste", "📄",
              "Keep paper clean and dry and place it in the recyclable waste stream."),
    "cardboard": ("Dry / Recyclable Waste", "📦",
                  "Flatten clean cardboard and place it in the recyclable waste stream."),
    "mobile": ("E-Waste", "📱",
               "Do not put a mobile phone in regular waste. Use an authorized e-waste collection point."),
    "laptop": ("E-Waste", "💻",
               "Dispose of laptops through an authorized e-waste recycling channel."),
    "charger": ("E-Waste", "🔌",
                "Old chargers should be handled through an appropriate e-waste collection system."),
    "battery": ("Hazardous / E-Waste", "⚠️",
                "Do not put batteries in regular household waste. Use an authorized battery/e-waste collection point."),
    "glass": ("Glass Waste", "🫙",
              "Use your local glass/recycling collection system. Handle broken glass carefully.")
}

item = st.text_input(
    "Enter a waste item",
    placeholder="Example: plastic bottle, banana peel, old mobile phone"
)

if st.button("🔍 Analyze Waste"):
    if not item.strip():
        st.warning("Please enter a waste item.")
    else:
        text = item.lower()
        result = None

        for keyword, data in waste_data.items():
            if keyword in text:
                result = data
                break

        if result:
            category, icon, recommendation = result

            st.success(f"{icon} Category: {category}")

            st.markdown("### Recommended Action")
            st.write(recommendation)

            st.markdown("### 🌱 Environmental Impact")
            st.write(
                "Correct segregation can improve recycling, reduce contamination "
                "of waste streams, and encourage responsible waste management."
            )

            if "battery" in text or "mobile" in text:
                st.warning(
                    "Safety: Do not burn, puncture, crush, or dismantle batteries "
                    "or electronic devices. Follow local disposal guidelines."
                )
        else:
            st.info(
                "I could not confidently classify this item. "
                "Please describe it in more detail and check your local "
                "waste-management guidelines."
            )

st.divider()

st.markdown("### 🤖 AI Workflow")
st.write(
    "User Input → Natural Language Analysis → Waste Classification → "
    "Disposal Recommendation → Sustainability Guidance"
)

st.markdown("### Responsible AI")
st.write(
    "The system avoids unnecessary personal data, provides safety guidance, "
    "handles uncertain inputs, and reminds users that local waste rules may differ."
)

st.caption("EcoSort AI | AI for Sustainability | SDG 12")
