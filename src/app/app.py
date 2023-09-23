import streamlit as st
from datetime import date

from utils.utils import override_app_padding
from components.app_header import app_header
from components.new_pred_form import new_pred_form
from components.sidebar import sidebar


# Set page title and layout
st.set_page_config(page_title=" SalesSense Prediction", layout="wide")

# Apply the function to override default padding
override_app_padding()

# Define custom color palette
custom_color_palette = ["#835AF1", "#37AA9C", "#B8F7D4", "#94F3E4"]

# Implement the app header
view_trend_button = app_header()

# Implement the sidebar
sidebar()


if view_trend_button == False:
    # Implement the prediction form
    new_pred_form()

else:
    # Define a function that sets view_trend_button to False
    def callback_func():
        view_trend_button = False

    st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

    st.button(
        "Make a Prediction", on_click=lambda: callback_func(), use_container_width=True
    )

# st.markdown(
#     "<h2 style='text-align: center; margin-bottom: -3.125rem'>Predicted Sales</h2>",
#     unsafe_allow_html=True,
# )
