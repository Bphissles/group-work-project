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

gender_choice = st.sidebar.selectbox("Gender", ["All", "Male", "Female"])
family_choice = st.sidebar.selectbox("Family Income", ["All", "Low", "Medium", "High"])
school_choice = st.sidebar.selectbox("School Type", ["All", "Public", "Private"])
att_range = st.sidebar.slider("Attendance (%)", 60, 100, (60, 100), step=1)

df_filtered = df.copy()
if gender_choice != "All":
    df_filtered = df_filtered[df_filtered["Gender"] == gender_choice]
if family_choice != "All":
    df_filtered = df_filtered[df_filtered["Family_Income"] == family_choice]
if school_choice != "All":
    df_filtered = df_filtered[df_filtered["School_Type"] == school_choice]
att_min, att_max = att_range
df_filtered = df_filtered[
    pd.to_numeric(df_filtered["Attendance"], errors="coerce").between(att_min, att_max)
]

## Make collapse for dataframe
with st.expander("Data"):
    st.dataframe(df_filtered)

st.title("Student Performance Factors")
st.divider()
# ROW 1: 
col1_r1, col2_r1 = st.columns([2, 1])

with col1_r1:
    st.subheader("Hours Studied Vs Exam Score")
    st.caption("Scatter plot + trendline")

    # graph
    x_col, y_col = "Hours_Studied", "Exam_Score"
    if x_col in df_filtered.columns and y_col in df_filtered.columns:
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.scatter(df_filtered[x_col], df_filtered[y_col], alpha=0.6)
        
        # Add trendline
        z = np.polyfit(df_filtered[x_col], df_filtered[y_col], 1)
        p = np.poly1d(z)
        ax.plot(df_filtered[x_col], p(df_filtered[x_col]), "r--", alpha=0.8, linewidth=2)
        
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()
    else:
        st.error('Column names not found in dataframe.')

with col2_r1:
    st.subheader("Correlation Between Study Time and Exam Scores")
    st.write("From the scatterplot it is clear there is a strong positive correlation between a student's study time and their resulting exam score. Students who put it the effort to study for long hours are likely to receive high remarks on their grades.")

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
    st.subheader("Outside Resources Proportions")
    st.write("The vast majority of students have access to the internet, regardless of their circumstances at home. Most students also have access to sufficient academic resources at home, and the same can be said for the help they receive in the form of parental involvement. All of these are crucial underlying factors that contribute to students' exam scores.")

with col2_r3:
    def pie_from_series(series, categories, title=""):
        s = pd.Categorical(series, categories=categories, ordered=True)
        counts = pd.Series(s).value_counts(dropna=True, sort=False)
        pie_df = counts.rename_axis("label").reset_index(name="count")

        if pie_df["count"].sum() == 0:  # CHANGED: guard for empty selection after filtering
            st.warning(f"No data to plot for {title}.")
            return

        fig = px.pie(
            pie_df,
            names="label",
            values="count",
            title=title,
            category_orders={"label": categories},
            hole=0.3,
            color="label",
            color_discrete_map={
                "Yes": "green", "High": "green",
                "No": "red", "Low": "red",
                "Medium": "yellow"
            },
        )
        fig.update_traces(textposition="inside", textinfo="percent+label", sort=False)
        fig.update_layout(
            title=dict(text=title, x=0.5, xanchor="center", y=1),
            showlegend=True,
            legend=dict(orientation="v", x=0.5, xanchor="center", y=-.1, yanchor="top"),
            height=360,
            margin=dict(l=10, r=10, t=40, b=80),
            uniformtext_minsize=10,
            uniformtext_mode="hide",
        )
        st.plotly_chart(fig, use_container_width=True)

    pie_col1, pie_col2, pie_col3 = st.columns(3)

    with pie_col1:
        pie_from_series(
            series=df_filtered["Internet_Access"],
            categories=["No", "Yes"],
            title="Internet Access"
        )

    with pie_col2:
        pie_from_series(
            series=df_filtered["Parental_Involvement"],
            categories=["Low", "Medium", "High"],
            title="Parental Involvement"
        )

    with pie_col3:
        pie_from_series(
            series=df_filtered["Access_to_Resources"],
            categories=["Low", "Medium", "High"],
            title="Access to Resources"
        )

# Footer
st.divider()
st.caption("Data source")
