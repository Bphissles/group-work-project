import streamlit as st

st.set_page_config(
    page_title="Student Performance Factors",
    page_icon="📊",
    layout="wide"
)

st.title("Student Performance Factors")
st.markdown(
    """
    Use the left sidebar to switch pages.
    """
)

with st.expander("How this app is organized (for students)"):
    st.write(
        """
        - `app.py` is the entry point.
        - Pages live in the `/pages` folder and auto-appear in the sidebar.
        """
    )

st.caption("Built with Streamlit • Class template")
