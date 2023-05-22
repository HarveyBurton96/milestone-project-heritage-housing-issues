# Heritage Housing Issues

This projects client has the aim of finding the predicted sale price of houses in Ames, Iowa and understanding the correlation between sale price and houses features. Using traditional analysis and predictive models we have provided a dashboard that presents the solution to both questions for the client.

Live version is available [here](Fix later)

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

As a good friend, you are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to help in maximising the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.

## Hypothesis and validation

### Hypothesis one

The size of the first floor will have a greater impact on the house sale than the size of the second floor.

* True, from the correlation study we can see that the size of first floor has a greater impact on the house sale price than the size of the second floor.

### Hypothesis Two

The year the house was built will have a lower impact on the sale price than the year the house was remodelled.

* False, from the correlation study we can see that the year the house was built has a greater impact on the sale price than the year the house was remodelled.

### Hypothesis Three

The overall condition of the house will have a greater impact on the sale price than the overall quality of the material and finish of the house.

* False, from the correlation study we can see that the overall quality of the material and finish of the house has a greater impact on the sale price than the overall condition of the house.

### Hypothesis four

The size of the garage will have a greater impact on the sale price than the size of the wood deck.

* True, from the correlation study we can see that the size of the garage has a greater impact on the sale price than the size of the wood deck.

## CRISP DM

