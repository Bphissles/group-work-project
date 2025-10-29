import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")
st.title("Student Performance Factors")

st.divider()
# ROW 1: 
col1_r1, col2_r1 = st.columns([2, 1])

with col1_r1:
    st.subheader("Hours Studied Vs Exam Score")
    st.caption("Scatter plot + trendline")

    # graph
    x_col, y_col = "Hours_Studied", "Exam_Score"
    try:
        if x_col in df.columns and y_col in df.columns:
            plt.figure()
            plt.scatter(df[x_col], df[y_col], alpha=0.6)
            plt.title(f'Scatter — {x_col} vs {y_col}')
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.grid(True)
            plt.show()
        else:
            print('Set x_col and y_col to valid column names.')
    except NameError:
        print('Please load df first.')

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
