import streamlit as st
import pandas as pd
import numpy as np

st.title("Empirical Table Testing Software")
st.write(
    "Use this software to numerically help you decide upon subsystem designs! I hope it helps :)"
   # "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

ratings = st.select_slider(
    "Rate the practicality of the subsystem out of 10",
    options=[
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10"
    ],
)



# Title
st.title("Design Scoring Tool")

# Ask user for the number of subsystem options
num_subsystems = st.number_input("Enter the number of subsystem options:", min_value=1, max_value=10, value=3)
num_factors = st.number_input("Enter the number of factors for each subsystem:", min_value=1, max_value=10, value=3)
# Create an editable DataFrame for user input


for subsystem in range(1, num_subsystems + 1):
    st.subheader(f"Subsystem {subsystem}")

    # Create a new editable DataFrame for each subsystem
    input_data = {
        "Factor": [f"Factor {i+1}" for i in range(num_factors)],
        "Weight (%)": [20] * num_factors,  # Default weight set to 20%
        "Rating (1-10)": [5] * num_factors,  # Default rating set to 5
    }

    df = pd.DataFrame(input_data)

    # Allow user to edit the table for each subsystem with a unique key
    df = st.data_editor(df, use_container_width=True, key=f"data_editor_{subsystem}")

    # Calculate weighted scores
    df["Weighted #"] = df["Rating (1-10)"] * (df["Weight (%)"] / 100)

    # Display the formatted table
    st.write("### Evaluation Table")
    st.write(df)

    # Display the total sum of weighted scores
    total_weighted_score = df["Weighted #"].sum()
    st.write(f"### Total Sum of Weighted Scores: {total_weighted_score:.2f}")