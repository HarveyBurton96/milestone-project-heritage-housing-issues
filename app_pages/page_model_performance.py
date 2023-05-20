import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file
from src.evaluate_ml import regression_performance


def page_model_body():

    version = 'v1'

    sale_price_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_sale_price/{version}/regressor_pipeline.pkl"
    )
    sale_price_importance = plt.imread(
        f"outputs/ml_pipeline/predict_sale_price/{version}/features_importance.png"
    )
    x_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv"
    )
    x_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/X_test.csv"
    )
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/Y_train.csv"
    )
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/Y_test.csv"
    )

    st.header("ML: Sale Price")

    st.info("Add text about model here")

    st.write("---")

    st.write(sale_price_pipe)

    st.write("---")

    st.image(sale_price_importance)

    st.write("---")

    regression_performance(x_train, y_train, x_test,
                           y_test, sale_price_pipe)
