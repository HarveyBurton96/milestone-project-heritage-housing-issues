import streamlit as st


def page_summary_body():
    st.header("Project Summary")

    st.info(
        f"Project Datasets\n\n"
        f"The dataset we are using represents the sale conditions of one house"
        f"contains overall condition of the property (like the Rating of "
        f"basement finished area, Interior finish of the garage, Kitchen "
        f"quality and Overall condition of the house) the year constructed "
        f"(like the Remodel date, Original construction date and the Year "
        f"garage was built) it also contians the square feet of the property "
        f"(like the First Floor square feet, Second-floor square feet and "
        f"Total square feet of basement area"
    )

    st.warning(
        f"Business requirement 1:\n\n"
        f"The client is interested in discovering how the house attributes "
        f"correlate with the sale price. Therefore, the client expects data "
        f"visualizations of the correlated variables against the sale price "
        f"to show that.\n\n"
        f"Business requirement 2:\n\n"
        f"The client is interested in predicting the house sales price from "
        f"her four inherited houses, and any other house in Ames, Iowa.\n"
    )

    st.write(
        f"For additional information about this project please read the "
        f"[Project README.](https://github.com/HarveyBurton96/milestone-project-heritage-housing-issues)"
    )
