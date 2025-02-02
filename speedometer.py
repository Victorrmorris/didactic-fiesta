import streamlit as st
import plotly.graph_objects as go

# Define categories and spending values
categories = ["Income", "Rent", "Groceries", "Utilities", "Entertainment", "Education", "Transportation"]
amounts = [3200, 1800, 846, 179, 155, 124, 63]  # Budget allocation

# Define source (where the money is coming from) and target (where it's going)
source = [0, 0, 0, 0, 0, 0]  # All expenses come from "Income"
target = [1, 2, 3, 4, 5, 6]  # The corresponding spending categories

# Create Sankey diagram
fig = go.Figure(go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=categories,
        color=["blue", "red", "green", "purple", "orange", "cyan", "pink"]
    ),
    link=dict(
        source=source,
        target=target,
        value=amounts[1:],  # Exclude income since it's the source
        color=["red", "green", "purple", "orange", "cyan", "pink"]
    )
))

# Streamlit App
st.title("Personal Budget Tracker")
st.subheader("Sankey Diagram - Budget Allocation")

# Display Plotly Sankey chart in Streamlit
st.plotly_chart(fig)

# Add an explanation below the Sankey diagram
st.markdown("""
### **How to Read This Sankey Diagram**
- The **left side (Income)** represents the total available budget ($3200).
- The **flows (arrows)** show how money is allocated across different spending categories.
- The **thicker arrows** indicate higher spending amounts (e.g., Rent takes the largest portion).
- The **right side (categories)** represents where your money is being spent.
""")
