import streamlit as st
import requests

# ------------------------------------------------------------
# 🌐 FastAPI backend URL
# ------------------------------------------------------------
API_URL = "https://insurance-premium-predictor-fastapi.onrender.com"

# ------------------------------------------------------------
# 🏠 Page Configuration
# ------------------------------------------------------------
st.set_page_config(
    page_title="Insurance Premium Predictor 🏠",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------------------
# 🧭 Sidebar Navigation
# ------------------------------------------------------------
st.sidebar.title("🏠 Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Predict", "About"])

# ------------------------------------------------------------
# 🏠 Home Page
# ------------------------------------------------------------
if page == "Home":
    st.title("💰 Insurance Premium Prediction App")

    st.markdown("""
    Welcome to the **Insurance Premium Prediction System**!  
    💡 This app helps you estimate your **insurance premium category** based on your:
    - 🧍 Age  
    - ⚖️ Weight  
    - 📏 Height  
    - 💰 Annual Income  
    - 🚬 Smoking habits  
    - 🏙️ City  
    - 💼 Occupation  

    🧠 The model is powered by **Machine Learning (FastAPI backend)**  
    and the UI is built using **Streamlit** 🚀  
    """)

    st.success("👈 Use the sidebar to go to the Prediction page!")

# ------------------------------------------------------------
# 🔮 Prediction Page
# ------------------------------------------------------------
elif page == "Predict":
    st.title("🔮 Predict Your Insurance Premium Category")
    st.write("Please enter your details below:")

    with st.form(key="prediction_form"):
        col1, col2 = st.columns(2)

        with col1:
            age = st.number_input("👤 Age", min_value=1, max_value=120, step=1)
            weight = st.number_input("⚖️ Weight (kg)", min_value=5.0)
            height = st.number_input("📏 Height (m)", min_value=0.5)
            income = st.number_input("💰 Annual Income (LPA)", min_value=0.0)

        with col2:
            smoker = st.selectbox("🚬 Are you a smoker?", [True, False])
            city = st.text_input("🏙️ City")
            occupation = st.selectbox(
                "💼 Occupation",
                [
                    "retired", "freelancer", "student", "government_job",
                    "business_owner", "unemployed", "private_job"
                ]
            )

        submit_button = st.form_submit_button(label="✨ Predict")

    # ------------------------------------------------------------
    # 🧠 Prediction Logic
    # ------------------------------------------------------------
    if submit_button:
        user_data = {
            "age": age,
            "weight": weight,
            "height": height,
            "income_lpa": income,
            "smoker": smoker,
            "city": city,
            "occupation": occupation
        }

        st.info("📦 Sending data to FastAPI backend... Please wait.")
        try:
            response = requests.post(API_URL, json=user_data)
            if response.status_code == 200:
                result = response.json().get("predicted_category", "Unknown")
                st.success(f"✅ Predicted Insurance Category: **{result}**")
            else:
                st.error(f"❌ Prediction failed. (Status Code: {response.status_code})")
        except Exception as e:
            st.error(f"⚠️ Could not connect to API: {e}")

# ------------------------------------------------------------
# ℹ️ About Page
# ------------------------------------------------------------
elif page == "About":
    st.title("ℹ️ About the Project")

    st.markdown("""
    ### 🧩 Tech Stack:
    - **Backend:** FastAPI  
    - **Frontend:** Streamlit  
    - **Database:** MongoDB  
    - **Model:** Scikit-Learn  

    ### 🚀 Features:
    - Collects user data  
    - Automatically calculates BMI, lifestyle risk, and age group  
    - Predicts the insurance premium category  
    - Stores predictions in MongoDB  

    ---
    👨‍💻 **Developed by:** Amit Kumar Singh Kurmi  
    🎓 **University:** Kalinga University  
    🎯 **Goal:** Building complete ML → GenAI project pipelines  
    """)

    st.info("Thank you for exploring this project! 🚀")
