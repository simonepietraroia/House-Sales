
# Sales Prediction App

## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In your Cloud IDE, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace. 
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|





## Business Requirements
As a good friend, you are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximising the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.


## Hypothesis and how to validate?
* We predict that OverallQual will be the feature that most closely correlates to the properties' SalePrice
* All the features will be compared to the target (SalePrice) and the most correlated features will be shown


## The rationale to map the business requirements to the Data Visualisations and ML tasks
* The client wishes to discover how house attributes correlate with sale prices. Therefore, the client expects data visualizations of the correlated variables against the sale price.
* A regressor model was used in this case to be able to show whether changes observed in the dependent variable are associated with changes in one or more of the explanatory variables.
* The dashboard will contain a graph of the most impactful variable and will also contain a cluster analysis which will be devided in 3 clusters.
* The dashboard will also contain a page to predict sales price by inputing the 9 most impactful features which allows the client to maximize sales price for the inherited properties.
* We agreed with the client an R2 score of at least 0.75 on the train set as well as on the test set.


## Dashboard Design
### Page 1: Quick project summary
* Quick project summary
	* Project Terms & Jargon
	* Describe Project Dataset
	* State Business Requirements

### Page 3: Sales Price Predict
* State business requirement 2
* Set of widgets inputs, Each set of inputs is related to a given ML task to predict sales value.
* "Run predictive analysis" button that serves the prospect data to our ML pipelines, and predicts an estimated sales price for the property value 

### Page 4: Project Hypothesis and Validation
* Before the analysis, we knew we wanted this page to describe each project hypothesis, the conclusions, and how we validated each. After the data analysis, we can report that:
* - We suspect Overall Qual has the most impact of property value
	* Correct. The correlation study at Sales Record Study supports that.
    
### Page 5: Predict Value
* Considerations and conclusions after the pipeline is trained
* Present ML pipeline steps
* Feature importance
* Pipeline performance

### Page 6: Cluster Analysis
* Considerations and conclusions after the pipeline is trained
* Present ML pipeline steps
* Silhouette plot
* Clusters distribution across SalePrice levels
* Relative Percentage (%) of SalePrice in each cluster
* The most important features to define a cluster
* Cluster Profile


## Unfixed Bugs
* Sales Price predict page on dashboard has input boxes that don't fit the input numbers more than 2 digets


## Deployment
### Heroku

* The App live link is: https://predict-sales-app-98929437a4b0.herokuapp.com// 
* Set the runtime.txt Python version to a [ python-3.9.18 ] stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries
* Pandas Profiling
* scikit-learn
* Kaggle
* ydata_profiling
* matplotlib.pyplot
* Seaborn
* ppScore
* Feature-engine
* ScipyStats
* Numpy
* Xgboost
* Joblib
* Yellowbrick
* Plotly

## Credits 

* A lot of inspiration is taken from the Code Institute's Churnometer walkthrough project
* The HyperOptimizationSearch function was directly taken from the Churnometer project 
* The slack predictive analysis channel was useful in helping trouble shoot some technical issues with the template

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

## Acknowledgements (optional)
* The slack predictive analysis channel was useful in helping trouble shoot some technical issues with the template

