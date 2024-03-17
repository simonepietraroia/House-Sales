import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_telco_data, load_pkl_file
from src.machine_learning.evaluate_regressor import regression_performance, regressor_performance

def page_predict_sale_body():

    version = 'v1'
    # load needed files
    sales_pipe_dc_fe = load_pkl_file(
        f'outputs/ml_pipeline/predict_sales/{version}/clf_pipeline_data_cleaning_feat_eng.pkl')
    sales_pipe_model = load_pkl_file(
        f"outputs/ml_pipeline/predict_sales/{version}/clf_pipeline_model.pkl")
    sales_feat_importance = plt.imread(
        f"outputs/ml_pipeline/predict_sales/{version}/features_importance.png")
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sales/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sales/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sales/{version}/y_train.csv").values
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sales/{version}/y_test.csv").values

    st.write("### ML Pipeline: Predict Sales Price")
    # display pipeline training summary conclusions
    st.info(
        f"* The pipeline was tuned aiming for at least an R2 score of at least 0.75 on the train set as well as on the test set, "
        f"since we are interested in this project in evaluating property value. \n"
        f"* The pipeline performance on train and test set is 1.00 and 0.49, respectively. \n"
        f"* The pipline preformance is most likely low due to the class oversampling method used."
        f" Additionally, the pipline preformance might have been affected by the choice of hyperparameter."
    )

    # show pipelines
    st.write("---")
    st.write("#### There are 2 ML Pipelines arranged in series.")

    st.write(" * The first is responsible for data cleaning and feature engineering.")
    st.write(sales_pipe_dc_fe)

    st.write("* The second is for feature scaling and modelling.")
    st.write(sales_pipe_model)

    # show feature importance plot
    st.write("---")
    st.write("* The features the model was trained and their importance.")
    st.write(X_train.columns.to_list())
    st.image(sales_feat_importance)

    # We don't need to apply dc_fe pipeline, since X_train and X_test
    # were already transformed in the jupyter notebook 

    # evaluate performance on train and test set
    st.write("---")
    st.write("### Pipeline Performance")
    regressor_performance(X_train=X_train, y_train=y_train,
                      X_test=X_test, y_test=y_test,
                      regressor=sales_pipe_model,
                      label="SalePrice")
