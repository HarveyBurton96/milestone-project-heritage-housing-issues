import streamlit as st


def page_hypothesis_body():
    st.header("Project Hypothesis and Validation")

    st.success(
        f"1. The size of the first floor will have a greater impact on the "
        f"house sale than the size of the second floor.\n"
        f" - True, from the correlation study we can see that the size of first "
        f"floor has a greater impact on the house sale price than the size of the "
        f"second floor.\n\n"

        f"2. The year the house was built will have a lower impact on the sale "
        f"price than the year the house was remodelled.\n"
        f"- False, from the correlation study we can see that the year the "
        f"house was built has a greater impact on the sale price than the year "
        f"the house was remodelled.\n\n"

        f"3. The overall condition of the house will have a greater impact on "
        f"the sale price than the overall quality of the material and finish of "
        f"the house.\n"
        f"- False, from the correlation study we can see that the overall "
        f"quality of the material and finish of the house has a greater impact "
        f"on the sale price than the overall condition of the house.\n\n"

        f"4. The size of the garage will have a greater impact on the sale "
        f"price than the size of the wood deck.\n"
        f"- True, from the correlation study we can see that the size of the "
        f"garage has a greater impact on the sale price than the size of the wood deck."
    )
