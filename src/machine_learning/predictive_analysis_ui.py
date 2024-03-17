import streamlit as st


def predict_sale_price(X_live, sales_features, sales_pipeline_dc_fe, sales_pipeline_model):

    # Apply data cleaning / feature engineering pipeline to live data
    X_live_sales_dc_fe = sales_pipeline_dc_fe.transform(X_live)

    # Predict sale price
    sales_prediction = sales_pipeline_model.predict(X_live_sales_dc_fe)
    
    # Display the predicted sale price
    st.write(f"Predicted Sale Price: ${sales_prediction[0]:.2f}")

    return sales_prediction[0]


def predict_cluster(X_live, cluster_features, cluster_pipeline, cluster_profile):

    # Predict cluster for the live data
    cluster_prediction = cluster_pipeline.predict(X_live)

    # Display cluster prediction
    st.write(f"Predicted Cluster: {cluster_prediction[0]}")

    # Display cluster profile interpretation
    st.info("Cluster Profile Interpretation:")
    st.success("""
    Cluster 0: Users without internet, low spender with phone.
    Cluster 1: Users with internet, high spender with phone.
    Cluster 2: Users with internet, mid spender without phone.
    """)

    # Display cluster profile
    st.table(cluster_profile)
