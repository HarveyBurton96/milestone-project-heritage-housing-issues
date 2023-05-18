import streamlit as st


def predict_sale_price(df, important_features, sale_price_pipeline):

    df_features = df.filter(important_features)

    sale_price_prediction = sale_price_pipeline.predict(df_features)

    clean = int(sale_price_prediction[0].round())

    st.write(
        f"The predicted Sale Price for this property is ${clean}")
