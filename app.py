import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_prospect import page_prospect_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_predict_sales import page_predict_sale_body
from app_pages.page_cluster import page_cluster_body
from app_pages.page_inherited_houses import page_inherited_house
app = MultiPage(app_name= "Predict Sales") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Sales Price Prediction", page_prospect_body)
app.add_page("Inherited Houses Prediction", page_inherited_house)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("ML: Predict Value", page_predict_sale_body)
app.add_page("ML: Cluster Analysis", page_cluster_body)

app.run() # Run the  app
