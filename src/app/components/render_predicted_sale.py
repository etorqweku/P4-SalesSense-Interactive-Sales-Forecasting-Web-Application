import streamlit as st
from datetime import date


# Render a predicted sale with custom styling
def render_predicted_sale():
    # Use st.markdown to display the content with HTML styling
    return st.markdown(
        f"""<div style='background-color: #37AA9C; padding: .5rem 1rem; border-radius: .5rem; color: white; margin-bottom: .5rem'>
                    <p style='margin-bottom: .1rem'>Date: {date.today()}</p>
                    <h1 style='margin-bottom: -.6rem; margin-top: -.6rem; color: white'>Sale: ${12.00}</h1>
                </div>
            """,
        unsafe_allow_html=True,
    )
