from src.data_management import load_house_data
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)

sns.set_style("whitegrid")


def page_correlation_body():

    df = load_house_data()

    vars_to_study = ['1stFlrSF', 'GarageArea', 'GrLivArea',
                     'OverallQual', 'TotalBsmtSF', 'YearBuilt']

    st.header("Sale Price Correlation Study")

    st.info(
        f"One of our business requirements was that the client is interested "
        f"in discovering how the house attributes correlate with the sale price."
    )

    if st.button("Show data frame"):
        st.write(df.head())

    st.write(
        f"In the jupyter notebooks we have run a correlation study to "
        f"understand which features correlate the best to Sale price of the "
        f"house.\n\n"
        f"The features with the highest correlation are:\n"
        f"- {vars_to_study}"
    )

    st.success(
        f"When we plotted the above features against the sale price below, we "
        f"were able to make the interpretation:\n"
        f"- The sale price is typically higher the greater the first floor "
        f"square feet is.\n"
        f"- The sale price is typically higher the greater the garage square "
        f"feet is.\n"
        f"- The sale price is typically higher the greater the above ground "
        f"living area square feet is.\n"
        f"- The sale price is typically higher the better the overall "
        f"materials and finish of the house is.\n"
        f"- The sale price is typically higher the greater the total square "
        f"feet of the basement area is.\n"
        f"- The sale price is typically higher the new the house is.\n"
    )

    df_eda = df.filter(vars_to_study + ['SalePrice'])
    target_var = 'SalePrice'

    def plot_numerical(df, col, target_var):
        plt.figure(figsize=(10, 5))
        sns.lmplot(data=df, x=col, y=target_var, truncate=False)
        plt.title(f"{col}", fontsize=20, y=1.05)
        st.pyplot()

    if st.checkbox(
        "Show the correlated features against the sale price plots."
    ):
        for col in vars_to_study:
            plot_numerical(df_eda, col, target_var)
            print("\n\n")
            if col == '1stFlrSF':
                st.write(
                    'We can see in the plot above that as the Sale Price increase so does the size of the first floor.')
            elif col == 'GarageArea':
                st.write(
                    'We can see in the plot above that as the Sale Price increase so does the size of the garage.')
            elif col == 'GrLivArea':
                st.write(
                    'We can see in the plot above that as the Sale Price increase so does the size of the above ground living area.')
            elif col == 'OverallQual':
                st.write(
                    'We can see in the plot above that as the Sale Price increase so does the overall finish of the house improves.')
            elif col == 'TotalBsmtSF':
                st.write(
                    'We can see in the plot above that as the Sale Price increase so does the size of the basement.')
            elif col == 'YearBuilt':
                st.write(
                    'We can see in the plot above that as the Sale Price increase the new the year the house was built is.')
            st.write('---')
