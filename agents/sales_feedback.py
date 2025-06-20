# agents/sales_feedback.py

from state import GraphState
import random

def sales_feedback_agent(state: GraphState) -> GraphState:
    """Simulates feedback collection and maps it to improvement ideas."""

    # Simulated dummy reviews and feedback
    reviews = state.user_feedback or [
        "Love the UI, but too slow on mobile.",
        "Export feature is missing!",
        "Great product, but onboarding is confusing."
    ]

    # Dummy sales data simulation
    sales_data = {"Q1": 12000, "Q2": 18500, "Q3": 20000}

    # Simple sentiment mapping to feature improvement
    suggestions = [
        "Improve dashboard speed",
        "Add CSV/Excel export options",
        "Introduce in-app onboarding tutorial"
    ]

    # Slack notification example
    import requests, os
    slack_url = os.getenv("SLACK_WEBHOOK_URL")
    if slack_url:
        try:
            requests.post(slack_url, json={"text": "📊 Sales & feedback agent completed analysis."})
        except Exception as e:
            print(f"Slack error: {e}")

    # Update state
    state.sales_data = sales_data
    state.user_feedback = reviews
    state.improvement_suggestions = suggestions

    # DEBUG
    print("✅ Sales & feedback analysis done.")
    return state
