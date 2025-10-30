import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Get the absolute path to the data file relative to this script
DATA_PATH = Path(__file__).parent.parent / "data" / "StudentPerformanceFactors.csv"
df = pd.read_csv(DATA_PATH)

st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

## Make collapse for dataframe
with st.expander("Data"):
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
    def pie_from_series(series, categories, title):
        if series.name not in df.columns:
            st.error(f"Column '{series.name}' not found in dataframe.")
            return

        s = pd.Categorical(df[series.name], categories=categories, ordered=True)
        counts = pd.Series(s).value_counts(dropna=True, sort=False)
        pie_df = counts.rename_axis("label").reset_index(name="count")

        fig = px.pie(
            pie_df,
            names="label",
            values="count",
            title=title,
            hole=0.3,
        )
        fig.update_traces(textposition="inside", textinfo="percent+label")
        fig.update_layout(margin=dict(l=0, r=0, t=50, b=0))
        st.plotly_chart(fig, use_container_width=True)

    pie_col1, pie_col2, pie_col3 = st.columns(3)

    with pie_col1:
        st.subheader("Internet Access")
        pie_from_series(
            series=df["Internet_Access"],
            categories=["Yes", "No"],
            title="Proportion of Internet Access"
        )

    with pie_col2:
        st.subheader("Parental Involvement")
        pie_from_series(
            series=df["Parental_Involvement"],
            categories=["Low", "Medium", "High"],
            title="Parental Involvement Levels"
        )

    with pie_col3:
        st.subheader("Access to Resources")
        pie_from_series(
            series=df["Access_to_Resources"],
            categories=["Low", "Medium", "High"],
            title="Access to Resources Levels"
        )

# Footer
st.divider()
st.caption("Data source")
