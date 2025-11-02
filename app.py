import streamlit as st
import requests

# ------------------------------------------------------------
# 🌐 FastAPI backend URL
# ------------------------------------------------------------

API_URL = "https://insurance-premium-predictor-fastapi-yyy4.onrender.com/predict"



# ------------------------------------------------------------
# 🎨 Streamlit UI Setup
# ------------------------------------------------------------
st.set_page_config(page_title="Insurance Premium Predictor", page_icon="💰", layout="centered")

st.title("💰 Insurance Premium Prediction App")
st.markdown("### Fill in your details below to get your insurance premium category prediction.")

# ------------------------------------------------------------
# 🧾 User Input Form
# ------------------------------------------------------------
with st.form("insurance_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=1, max_value=120, value=30, step=1)
        weight = st.number_input("Weight (kg)", min_value=10, max_value=300, value=65, step=1)

        # ✅ FIX: use text_input for float values to preserve exact decimal entered
        height_str = st.text_input("Height (in meters, e.g. 1.72)", "1.70")
        income_str = st.text_input("Annual Income (in LPA, e.g. 5.5)", "6.0")

    with col2:
        smoker = st.radio("Are you a smoker?", ["No", "Yes"])
        city = st.text_input("City", placeholder="e.g. Mumbai, Jaipur, etc.")
        occupation = st.selectbox(
            "Occupation",
            [
                "retired",
                "freelancer",
                "student",
                "government_job",
                "business_owner",
                "unemployed",
                "private_job",
            ],
        )

    submitted = st.form_submit_button("🔍 Predict Premium")

# ------------------------------------------------------------
# 📤 Send Data to FastAPI Backend
# ------------------------------------------------------------
if submitted:
    if not city.strip():
        st.warning("⚠️ Please enter your city.")
    else:
        try:
            # ✅ Convert safely to float
            height = float(height_str.replace(",", "."))
            income_lpa = float(income_str.replace(",", "."))

            payload = {
                "age": int(age),
                "weight": int(weight),
                "height": height,
                "income_lpa": income_lpa,
                "smoker": True if smoker == "Yes" else False,
                "city": city.strip(),
                "occupation": occupation,
            }

            response = requests.post(API_URL, json=payload)

            if response.status_code == 200:
                result = response.json()
                st.success(f"🏆 Predicted Insurance Premium Category: **{result['predicted_category']}**")
            else:
                st.error(f"❌ Error {response.status_code}: {response.text}")

        except ValueError:
            st.error("❌ Please enter valid numeric values for height and income (e.g. 1.70, 6.5).")
        except requests.exceptions.ConnectionError:
            st.error("🚫 Cannot connect to backend. Make sure FastAPI is running on 127.0.0.1:8000.")
