import streamlit as st


# Override the default padding of streamlit app
def override_app_padding():
    st.markdown(
        """
    <style>
        .block-container {
             padding-top: 1rem;
             padding-bottom: 2rem;
             max-height: 100vh;
        }   
    </style>
    """,
        unsafe_allow_html=True,
    )
