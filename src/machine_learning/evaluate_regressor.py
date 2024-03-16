import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

def regression_performance(X, y, regressor, label):
   
    prediction = regressor.predict(X)

    st.write('#### Regression Performance')
    st.write(f'**Mean Squared Error ({label}):** {mean_squared_error(y, prediction):.2f}')
    st.write(f'**R^2 Score ({label}):** {r2_score(y, prediction):.2f}')


# Function to evaluate the performance of the regressor model
def regressor_performance(X_train, y_train, X_test, y_test, regressor, label):
    
    st.info("Train Set Performance")
    regression_performance(X_train, y_train, regressor, label)

    st.info("Test Set Performance")
    regression_performance(X_test, y_test, regressor, label)
