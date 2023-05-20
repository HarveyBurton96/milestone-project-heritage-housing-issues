import streamlit as st


def page_hypothesis_body():
    st.header("Project Hypothesis and Validation")

    st.info(
        f"At the business understanding step we created four hypotheses to "
        f"test throughout the project. Please find each one and its resolution "
        f"below.")

    st.write("---")

    st.subheader("Hypothesis one:")

    st.write(
        f"The size of the first floor will have a greater impact on the "
        f"house sale than the size of the second floor.\n"
        f" - True, from the correlation study we can see that the size of "
        f"first floor has a greater impact on the house sale price than the "
        f"size of the second floor.")

    st.write("---")

    st.subheader("Hypothesis two:")

    st.write(
        f"The year the house was built will have a lower impact on the "
        f"sale price than the year the house was remodelled.\n"
        f"- False, from the correlation study we can see that the year the "
        f"house was built has a greater impact on the sale price than the "
        f"year the house was remodelled.")

    st.write("---")

    st.subheader("Hypothesis three:")

    st.write(
        f"The overall condition of the house will have a greater impact on "
        f"the sale price than the overall quality of the material and finish "
        f"of the house.\n"
        f"- False, from the correlation study we can see that the overall "
        f"quality of the material and finish of the house has a greater "
        f"impact on the sale price than the overall condition of the house.")

    st.write("---")

    st.subheader("Hypothesis four:")

    st.write(
        f"The size of the garage will have a greater impact on the sale "
        f"price than the size of the wood deck.\n"
        f"- True, from the correlation study we can see that the size of the "
        f"garage has a greater impact on the sale price than the size of the "
        f"wood deck.\n\n"
        f"---\n"
    )
