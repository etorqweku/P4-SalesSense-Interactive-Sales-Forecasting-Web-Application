import streamlit as st
from datetime import date

from utils.utils import override_app_padding
from components.app_header import app_header


# Apply the function to override default padding
override_app_padding()

# Define custom color palette
custom_color_palette = ["#835AF1", "#37AA9C", "#B8F7D4", "#94F3E4"]

# Implement the app header
view_trend_button = app_header()
