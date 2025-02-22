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

weight = 0
# Function to generate dynamic columns based on user input
def generate_inputs(num_factors):
    factors = []
    for i in range(num_factors):
        factor_name = st.text_input(f"Enter the name for Factor {i+1}", f"Factor {i+1}")
        score = st.slider(f"{factor_name} Rating (1-10)", 1, 10, 5)
        weight = st.slider(f"Set weight for {factor_name} (%)", 1, 100, 20)  # Weights in percentage (1-100)
        factors.append((factor_name, score, weight))
    return factors

# Title
st.title("Dynamic Design Scoring Tool with Weights")

# Ask the user for the number of factors
num_factors = st.number_input("How many factors would you like to rate?", min_value=1, max_value=10, value=3)

# Generate the inputs
factors = generate_inputs(num_factors)

# Create a DataFrame to store the data
factor_names = [factor[0] for factor in factors]
scores = [factor[1] for factor in factors]
weights = [factor[2] for factor in factors]

# Calculate weighted scores
weighted_scores = [score * (weight / 100) for score, weight in zip(scores, weights)]
total_weighted_score = sum(weighted_scores)

#if (sum(weights) != 100):
   # total_weighted_score == sum of weighted score/total weights



# Create a DataFrame to display the results in a table
df = pd.DataFrame({
    'Factor': factor_names,
    'Rating (1-10)': scores,
    'Weight (%)': weights,
    'Weighted Score': weighted_scores
})

# Display the table
st.write("### Design Score Summary")
st.write(df)

# Display the total weighted score
st.write(f"### Total Weighted Score: {total_weighted_score:.2f}")




