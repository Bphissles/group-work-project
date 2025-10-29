import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

df = pd.read_csv("./data/StudentPerformanceFactors.csv")
st.dataframe(df)
st.title("Student Performance Factors")
st.divider()
# ROW 1: 
col1_r1, col2_r1 = st.columns([2, 1])

with col1_r1:
    st.subheader("Hours Studied Vs Exam Score")
    st.caption("Scatter plot + trendline")

    # graph
    x_col, y_col = "Hours_Studied", "Exam_Score"
    if x_col in df.columns and y_col in df.columns:
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.scatter(df[x_col], df[y_col], alpha=0.6)
        
        # Add trendline
        z = np.polyfit(df[x_col], df[y_col], 1)
        p = np.poly1d(z)
        ax.plot(df[x_col], p(df[x_col]), "r--", alpha=0.8, linewidth=2)
        
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()
    else:
        st.error('Column names not found in dataframe.')

with col2_r1:
    st.subheader("Heading")
    st.write("Big Copy")

st.divider()
# ROW 2:
col1_r2, col2_r2, col3_r2 = st.columns(3)

with col1_r2:
    st.subheader("Activity Vs Exam Score Heatmap")

with col2_r2:
    st.subheader("Heading")
    st.write("Big Copy")

with col3_r2:
    st.subheader("Sleep Vs Exam Score Heatmap")
    st.write("Big Copy")

st.divider()
# ROW 3:
col1_r3, col2_r3 = st.columns([1, 2])

with col1_r3:
    st.subheader("Heading")
    st.write("Big Copy")

with col2_r3:
    btn_col1, btn_col2, btn_col3 = st.columns(3)
    
    with btn_col1:
        st.write("Big Copy")
    
    with btn_col2:
        st.write("Big Copy")
    
    with btn_col3:
        st.write("Big Copy")

# Footer
st.divider()
st.caption("Data source")
