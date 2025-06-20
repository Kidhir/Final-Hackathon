# agents/roadmap_planning.py
from state import GraphState

def roadmap_planning_agent(state: GraphState) -> GraphState:
    """Generates a mock roadmap based on user feedback and competitors."""
    feedback = state.feature_requests or ["Fast login", "Dark mode"]
    competitors = state.competitor_features or ["Team chat", "Audit logs"]

    roadmap = {
        "Sprint 1": [feedback[0], competitors[0]],
        "Sprint 2": [feedback[1] if len(feedback) > 1 else "Performance tuning"],
    }

    state.roadmap = roadmap
    print("Draft roadmap:", roadmap)
    return state
