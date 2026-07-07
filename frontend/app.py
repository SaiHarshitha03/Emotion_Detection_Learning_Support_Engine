import os
import sys
import requests
import streamlit as st
import plotly.graph_objects as go

# ==========================
# Project Path
# ==========================

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from prediction.predict import get_learning_recommendation
from analytics.dashboard import show_dashboard

# ==========================
# Page Config
# ==========================

st.set_page_config(
    page_title="AI Emotion Learning Assistant",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================
# Premium CSS
# ==========================

st.markdown("""
<style>

#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

.stApp{
background:linear-gradient(135deg,#0f172a,#111827,#1e293b);
color:white;
}

/* Sidebar */

section[data-testid="stSidebar"]{
background:#111827;
border-right:1px solid #2d3748;
}

/* Hero */

.hero{
padding:35px;
border-radius:25px;
background:rgba(255,255,255,.08);
backdrop-filter:blur(18px);
box-shadow:0 10px 30px rgba(0,0,0,.35);
margin-bottom:30px;
animation:fade .7s ease;
}

@keyframes fade{
from{opacity:0;transform:translateY(25px);}
to{opacity:1;transform:translateY(0);}
}

/* Cards */

.card{
padding:25px;
background:rgba(255,255,255,.05);
border-radius:20px;
backdrop-filter:blur(18px);
box-shadow:0px 5px 20px rgba(0,0,0,.25);
margin-bottom:20px;
}

            .tech-card{
    background:#1e293b;
    border-radius:18px;
    padding:25px;
    text-align:center;
    transition:.3s;
    border:1px solid #334155;
}

.tech-card:hover{
    transform:translateY(-8px);
    box-shadow:0 10px 25px rgba(0,201,255,.35);
    border-color:#00c9ff;
}
/* Result */

.result{
padding:25px;
border-left:8px solid #00c9ff;
background:white;
color:black;
border-radius:18px;
}

/* Buttons */

.stButton>button{

width:100%;
height:55px;
border:none;
border-radius:15px;
font-size:18px;
font-weight:bold;

background:linear-gradient(90deg,#00C9FF,#92FE9D);

color:black;

transition:.3s;

}

.stButton>button:hover{

transform:scale(1.04);

box-shadow:0px 0px 18px #00c9ff;

}

/* Text Area */

textarea{

background:#111827!important;

color:white!important;

font-size:18px!important;

border-radius:15px!important;

}

</style>
""",unsafe_allow_html=True)

# ==========================
# Sidebar
# ==========================

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/4712/4712109.png",
        width=90
    )

    st.title("🧠 AI Workspace")

    st.success("🟢 Online")

    st.markdown("---")

    st.button("🏠 Home", use_container_width=True)
    st.button("🎭 Emotion Scan", use_container_width=True)
    st.button("📊 Analytics", use_container_width=True)
    st.button("📜 History", use_container_width=True)
    st.button("⚙️ Settings", use_container_width=True)

    st.markdown("---")

    # 👇 Move this INSIDE the sidebar
    st.markdown("""
    <div style="
    background:#1e293b;
    border:1px solid #334155;
    border-radius:18px;
    padding:18px;
    ">

    <h4 style="text-align:center;color:white;">
    Project Details
    </h4>

    <p style="color:#CBD5E1;">
    🤖 <b>Model</b><br>
    Logistic Regression
    </p>

    <p style="color:#CBD5E1;">
    📚 <b>Dataset</b><br>
    GoEmotions
    </p>

    <p style="color:#CBD5E1;">
    🚀 <b>Version</b><br>
    v2.0
    </p>

    </div>
    """, unsafe_allow_html=True)

    

    

# ==========================
# Hero
# ==========================

st.markdown("""

<div class="hero">

<h1 style="font-size:55px;">
🧠 AI Emotion Learning Assistant
</h1>

<h3 style="color:#CBD5E1;">

Understand emotions • Improve learning • Stay motivated

</h3>

</div>

""",unsafe_allow_html=True)

# ==========================
# Input Card
# ==========================

