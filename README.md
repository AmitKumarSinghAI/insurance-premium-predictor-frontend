# 💰 Insurance Premium Predictor (FastAPI + Streamlit)

## 🚀 Overview
This is a **Machine Learning–powered Insurance Premium Prediction System** that predicts the **insurance premium category** of a person based on factors such as age, weight, height, income, smoking habits, city, and occupation.

It’s built with:
- 🧠 **FastAPI** → Backend & ML model hosting  
- 🎨 **Streamlit** → Frontend UI  
- ⚙️ **Scikit-Learn** → Model training and prediction  

---

## 🌐 Live Links
- **Backend (FastAPI):** [https://insurance-premium-predictor-fastapi.onrender.com](https://insurance-premium-predictor-fastapi.onrender.com)
- **Frontend (Streamlit):** *Coming soon after deployment*

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | Streamlit |
| **Backend** | FastAPI |
| **Model** | Scikit-Learn |
| **Language** | Python |
| **Deployment** | Render |

---

## 📦 Features
✅ Predicts user’s insurance premium category  
✅ Sends user data to backend via API  
✅ Displays prediction results in real time  
✅ User-friendly interface with sidebar navigation  
✅ Fully deployed using Render  

---

## 🧠 Input Parameters

| Parameter | Description |
|------------|-------------|
| `age` | Age of the person |
| `weight` | Weight in kilograms |
| `height` | Height in meters |
| `income_lpa` | Annual income (LPA) |
| `smoker` | True or False |
| `city` | City name |
| `occupation` | Type of occupation |

---

## ⚙️ How It Works
1. The user enters their details in the **Streamlit frontend**.  
2. Data is sent to the **FastAPI backend** via a REST API request.  
3. The backend loads a **trained ML model** to predict the **premium category**.  
4. The prediction result is displayed instantly in the UI.  

---

## 🧾 Folder Structure
```
📁 Insurance-Premium-Predictor
│
├── 📁 backend
│   ├── app.py
│   ├── model.pkl
│   ├── requirements.txt
│   ├── Procfile
│
├── 📁 frontend
│   ├── app.py
│   ├── requirements.txt
│   ├── Procfile
│
├── README.md
```

---

## ⚙️ Local Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/AmitKumarSinghAI/insurance-premium-predictor-fastapi.git
cd insurance-premium-predictor-fastapi
```

### 2️⃣ Create and Activate Virtual Environment
```bash
python -m venv .venv
.\.venv\Scriptsctivate   # for Windows
source .venv/bin/activate  # for macOS/Linux
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Backend (FastAPI)
```bash
uvicorn app:app --reload
```

Then open: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 5️⃣ Run Frontend (Streamlit)
```bash
streamlit run app.py
```

Then open: [http://localhost:8501](http://localhost:8501)

---

## 🚀 Deployment Guide

### 🔹 Deploy Backend (FastAPI)
1. Push backend code to GitHub.  
2. Go to [Render.com](https://render.com).  
3. Create a **New Web Service** → connect your GitHub repo.  
4. In “Start Command,” write:
   ```
   uvicorn app:app --host 0.0.0.0 --port 10000
   ```

### 🔹 Deploy Frontend (Streamlit)
1. Push Streamlit UI code to GitHub.  
2. Create another **Web Service** on Render.  
3. In “Start Command,” write:
   ```
   streamlit run app.py --server.port 10000 --server.address 0.0.0.0
   ```

---

## 👨‍💻 Developer Info

**Name:** Amit Kumar Singh Kurmi  
**University:** Kalinga University  
**Goal:** Building complete ML → GenAI project pipelines  
**GitHub:** [https://github.com/Amit905460](https://github.com/Amit905460)

---

## 🏁 Future Improvements
- Add user authentication  
- Display analytics dashboard  
- Improve model accuracy using ensemble techniques  
- Connect MongoDB Atlas for real-time cloud storage  

---

⭐ **If you like this project, give it a star on GitHub!** 🌟
