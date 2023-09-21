import streamlit as st


# Override the default padding of streamlit app
def override_app_padding():
    st.markdown(
        """
    <style>
        .block-container {
             padding-top: 1rem;
        }   
    </style>
    """,
        unsafe_allow_html=True,
    )
