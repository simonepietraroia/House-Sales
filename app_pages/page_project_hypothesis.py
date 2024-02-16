import streamlit as st


def page_project_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    # conclusions taken from "02 - Churned Customer Study" notebook
    st.success(
        f"* We suspect that a higher grade in OverallQual the higher the value property/ Sales Price: Correct. "
        f"The correlation study at Sales Records Study supports that. \n\n"

        f"Higher OverallQual is a major indicator of predicted increased value property which in turn increases the sale price. "
    )
