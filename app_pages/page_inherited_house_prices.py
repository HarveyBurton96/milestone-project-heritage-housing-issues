import streamlit as st
import pandas as pd
from src.predictive_model import predict_sale_price
from src.data_management import inherit_house_data, load_pkl_file


def page_inherited_body():

    df = inherit_house_data()
    house_one = df.iloc[[0]]
    house_two = df.iloc[[1]]
    house_three = df.iloc[[2]]
    house_four = df.iloc[[3]]

    features = ['OverallQual', 'TotalBsmtSF', '2ndFlrSF', 'GarageArea']

    version = 'v1'

    sale_price_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_sale_price/{version}/regressor_pipeline.pkl"
    )

    predict_house_one = predict_sale_price(
        house_one, features, sale_price_pipe)

    st.write(house_one)

    st.write(house_two)

    st.write(house_three)

    st.write(house_four)

    st.header("Four Inherited Houses Sale Prices")
