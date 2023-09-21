import streamlit as st

from components.render_predicted_sale import render_predicted_sale


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


# Define the sidebar component
def sidebar():
    # In the Streamlit sidebar
    with st.sidebar:
        # Expandable section for Store Family
        with st.expander("STORE FAMILY"):
            # Iterate over family options and display them with custom styling
            for family in family_options:
                st.markdown(
                    f"""
                    <div style='background-color: #835AF1; padding: .5rem 1rem; border-radius: .5rem; color: white; margin-bottom: .5rem'>{family}</div>
                    """,
                    unsafe_allow_html=True,
                )

        # Expandable section for Sales Predictions
        with st.expander("SALES PREDICTIONS"):
            # Render predicted sale for each of the top 3 predictions
            for i in range(3):
                render_predicted_sale()

        # Add an empty Markdown element to create space
        st.markdown(f"{'<br>'*2}", unsafe_allow_html=True)

        # Expandable section for About App
        with st.expander("ABOUT APP"):
            # Provide information about the SalesSense app
            st.write(
                "SalesSense is an intuitive web app powered by cutting-edge machine learning models that provides real-time sales forecasts, helping businesses optimize inventory, boost profits, and make data-driven decisions effortlessly"
            )