st.markdown("<div class='card'>",unsafe_allow_html=True)

text=st.text_area(

"💬 Tell me how you're feeling",

height=180,

placeholder="Example: I am excited but nervous about tomorrow's interview."

)

col1,col2=st.columns(2)

predict=col1.button("🚀 Analyze Emotion",use_container_width=True)

clear=col2.button("🗑 Clear",use_container_width=True)

st.markdown("</div>",unsafe_allow_html=True)

if clear:
    st.rerun()

emoji={
"joy":"😊",
"sadness":"😢",
"anger":"😠",
"fear":"😨",
"love":"❤️",
"surprise":"😲"
}

API_URL="http://127.0.0.1:8000/predict"
# ==========================================================
# PREDICTION
# ==========================================================

if predict:

    if text.strip() == "":
        st.warning("⚠ Please enter some text.")

    else:

        with st.spinner("🧠 AI is analyzing your emotion..."):

            try:

                response = requests.post(
                    API_URL,
                    json={"text": text},
                    timeout=30
                )

                if response.status_code == 200:

                    result = response.json()

                    primary = result["primary_emotion"].lower()
                    secondary = result["secondary_emotion"].lower()

                    primary_score = result["primary_confidence"]
                    secondary_score = result["secondary_confidence"]

                    mixed = result["mixed_emotion"]

                    confidence = result["confidence"]

                    recommendation = result["recommendation"]

                    motivation = result["motivation"]

                    insight = result["emotion_insight"]

                    icon = emoji.get(primary, "🙂")

                    st.success("🎉 Emotion detected successfully!")

                    col1, col2 = st.columns([2, 1])

                    with col1:

                        st.markdown(f"""
                        <div class="result">

                        <h1 style="font-size:50px;">
                        {icon} {primary.title()}
                        </h1>

                        <h3>Confidence : {primary_score:.2f}%</h3>

                        </div>
                        """, unsafe_allow_html=True)

                    with col2:

                        fig = go.Figure(go.Indicator(

                            mode="gauge+number",

                            value=primary_score,

                            title={"text": "Confidence"},

                            gauge={

                                "axis": {"range": [0, 100]},

                                "bar": {"color": "#00C9FF"},

                                "bgcolor": "#E5E7EB"

                            }

                        ))

                        fig.update_layout(
                            height=300,
                            margin=dict(l=10, r=10, t=40, b=10)
                        )

                        st.plotly_chart(
                            fig,
                            use_container_width=True
                        )

                    st.markdown("---")

                    c1, c2 = st.columns(2)

                    with c1:

                        st.markdown("## 🎭 Secondary Emotion")

                        st.info(
                            f"{emoji.get(secondary,'🙂')} "
                            f"{secondary.title()} "
                            f"({secondary_score:.2f}%)"
                        )

                    with c2:

                        st.markdown("## 🧠 Mixed Emotion")

                        if mixed:

                            st.warning(
                                f"Your text contains both "
                                f"**{primary.title()}** and "
                                f"**{secondary.title()}** emotions."
                            )

                        else:

                            st.success("Single dominant emotion detected.")

                    st.markdown("---")

                    st.subheader("📊 Confidence Distribution")

                    for emotion_name, score in confidence.items():

                        st.write(
                            f"**{emotion_name.title()}** "
                            f"({score:.2f}%)"
                        )

                        st.progress(score / 100)

                    st.markdown("---")

                    st.subheader("💡 AI Learning Coach")

                    if isinstance(recommendation, list):

                        for tip in recommendation:

                            st.success("✅ " + tip)

                    else:

                        st.success(recommendation)

                    st.markdown("---")

                    st.subheader("💬 AI Motivation")

                    st.info(motivation)

                    st.subheader("🧠 Emotion Insight")

                    st.success(insight)

                else:

                    st.error("Prediction failed.")

            except requests.exceptions.ConnectionError:

                st.error("❌ FastAPI server is not running.")

            except Exception as e:

                st.error("Unexpected Error")

                st.exception(e)
                # ==========================================================
# HISTORY
# ==========================================================

