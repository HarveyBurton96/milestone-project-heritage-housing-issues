import streamlit as st


def page_summary_body():
    st.header("Project Summary")

    st.info("This page gives a light overview of the project goals and the contents of the other pages.")

    st.write("---")

    st.subheader("Contents")

    st.write(
        f"- Project Hypothesis and Validation: Contains information on the hypotheses we created at the Business understanding stage and the resolutions.\n"
        f"- Sale Price Correlation Study: Looks at the correlation between the features in the data frame and the sale price.\n"
        f"- Four Inherited Houses Sale Prices: Shows the predicted sale price for the four inherited houses.\n"
        f"- Prediction Sale Prices: Allows the user to enter the features and predict any houses sale price in Ames, Iowa.\n"
        f"- ML: Sale Price: Shows a technical evaluation of the pipeline.\n"
        f"---"
    )

    st.subheader("Project Datasets")

    st.write(
        f"The dataset we are using represents the sale conditions of one house "
        f"contains overall condition of the property (like the Rating of "
        f"basement finished area, Interior finish of the garage, Kitchen "
        f"quality and Overall condition of the house) the year constructed "
        f"(like the Remodel date, Original construction date and the Year "
        f"garage was built) it also contains the square feet of the property "
        f"(like the First Floor square feet, Second-floor square feet and "
        f"Total square feet of basement area.\n\n"
        f"---"
    )

    st.subheader("Business requirement 1:")

    st.write(
        f"The client is interested in discovering how the house attributes "
        f"correlate with the sale price. Therefore, the client expects data "
        f"visualizations of the correlated variables against the sale price "
        f"to show that.\n\n"
        f"---")

    st.subheader("Business requirement 2:")

    st.write(
        f"The client is interested in predicting the house sales price from "
        f"her four inherited houses, and any other house in Ames, Iowa.\n\n"
        f"---"
    )

    st.write(
        f"For additional information about this project please read the "
        f"[Project README.](https://github.com/HarveyBurton96/milestone-project-heritage-housing-issues)"
    )
