import streamlit as st
import pandas as pd
from src.predictive_model import predict_sale_price
from src.data_management import load_house_data, load_pkl_file


def page_predictive_body():

    features = ['OverallQual', 'TotalBsmtSF', '2ndFlrSF', 'GarageArea']

    version = 'v3'

    sale_price_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_sale_price/{version}/regressor_pipeline.pkl"
    )

    st.header("Prediction Sale Prices")

    st.info(
        f"One this screen you can enter different values for the key features "
        f"to determin what any house in Ames, Iowa would sell for.\n\n"
        f"For the section below each widget is for one of the key features of "
        f"the model. When you click the 'Find the predicted sale price' button"
        f" the model will tell you the predicted sale price for a house with "
        f"the features you have input. You can change the values of the inputs"
        f" to see how the feature affects the sale price.\n\n")

    st.write("---")

    live_house = DrawInputWidgets()

    if st.button("Find the predicted sale price"):
        predict_sale_price(live_house, features, sale_price_pipe)

    st.write("---")

    st.success(
        f"OverallQual - Key:\n"
        f"- 1: Very Poor\n"
        f"- 2: Poor\n"
        f"- 3: Fair\n"
        f"- 4: Below Average\n"
        f"- 5: Average\n"
        f"- 6: Above Average\n"
        f"- 7: Good\n"
        f"- 8: Very Good\n"
        f"- 9: Excellent\n"
        f"- 10: Very Excellent"
    )


def DrawInputWidgets():

    df = load_house_data()
    percentageMin = 0.4
    percentageMax = 2.0

    col1, col2 = st.beta_columns(2)
    col3, col4 = st.beta_columns(2)

    live_house = pd.DataFrame([], index=[0])

    with col1:
        feature = 'OverallQual'
        st_widget = st.selectbox(
            label=f"Rates the overall material and finish of the house - {feature}. Please see the key below.",
            options=df[feature].unique()
        )
    live_house[feature] = st_widget

    with col2:
        feature = 'TotalBsmtSF'
        st_widget = st.number_input(
            label=f"Total square feet of basement area - {feature}. The range is: 0 - 12220",
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    live_house[feature] = st_widget

    with col3:
        feature = '2ndFlrSF'
        st_widget = st.number_input(
            label=f"Second-floor square feet - {feature}. The range is : 0 - 4130",
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    live_house[feature] = st_widget

    with col4:
        feature = 'GarageArea'
        st_widget = st.number_input(
            label=f"Size of garage in square feet - {feature}. The range is : 0 - 2836",
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    live_house[feature] = st_widget

    return live_house
