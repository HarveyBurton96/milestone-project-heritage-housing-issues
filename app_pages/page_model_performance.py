import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file
from src.evaluate_ml import regression_performance


def page_model_body():

    version = 'v3'

    sale_price_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_sale_price/{version}/regressor_pipeline.pkl"
    )
    sale_price_importance = plt.imread(
        f"outputs/ml_pipeline/predict_sale_price/{version}/features_importance.png"
    )
    evaluation_plot = plt.imread(
        f"outputs/ml_pipeline/predict_sale_price/{version}/evaluation_plot.png"
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

    st.info(
        f"We have used a Regressor model to predict the Sale price of a house."
        f" The business requirement for our model was to achieve an R2 score "
        f"greater or equal to 0.75, our model on the train and test data was "
        f"able to achieve an R2 score over 0.8 meaning our model successfully "
        f"fulfilled our business requirement."
    )

    st.write("---")

    st.subheader(
        "ML pipeline to predict the sale price of a house sold in Ames, Iowa")

    st.write(f"{sale_price_pipe}")

    st.write("---")

    st.subheader("Important features")
    st.write(
        f"The features: OverallQual, TotalBsmtSF, 2ndFlrSF and GarageArea. "
        f"Where used to train the model and the graph below shows us their "
        f"importance."
    )

    st.image(sale_price_importance)

    st.write("---")

    st.subheader("Model Evaluation")

    regression_performance(x_train, y_train, x_test,
                           y_test, sale_price_pipe)

    st.image(evaluation_plot)
