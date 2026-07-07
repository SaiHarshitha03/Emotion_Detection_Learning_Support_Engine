# 🧠 AI Emotion Detection & Learning Support Engine

An AI-powered Emotion Detection and Learning Support platform that analyzes user emotions from text and provides personalized learning recommendations, motivation, emotion insights, analytics, and prediction history.

---

## 🚀 Live Demo

### 🌐 Streamlit App
https://emotiondetectionlearningsupportengine-zb9zsrstpkslbx47szovkt.streamlit.app/

### ⚡ FastAPI Backend
https://emotion-detection-learning-support-engine.onrender.com

### 📚 API Documentation
https://emotion-detection-learning-support-engine.onrender.com/docs

---

# 📖 Overview

The AI Emotion Detection & Learning Support Engine uses Machine Learning and Natural Language Processing (NLP) to detect emotions from user text.

The platform predicts emotions such as:

- 😊 Joy
- 😢 Sadness
- 😠 Anger
- 😨 Fear
- ❤️ Love
- 😲 Surprise

Based on the detected emotion, the system provides:

- Personalized Learning Recommendations
- Motivation
- Emotion Insights
- Confidence Scores
- Analytics Dashboard
- Prediction History

---

# ✨ Features

## 🎭 Emotion Detection
- Detect emotions from text
- Confidence percentage
- Secondary emotion prediction
- Mixed emotion detection

## 💡 AI Learning Support
- Personalized study recommendations
- Emotion-based learning guidance
- Smart suggestions

## ❤️ Motivation
- Encouraging motivational messages
- Personalized support

## 🧠 Emotion Insight
- Understand emotional state
- Helpful mental wellness insights

## 📊 Analytics Dashboard
- Emotion distribution
- Prediction statistics
- Interactive visualizations using Plotly

## 📜 History
- Stores recent predictions
- Displays previously detected emotions

## 🌐 REST API
- FastAPI backend
- Interactive Swagger Documentation

---

# 🏗️ Project Architecture

```
User
   │
   ▼
Streamlit Frontend
   │
   ▼
FastAPI Backend
   │
   ▼
Machine Learning Model
(Logistic Regression)
   │
   ▼
Prediction
   │
   ▼
Recommendations + Motivation + Insights
```

---

# 🛠 Tech Stack

## Frontend
- Streamlit

## Backend
- FastAPI
- Uvicorn

## Machine Learning
- Scikit-learn
- Logistic Regression

## NLP
- TF-IDF Vectorizer
- GoEmotions Dataset

## Visualization
- Plotly
- Matplotlib

## Programming Language
- Python

---

# 📂 Project Structure

```
Emotion_Detection_Learning_Support_Engine/

├── api/
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── prediction/
│   ├── predict.py
│   └── __init__.py
│
├── recommendation/
│   └── recommender.py
│
├── analytics/
│   └── dashboard.py
│
├── models/
│   ├── logistic/
│   └── bilstm/
│
├── history/
│
├── assets/
│
├── data/
│
├── requirements.txt
│
└── README.md
```

---

# 📊 Dataset

**GoEmotions Dataset**

Developed by Google Research.

Contains over **58,000** carefully labeled Reddit comments with **27 emotions**.

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/SaiHarshitha03/Emotion_Detection_Learning_Support_Engine.git
```

Move into the project

```bash
cd Emotion_Detection_Learning_Support_Engine
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run FastAPI Backend

```bash
uvicorn api.main:app --reload
```

Backend:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Streamlit Frontend

```bash
streamlit run frontend/app.py
```

---

# 📸 Screenshots

Add screenshots of:

- Home Page
- Emotion Detection
- Analytics Dashboard
- Prediction History
- Swagger API

---

# 📈 Future Improvements

- User Authentication
- Database Integration
- Deep Learning Models (BERT/LSTM)
- Voice Emotion Detection
- Multi-language Support
- Emotion Trend Analysis
- Chatbot Integration

---

# 👩‍💻 Author

**Adapa Sai Harshitha**

B.Tech – Artificial Intelligence & Data Science

Vishnu Institute of Technology

GitHub:
https://github.com/SaiHarshitha03

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

It motivates future improvements and helps others discover the project.

---

## 📜 License

This project is licensed under the MIT License.
