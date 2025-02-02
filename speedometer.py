import streamlit as st
import plotly.graph_objects as go

# Define budget and actual spending
budget = 3200  # Total budget
actual_spending = 3166  # Actual expenses
percentage_spent = (actual_spending / budget) * 100  # Calculate percentage

# Create improved gauge chart
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=percentage_spent,
    title={"text": "Budget Utilization (%)"},
    gauge={
        "axis": {"range": [0, 100], "tickvals": [0, 50, 100], "ticktext": ["0%", "50%", "100%"]},
        "bar": {"color": "white"},  # White needle for better contrast
        "steps": [
            {"range": [0, 70], "color": "lightgreen"},  # Safe zone
            {"range": [70, 90], "color": "yellow"},  # Warning zone
            {"range": [90, 100], "color": "red"}  # Over-budget zone
        ],
        "threshold": {
            "line": {"color": "red", "width": 4},  # Red line as spending threshold
            "thickness": 0.8,
            "value": percentage_spent  # Show actual spending level
        }
    }
))

# Streamlit App
st.title("Personal Budget Tracker")
st.subheader("Gauge Chart - Budget Utilization")

# Display Plotly gauge chart in Streamlit
st.plotly_chart(fig)

# Add an explanation below the gauge chart
st.markdown("""
### **What Does This Mean?**
- You have spent **{:.1f}%** of your budget.
- The **green zone (0-70%)** means you're within a safe spending range.
- The **yellow zone (70-90%)** means you are nearing your budget limit.
- The **red zone (90-100%)** is a danger zone—you're at risk of overspending.
- The **white indicator** shows your current budget usage.
""".format(percentage_spent))
