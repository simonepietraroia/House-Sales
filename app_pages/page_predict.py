import streamlit as st
import pandas as pd
from src.data_management import load_telco_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import predict_sale_price, predict_cluster

def page_predict_body():

    # load predict sales files
    version = 'v1'
    sales_pipe_dc_fe = load_pkl_file(
        f'outputs/ml_pipeline/predict_sales/{version}/clf_pipeline_data_cleaning_feat_eng.pkl')
    sales_pipe_model = load_pkl_file(
        f"outputs/ml_pipeline/predict_sales/{version}/clf_pipeline_model.pkl")
    sales_features = (pd.read_csv(f"outputs/ml_pipeline/predict_sales/{version}/X_train.csv")
                      .columns
                      .to_list()
                      )

    # load cluster analysis files
    version = 'v1'
    cluster_pipe = load_pkl_file(
        f"outputs/ml_pipeline/cluster_analysis/{version}/cluster_pipeline.pkl")
    cluster_features = (pd.read_csv(f"outputs/ml_pipeline/cluster_analysis/{version}/TrainSet.csv")
                        .columns
                        .to_list()
                        )
    cluster_profile = pd.read_csv(
        f"outputs/ml_pipeline/cluster_analysis/{version}/clusters_profile.csv")

    st.write("### Prospect Churnometer Interface")
    st.info(
        f"* The client is interested in knowing an aproximate property value for the 4 inherited properties.\n"
        f"* The client is also interested in having the data be shown visually to see which properties belong to which cluster.\n"
        f"* Based on that, present potential factors that affect property value."
    )
    st.write("---")

    # Generate Live Data
    X_live = DrawInputsWidgets()

    # predict on live data
    if st.button("Run Predictive Analysis"):
        sales_prediction = predict_sale_price(
            X_live, sales_features, sales_pipe_dc_fe, sales_pipe_model)

        st.write(f"Predicted Sale Price: ${sales_prediction:.2f}")

        # If you have a cluster prediction function, you can call it here
        # predict_cluster(X_live, cluster_features, cluster_pipe, cluster_profile)


def check_variables_for_UI(sales_features, cluster_features):
    import itertools

    combined_features = set(
        list(
            itertools.chain(sales_features, cluster_features)
        )
    )
    st.write(
        f"* There are {len(combined_features)} features for the UI: \n\n {combined_features}")


def DrawInputsWidgets():

    # load dataset
    df = load_telco_data()
    percentageMin, percentageMax = 0.4, 2.0

    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.beta_columns(10)

    X_live = pd.DataFrame([], index=[0])

    with col1:
        feature = "1stFlrSF"
        custom_number = st.text_area(
            label=feature,
            value=str(df[feature].median()),  # Convert median value to string
        )
    # Convert custom_number to float if it's not empty
    custom_number = float(custom_number) if custom_number.strip() != '' else None
    X_live[feature] = custom_number

    # Apply HTML/CSS to adjust the width of the input box
    st.write(f'<style>div.row-widget.stTextArea>div {{"width": "400px"}}</style>', unsafe_allow_html=True)


    with col2:
        feature = "GarageArea"
        custom_number = st.text_area(
            label=feature,
            value=str(df[feature].median()),  # Convert median value to string
        )
    # Convert custom_number to float if it's not empty
    custom_number = float(custom_number) if custom_number.strip() != '' else None
    X_live[feature] = custom_number

    # Apply HTML/CSS to adjust the width of the input box
    st.write(f'<style>div.row-widget.stTextArea>div {{"width": "400px"}}</style>', unsafe_allow_html=True)

    with col3:
        feature = "LotArea"
        custom_number = st.text_area(
            label=feature,
            value=str(df[feature].median()),  # Convert median value to string
        )
    # Convert custom_number to float if it's not empty
    custom_number = float(custom_number) if custom_number.strip() != '' else None
    X_live[feature] = custom_number

    # Apply HTML/CSS to adjust the width of the input box
    st.write(f'<style>div.row-widget.stTextArea>div {{"width": "400px"}}</style>', unsafe_allow_html=True)


    with col4:
        feature = "BsmtUnfSF"
        custom_number = st.text_area(
            label=feature,
            value=str(df[feature].median()),  # Convert median value to string
        )
    # Convert custom_number to float if it's not empty
    custom_number = float(custom_number) if custom_number.strip() != '' else None
    X_live[feature] = custom_number

    # Apply HTML/CSS to adjust the width of the input box
    st.write(f'<style>div.row-widget.stTextArea>div {{"width": "400px"}}</style>', unsafe_allow_html=True)

    with col5:
        feature = "GrLivArea"
        custom_number = st.text_area(
            label=feature,
            value=str(df[feature].median()),  # Convert median value to string
        )
    # Convert custom_number to float if it's not empty
    custom_number = float(custom_number) if custom_number.strip() != '' else None
    X_live[feature] = custom_number

    # Apply HTML/CSS to adjust the width of the input box
    st.write(f'<style>div.row-widget.stTextArea>div {{"width": "400px"}}</style>', unsafe_allow_html=True)

    with col6:
        feature = "LotFrontage"
        custom_number = st.text_area(
            label=feature,
            value=str(df[feature].median()),  # Convert median value to string
        )
    # Convert custom_number to float if it's not empty
    custom_number = float(custom_number) if custom_number.strip() != '' else None
    X_live[feature] = custom_number

    # Apply HTML/CSS to adjust the width of the input box
    st.write(f'<style>div.row-widget.stTextArea>div {{"width": "400px"}}</style>', unsafe_allow_html=True)

    with col7:
        feature = "BsmtFinSF1"
        custom_number = st.text_area(
            label=feature,
            value=str(df[feature].median()),  # Convert median value to string
        )
    # Convert custom_number to float if it's not empty
    custom_number = float(custom_number) if custom_number.strip() != '' else None
    X_live[feature] = custom_number

    # Apply HTML/CSS to adjust the width of the input box
    st.write(f'<style>div.row-widget.stTextArea>div {{"width": "400px"}}</style>', unsafe_allow_html=True)

    with col8:
        feature = "TotalBsmtSF"
        custom_number = st.text_area(
            label=feature,
            value=str(df[feature].median()),  # Convert median value to string
        )
    # Convert custom_number to float if it's not empty
    custom_number = float(custom_number) if custom_number.strip() != '' else None
    X_live[feature] = custom_number

    # Apply HTML/CSS to adjust the width of the input box
    st.write(f'<style>div.row-widget.stTextArea>div {{"width": "400px"}}</style>', unsafe_allow_html=True)

    with col9:
        feature = "OpenPorchSF"
        custom_number = st.text_area(
            label=feature,
            value=str(df[feature].median()),  # Convert median value to string
        )
    # Convert custom_number to float if it's not empty
    custom_number = float(custom_number) if custom_number.strip() != '' else None
    X_live[feature] = custom_number

    # Apply HTML/CSS to adjust the width of the input box
    st.write(f'<style>div.row-widget.stTextArea>div {{"width": "400px"}}</style>', unsafe_allow_html=True)
    with col10:
        feature = "2ndFlrSF"
        custom_number = st.text_area(
            label=feature,
            value=str(df[feature].median()),  # Convert median value to string
        )
    # Convert custom_number to float if it's not empty
    custom_number = float(custom_number) if custom_number.strip() != '' else None
    X_live[feature] = custom_number

    # Apply HTML/CSS to adjust the width of the input box
    st.write(f'<style>div.row-widget.stTextArea>div {{"width": "400px"}}</style>', unsafe_allow_html=True)
    return X_live