* Business Understanding
  * For this step we will review the request from the client and map out the best solution to solving each business requirement. We will go into more detail about this step in the [ML Business case](#ml-business-case) section below.

* Data Understanding
  * In this step we will create our first two jupyter notebooks. The first one to download the data from Kaggle and to inspect the data types to check everything is in order. In the second notebook we will look at the correlation between the features of the data frame to the Sale price.

* Data Preparation
  * For this step we create two more jupyter notebooks. Notebook '3 Data Cleaning' is used to evaluate the missing data in the dataset and look at the most appropriate way to handle each feature with missing data. In notebook '4 Feature Engineering' we look at different feature engineering methods including categorical encoding - ordinal and numerical transformations to try and achieve a more normal distribution for the features and finally smart correlated selected variables.

* Modelling
  * For this step we create a final jupyter notebook called '5 Modelling and Evaluation Predicted Sale Price'. In this notebook we look at the best regression model to use and selecting reduced features to only include the most important one.

* Evaluation
  * Here we create the streamlit pages and compile the understand and solutions we had found from the data to answer the business requirements for the client. We also make this user friendly for the client to be able to easily understand and share if needed.

* Deployment
  * Finally, we set the streamlit pages live at this step.

![CRISP DM graph](/images/readme_images/CRISP_DM.png)

## ML tasks rationale

### Business Requirement 1

The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualizations of the correlated variables against the sale price to show that.

To solve this business requirement, we created jupyter notebook '2 Housing Prices Correlation'. This compared the correlation between Sale price and the rest of the features available in the data frame. We used the Spearman and the Pearson techniques and then combined the two and selected the top 6 most correlated features. Next, we plotted scatter plots to show how each feature correlated with the sale price using an mlplot which are recorded below. That completes our business requirement 1.

![Scatterplot of First Floor square feet against Sale Price](/images/readme_images/first_floor_against_sale_price.png)

![Scatterplot of Size of garage in square feet against Sale Price](/images/readme_images/garage_against_sale_price.png)

![Scatterplot of Above grade ground living area square feet against Sale Price](/images/readme_images/GrLiv_against_sale_price.png)

![Scatterplot of Rates the overall material and finish of the house against Sale Price](/images/readme_images/OverallQual_against_Sale_price.png)

![Scatterplot of Total square feet of basement area against Sale Price](/images/readme_images/TotalBsmtSF_vs_Sale_price.png)

![Scatterplot of Original construction date against Sale Price](/images/readme_images/Year_vs_sale_price.png)

### Business Requirement 2

The client is interested in predicting the house sales price from her four inherited houses, and any other house in Ames, Iowa.

To solve this business requirement we first needed to build our ML pipeline. As the output from our pipeline would be a continuous number I decided to use the regression model. We then cleaned the data in notebook '3 Data Cleaning' and then did feature engineering in notebook '4 Feature Engineering' in preparation for finding the best model. Finally, we used code from the code institute churnometer walkthrough project to find the best model and hyperparameters to achieve the best R2 score we could. The model was:

![Model steps](/images/readme_images/pipeline_steps.png)

With the following features used: OverallQual, TotalBsmtSF, 2ndFlrSF and GarageArea. Because they were the four most important features to the pipeline out of all the features and once we only used them we did not see a big drop in the R2 score of the model.

![Important features](/images/readme_images/Feature_importance.png)

Once we had the model and features decided we evaluated the model to make sure it met our business requirement of a R2 score above 0.75. As we can see in the image below the model passed this requirement with a R2 score of 0.839

![Model evaluation](/images/readme_images/Model_evaluation.png)

![Train and test predictions](/images/readme_images/Train_test_predictions.png)

Now that we have our completed pipeline, we can solve the next requirement of finding the value of each of the inherited houses:

![First inherited house predicted sale price](/images/readme_images/First_inherited_house.png)

![Second inherited house predicted sale price](/images/readme_images/Second_inherited_house.png)

![Third inherited house predicted sale price](/images/readme_images/Third_inherited_house.png)

![Fourth inherited house predicted sale price](/images/readme_images/Four_inherited_house.png)

To solve the final requirement of allowing the client to find the sale price of any house in Ames, Iowa. We have built in our streamlit pages widgets that allow the user to input values for the four important features and it will give the predictive sale price for that house.

![Predictive sale price](/images/readme_images/Prediction_sale_price.png)

## ML Business Case

1. What are the business requirements?

    * The client is interested in discovering how house attributes correlate with sale prices. Therefore, the client expects data visualizations of the correlated variables against the sale price.
    * The client is interested in predicting the house sale prices from her 4 inherited houses, and any other house in Ames, Iowa.

2. Is there any business requirement that can be answered with conventional data analysis?

    * Yes, we can use conventional data analysis to investigate how house attributes are correlated with the sale prices.

3. Does the client need a dashboard or an API endpoint?

    * The client needs a dashboard

4. What does the client consider as a successful project outcome?

    * A study showing the most relevant variables correlated to sale price.
    * Also, a capability to predict the sale price for the 4 inherited houses, as well as any other house in Ames, Iowa.

5. Can you break down the project into Epics and User Stories?

    * Information gathering and data collection.
    * Data visualization, cleaning, and preparation.
    * Model training, optimization and validation.
    * Dashboard planning, designing, and development.
    * Dashboard deployment and release.

6. Ethical or Privacy concerns?

    * No. The dataset given is a public dataset.

7. Does the data suggest a particular model?

    * The data suggests a regressor where the target is the sale price.

8. What are the model's inputs and intended outputs?

    * The inputs are house attribute information, and the output is the predicted sale price.

9. What are the criteria for the performance goal of the predictions?

    * We agreed with the client an R2 score of at least 0.75 on the train set as well as on the test set.

10. How will the client benefit?

    * The client will maximize the sales price for the inherited properties. And be able to expand their understanding for property sales in Ames, Iowa.

## Dashboard Design

At the top of each page, we have included text within a blue information box that gives a description of the page below.

### Project Summary

On this page we have given a brief description of the contents of the other pages as well as a quick description of the project dataset and the business requirements.

![Summary page part one](/images/readme_images/Summary_page_part_one.png)

![Summary page part two](/images/readme_images/Summary_page_part_two.png)

### Project Hypothesis and Validation

On this page we have each of our four hypothesis and the validation that we found for each.

![Hypothesis page part one](/images/readme_images/Hypothesis_page_part_one.png)

![Hypothesis page part two](/images/readme_images/Hypothesis_page_part_two.png)

### Sale Price Correlation Study

On this page we show the first 5 rows of the data frame which is shown when the user selects the 'Show data frame' button. We then state the six most correlated features to the sale price of a house. In the green box directly below we have written how each feature is correlated to the sale price. Finally, we have a checkbox that when ticked shows the correlated scatterplots between the features and the sale price.

![Correlation page part one](/images/readme_images/Correlation_page_part_one.png)

![Correlation page part two](/images/readme_images/Correlation_page_part_two.png)

![Correlation page part three](/images/readme_images/Correlation_page_part_three.png)

![Correlation page part four](/images/readme_images/Correlation_page_part_four.png)

![Correlation page part five](/images/readme_images/Correlation_page_part_five.png)

![Correlation page part six](/images/readme_images/Correlation_page_part_six.png)

![Correlation page part seven](/images/readme_images/Correlation_page_part_seven.png)

### Four Inherited Houses Sale Prices

On this page we have split the four inherited houses into their own section. In each section we display the predicted sale price for that house and a checkbox that when ticked shows the row for the corresponding house with all features present.

![Inherited page part one](/images/readme_images/Inherited_page_part_one.png)

![Inherited page part two](/images/readme_images/Inherited_page_part_two.png)

### Prediction Sale Prices

On this page we have added the widgets allowing the user to enter the features for any house they wish to find the predictive sale price in the Ames, Iowa area. Above each widget is the code name used in the data frame, the full title for the feature and for the numerical features the range they can enter in the widget. For the categorical question we have included a key below the widgets explaining what each option stands for. Then when the user clicks the 'Find the predicted sale price' button it gives the predicted sale price for that house.

![Prediction page part one](/images/readme_images/Prediction_page_part_one.png)

![Prediction page part two](/images/readme_images/Prediction_page_part_two.png)

### ML: Sale Price

On this page we have included the description of the pipelines steps as well as the graph showing the four most important features to the pipeline. Finally, we have included the Model evaluation for the user to review as well as a scatterplot for the prediction and actual sale price for the train set and test set.

![ML page part one](/images/readme_images/ML_page_part_one.png)

![ML page part two](/images/readme_images/ML_page_part_two.png)

![ML page part three](/images/readme_images/ML_page_part_three.png)

## Agile development

I recorded the steps I wished to take in a different document, but after I finished the streamlit pages, I moved the steps into the issue and project section of this repository.

![Project issues](/images/readme_images/issues.png)

## Unfixed Bugs

* Using the inbuilt python checker the only outstanding issue is the length of some of the lines of the code. I have reduced this across the code, but the length of the code doesn't affect the code running.
* I have performed rigorous manual testing of the streamlit pages, and no outstanding bugs are left.

## Deployment

### Heroku

* The App live link is: <https://YOUR_APP_NAME.herokuapp.com/>
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

* numpy - Used to perform mathematical operations.
* pandas - Used to display and manipulate the Data Frame.
* matplotlib - Used for data visualization e.g. histograms and scatterplots.
* seaborn - Used for data presentation e.g. heatmaps and scatterplots.
* pandas-profiling - Used to show an analysis of the Data Frame.
* ppscore - Used to find the predictive power score of the Data Frame.
* streamlit - Used to build the web app for the project.
* feature-engine - Used for data transformations.
* scikit-learn - Used for the machine learning models.
* xgboost - Used for regression classification.

## Credits

* Contents have been copied and some modified from the code institute churnometer walkthrough project. [Please click this link to find my copy of the walkthrough project.](https://github.com/HarveyBurton96/churnometer)
* [Stack Overflow](https://stackoverflow.com/) used for researching solutions to bugs in the code.
* The template for this repo provided by [code institute.](https://github.com/Code-Institute-Solutions/milestone-project-heritage-housing-issues)
* The code institute slack community also helped me with solutions to bugs in my code.
* Inspiration for the readme file from [Vasi012](https://github.com/Vasi012/PP5-Predictive-Analysis)
* The Crisp DM image is from [Data Science Process Alliance](https://www.datascience-pm.com/crisp-dm-2/)

## Acknowledgements

I would like to thank my mentor Marcel for his help during this project and a thanks to Niel McEwen for his help in the slack community.
