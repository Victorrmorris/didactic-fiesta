import plotly.graph_objects as go

# Define budget and actual spending
budget = 3200  # Total budget
actual_spending = 3166  # Actual expenses

# Create gauge chart
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=actual_spending,
    title={"text": "Budget vs. Actual Spending"},
    gauge={
        "axis": {"range": [0, budget]},
        "bar": {"color": "blue"},  # Actual spending indicator
        "steps": [
            {"range": [0, budget * 0.7], "color": "lightgreen"},  # Safe zone
            {"range": [budget * 0.7, budget * 0.9], "color": "yellow"},  # Warning zone
            {"range": [budget * 0.9, budget], "color": "red"}  # Danger zone
        ],
        "threshold": {
            "line": {"color": "black", "width": 4},
            "thickness": 0.75,
            "value": actual_spending  # Mark actual spending
        }
    }
))

# Show the gauge chart
fig.show()
