import streamlit as st
import plotly.graph_objects as go

# Define categories and spending values
categories = ["Income", "Rent", "Groceries", "Utilities", "Entertainment", "Education", "Transportation"]
amounts = [3200, 1800, 846, 179, 155, 124, 63]  # Budget allocation

# Define source (income) and target (spending categories)
source = [0, 0, 0, 0, 0, 0]  # Income flows to each category
target = [1, 2, 3, 4, 5, 6]  # Corresponding spending categories
colors = ["#007bff", "#ff4b5c", "#28a745", "#ffcc00", "#ff7f0e", "#17becf", "#9467bd"]  # Custom color palette

# Create Sankey diagram
fig = go.Figure(go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=categories,
        color=colors  # Assigning distinct colors
    ),
    link=dict(
        source=source,
        target=target,
        value=amounts[1:],  # Exclude income (source)
        color=[colors[i] for i in range(1, len(colors))]  # Match category colors
    )
))

# Streamlit App Layout
st.title("💰 Personal Budget Tracker")
st.subheader("📊 Sankey Diagram - Where Your Money Goes")

# Display Plotly Sankey chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Add a clear explanation below the Sankey diagram
st.markdown("""
### **How to Read This Sankey Diagram**
🔹 The **left side (Income)** represents your total budget ($3200).  
🔹 The **flows (arrows)** show how money is distributed across different spending categories.  
🔹 The **thicker the arrow, the higher the spending** (e.g., Rent takes the biggest portion).  
🔹 The **colors help differentiate categories**, making it easy to track where money is going.  

💡 **Tip:** If your "Rent" arrow is too thick, consider adjusting your housing expenses.  
""")
