import streamlit as st

def page_summary_body():

    st.write("### Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Terms & Jargon**\n"
        f"* **1stFlrSF** is First Floor Square Feet.\n"
        f"* **2ndFlrSF** is Second Floor Square Feet.\n"
        f"* **BedroomAbvGr** is Bedroom Above Grade and is given a score from 0-8.\n "
        f"* **BsmtExposure** refers to walkout or garden level walls ( Gd: Good Exposure; Av: Average Exposure; Mn: Mimimum Exposure; No: No Exposure; None: No Basement)\n" 
        f"* **BsmtFinType1** Rating of basement finished area (GLQ: Good Living Quarters; ALQ: Average Living Quarters;  BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement)\n" 
        f"* **BsmtFinSF1** Type 1 finished square feet\n" 
        f"* **BsmtUnfSF** Unfinished square feet of basement area\n" 
        f"* **TotalBsmtSF** Total square feet of basement area\n\n" 
        f"**Project Dataset**\n"
        f"* The dataset is from a public sales record of properties purchased in Ames, Iowa. ** "
        f"The dataset was public so hiding dataset was not  neccecary and it contains individual measurments and custom grading of properties sold."
    )
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/simonepietraroia/House-Sales/blob/main/README.md).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in understanding the property market of Ames, Iowa"
        f"so that the client can place an appropriate for sale price on 4 different inherited properties.\n "
        f"* 2 - The client is interested in discovering how house attributes correlate with sale prices. Therefore, the client expects data visualizations of the correlated variables against the sale price.\n "
        f"The client will maximize the sales price for the inherited properties."
        )

        