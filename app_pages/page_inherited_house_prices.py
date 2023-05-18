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

    st.header("Four Inherited Houses Sale Prices")

    st.write("---")

    st.subheader("First inherited house")

    predict_sale_price(house_one, features, sale_price_pipe)

    if st.checkbox("See a breakdown of the the first house features"):
        st.write(house_one)

    st.write("---")

    st.subheader("Second inherited house")

    predict_sale_price(house_two, features, sale_price_pipe)

    if st.checkbox("See a breakdown of the the second house features"):
        st.write(house_two)

    st.write("---")

    st.subheader("Third inherited house")

    predict_sale_price(house_three, features, sale_price_pipe)

    if st.checkbox("See a breakdown of the the third house features"):
        st.write(house_three)

    st.write("---")

    st.subheader("Fourth inherited house")

    predict_sale_price(house_four, features, sale_price_pipe)

    if st.checkbox("See a breakdown of the the fourth house features"):
        st.write(house_four)
