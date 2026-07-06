import streamlit as st
import pandas as pd
import plotly.express as px


def show_dashboard(history):

    st.header("📊 Analytics Dashboard")

    # ----------------------------
    # No data
    # ----------------------------
    if len(history) == 0:
        st.info("No predictions available.")
        return

    # ----------------------------
    # Create DataFrame
    # ----------------------------
    df = pd.DataFrame(history)

    # ----------------------------
    # Summary Metrics
    # ----------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Predictions", len(df))

    with col2:
        st.metric("Unique Emotions", df["emotion"].nunique())

    # ----------------------------
    # Prediction History
    # ----------------------------
    st.subheader("📜 Prediction History")

    st.dataframe(
        df,
        width="stretch"
    )

    # ----------------------------
    # Download CSV
    # ----------------------------
    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download Prediction History",
        data=csv,
        file_name="prediction_history.csv",
        mime="text/csv"
    )

    # ----------------------------
    # Emotion Counts
    # ----------------------------
    st.subheader("📈 Emotion Counts")

    emotion_counts = (
        df.groupby("emotion")
        .size()
        .reset_index(name="Count")
        .sort_values(by="Count", ascending=False)
    )

    emotion_counts.rename(
        columns={"emotion": "Emotion"},
        inplace=True
    )

    # ----------------------------
    # Most Frequent Emotion
    # ----------------------------
    top_emotion = emotion_counts.iloc[0]["Emotion"]

    st.success(f"Most Detected Emotion: **{top_emotion}**")

    # ----------------------------
    # Bar Chart
    # ----------------------------
    fig_bar = px.bar(
        emotion_counts,
        x="Emotion",
        y="Count",
        color="Emotion",
        text="Count",
        title="Emotion Counts"
    )

    fig_bar.update_layout(
        xaxis_title="Emotion",
        yaxis_title="Count",
        template="plotly_white",
        height=500
    )

    st.plotly_chart(
        fig_bar,
        width="stretch"
    )

    # ----------------------------
    # Pie Chart
    # ----------------------------
    st.subheader("🥧 Emotion Distribution")

    fig_pie = px.pie(
        emotion_counts,
        names="Emotion",
        values="Count",
        color="Emotion",
        hole=0.4,
        title="Emotion Distribution"
    )

    fig_pie.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig_pie.update_layout(
        height=550,
        template="plotly_white"
    )

    st.plotly_chart(
        fig_pie,
        width="stretch"
    )