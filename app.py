import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.page_summary import page_summary_body
from app_pages.page_hypothesis import page_hypothesis_body
from app_pages.page_correlation_sale_price import page_correlation_body
from app_pages.page_inherited_house_prices import page_inherited_body
from app_pages.page_predictive_prices import page_predictive_body
from app_pages.page_model_performance import page_model_body

app = MultiPage(app_name="Heritage Housing Issues")

app.app_page("Project Summary", page_summary_body)
app.app_page("Project Hypothesis and Validation", page_hypothesis_body)
app.app_page("Sale Price Correlation Study", page_correlation_body)
app.app_page("Four Inherited Houses Sale Prices", page_inherited_body)
app.app_page("Prediction Sale Prices", page_predictive_body)
app.app_page("ML: Sale Price", page_model_body)

app.run()
