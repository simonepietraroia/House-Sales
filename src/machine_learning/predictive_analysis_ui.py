import streamlit as st


def predict_sales(X_live, sales_features, sales_pipeline_dc_fe, sales_pipeline_model):

    # from live data, subset features related to this pipeline
    X_live_sales = X_live.filter(sales_features)

    # apply data cleaning / feat engine pipeline to live data
    X_live_sales_dc_fe = sales_pipeline_dc_fe.transform(X_live_sales)

    # predict
    sales_prediction = sales_pipeline_model.predict(X_live_sales_dc_fe)
    sales_prediction_proba = sales_pipeline_model.predict_proba(
        X_live_sales_dc_fe)
    # st.write(churn_prediction_proba)

    # Create a logic to display the results
    sales_prob = sales_prediction_proba[0, sales_prediction][0]*100
    if churn_prediction == 1:
        churn_result = 'will'
    else:
        churn_result = 'will not'

    statement = (
        f'### There is {churn_prob.round(1)}% probability '
        f'that this prospect **{churn_result} churn**.')

    st.write(statement)

    return churn_prediction


def predict_cluster(X_live, cluster_features, cluster_pipeline, cluster_profile):

    # from live data, subset features related to this pipeline
    X_live_cluster = X_live.filter(cluster_features)

    # predict
    cluster_prediction = cluster_pipeline.predict(X_live_cluster)

    statement = (
        f"### The prospect is expected to belong to **cluster {cluster_prediction[0]}**")
    st.write("---")
    st.write(statement)

  	# text based on "07 - Modeling and Evaluation - Cluster Sklearn" notebook conclusions
    statement = (
        f"* Historically, **users in Clusters 0  don't tend to Churn** "
        f"whereas in **Cluster 1 a third of users churned** "
        f"and in **Cluster 2 a quarter of users churned**."
    )
    st.info(statement)

  	# text based on "07 - Modeling and Evaluation - Cluster Sklearn" notebook conclusions
    statement = (
        f"* The cluster profile interpretation allowed us to label the cluster in the following fashion:\n"
        f"* Cluster 0 has user without internet, who is a low spender with phone\n"
        f"* Cluster 1 has user with Internet, who is a high spender with phone\n"
        f"* Cluster 2 has user with Internet , who is a mid spender without phone"
    )
    st.success(statement)

    # hack to not display index in st.table() or st.write()
    cluster_profile.index = [" "] * len(cluster_profile)
    # display cluster profile in a table - it is better than in st.write()
    st.table(cluster_profile)
