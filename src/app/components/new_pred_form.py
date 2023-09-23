import streamlit as st
from utils.utils import data_preprocessor


family_options = [
    "AUTOMOTIVE",
    "BABY CARE",
    "BEAUTY",
    "BEVERAGES",
    "BOOKS",
    "BREAD/BAKERY",
    "CELEBRATION",
    "CLEANING",
    "DAIRY",
    "DELI",
    "EGGS",
    "FROZEN FOODS",
    "GROCERY I",
    "GROCERY II",
    "HARDWARE",
    "HOME AND KITCHEN I",
    "HOME AND KITCHEN II",
    "HOME APPLIANCES",
    "HOME CARE",
    "LADIESWEAR",
    "LAWN AND GARDEN",
    "LINGERIE",
    "LIQUOR,WINE,BEER",
    "MAGAZINES",
    "MEATS",
    "PERSONAL CARE",
    "PET SUPPLIES",
    "PLAYERS AND ELECTRONICS",
    "POULTRY",
    "PREPARED FOODS",
    "PRODUCE",
    "SCHOOL AND OFFICE SUPPLIES",
    "SEAFOOD",
]

day_of_week_options = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}


def new_pred_form():
    # Display a subheader for making a new prediction
    st.subheader("Make a New Prediction")

    # Create a container to organize the form elements
    with st.container():
        # Create a form for user input
        with st.form("sales_prediction_form"):
            # Split the form into two columns
            form_col_1, form_col_2 = st.columns(2)

            # Form column 1
            with form_col_1:
                # Create a dropdown for selecting the family of the store
                family = st.selectbox(
                    label="Please Select the Family of the Store",
                    options=family_options,
                )

                # Create a dropdown for selecting the day of the week
                day_of_week = st.selectbox(
                    label="Select day of the week",
                    options=list(day_of_week_options.keys()),
                    format_func=lambda x: day_of_week_options[
                        list(day_of_week_options.keys()).index(x) + 1
                    ],
                )

                # Create a date input field for choosing the forecast date
                current_date = st.date_input(label="Choose the forecast date")

            # Form column 2
            with form_col_2:
                # Create a numeric input field for the number of items on promotion
                onpromotion = st.number_input(
                    label="Enter the number of items on promotion", min_value=0
                )

                # Create a numeric input field for entering previous sales
                lag_1 = st.number_input(label="Enter previous sales", min_value=0)

                # Create a numeric input field for entering rolling mean
                rolling_mean = st.number_input(label="Enter rolling mean", min_value=0)

            # Create a form submit button with a primary style
            st.form_submit_button(
                label="Submit",
                use_container_width=True,
                type="primary",
                on_click=lambda: data_preprocessor(
                    family, day_of_week, current_date, onpromotion, lag_1, rolling_mean
                ),
            )
