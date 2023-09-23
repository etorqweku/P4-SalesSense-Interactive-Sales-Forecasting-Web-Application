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


def data_preprocessor(
    family: str,
    day_of_week: int,
    current_date,
    onpromotion: int,
    lag_1: int,
    rolling_mean: int,
):
    print(family, day_of_week, current_date, onpromotion, lag_1, rolling_mean)
