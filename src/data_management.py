import streamlit as st
import pandas as pd
import joblib


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_house_data():
    df = pd.read_csv("outputs/datasets/collection/HousePricesRecords.csv")
    return df


def inherit_house_data():
    df_inherit = pd.read_csv("inputs/datasets/raw/house-price-20211124T154130Z-001/house-price/inherited_houses.csv")
    return df_inherit


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)