if "history" not in st.session_state:
    st.session_state.history = []

if predict and text.strip() != "":

    try:

        response = requests.post(
            API_URL,
            json={"text": text},
            timeout=30
        )

        if response.status_code == 200:

            result = response.json()

            st.session_state.history.insert(
                0,
                {
                    "text": text,
                    "emotion": result["primary_emotion"]
                }
            )

            st.session_state.history = st.session_state.history[:10]

    except:
        pass

# ==========================================================
# HISTORY PANEL
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<h2 style='text-align:center;'>
📜 Recent Emotion History
</h2>
""", unsafe_allow_html=True)

if len(st.session_state.history) == 0:

    st.info("No predictions yet.")

else:

    cols = st.columns(2)

    for i, item in enumerate(st.session_state.history):

        with cols[i % 2]:

            icon = emoji.get(item["emotion"], "🙂")

            st.markdown(f"""
<div style="
background:#1f2430;
border-radius:15px;
padding:20px;
margin-bottom:15px;
box-shadow:0 4px 12px rgba(0,0,0,0.3);
">
<h3 style="margin:0;color:white;">
{icon} {item['emotion'].title()}
</h3>

<p style="margin-top:12px;color:#CBD5E1;">
{item['text']}
</p>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# ANALYTICS
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<h2 style='text-align:center;'>
📊 Analytics Dashboard
</h2>
""", unsafe_allow_html=True)

show_dashboard(st.session_state.history)

# ==========================================================
# PROJECT INFO
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<h2 style="text-align:center;margin-bottom:35px;">
✨ Platform Features
</h2>
""", unsafe_allow_html=True)

cards = [
    ("🎭", "Emotion Detection",
     "Detect user emotions using Machine Learning."),
    ("📚", "AI Learning Support",
     "Personalized recommendations based on emotions."),
    ("📊", "Analytics Dashboard",
     "Interactive dashboards, prediction history and insights.")
]

c1, c2, c3 = st.columns(3)

for col, (icon, title, desc) in zip([c1, c2, c3], cards):
    with col:
        st.markdown(f"""
<div style="
background:#1e293b;
border:1px solid #334155;
border-radius:20px;
padding:30px 25px;
height:280px;
box-shadow:0 8px 20px rgba(0,0,0,.35);
margin-bottom:35px;
">

<div style="font-size:45px;">{icon}</div>

<h3 style="color:white;margin-top:15px;margin-bottom:15px;font-size:28px;">
{title}
</h3>

<p style="color:#CBD5E1;font-size:18px;line-height:1.6;margin:0;">
{desc}
</p>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# TECHNOLOGY
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<h2 style="text-align:center;margin-bottom:35px;">
⚙️ Technology Stack
</h2>
""", unsafe_allow_html=True)

cards = [
    ("🎨", "Frontend", "Streamlit"),
    ("⚡", "Backend", "FastAPI"),
    ("🧠", "ML Model", "Logistic Regression"),
    ("📚", "Dataset", "GoEmotions"),
]

cols = st.columns(4, gap="large")

for col, (icon, title, value) in zip(cols, cards):
    with col:
        st.markdown(f"""
<div style="
background:#1e293b;
border:1px solid #334155;
border-radius:20px;
padding:28px 20px;
height:260px;
text-align:center;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
box-shadow:0 8px 20px rgba(0,0,0,.35);
">

<div style="font-size:46px;">{icon}</div>

<div style="
margin-top:15px;
color:#94a3b8;
font-size:18px;
font-weight:500;
">
{title}
</div>

<div style="
margin-top:18px;
color:white;
font-size:24px;
font-weight:700;
">
{value}
</div>

</div>
""", unsafe_allow_html=True)
# ==========================================================
# FOOTER
# ==========================================================

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<center>

<h2>🧠 AI Emotion Learning Assistant</h2>

<p style='color:gray;'>

Built with ❤️ using
Python • Streamlit • FastAPI • Scikit-Learn

</p>

<p>

Emotion Detection & Learning Support System

</p>

</center>
""", unsafe_allow_html=True)


