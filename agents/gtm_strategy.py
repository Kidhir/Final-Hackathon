# agents/gtm_strategy.py
from langchain.agents import tool
from state import GraphState


def gtm_strategy_agent(state: GraphState) -> GraphState:
    """Creates a basic GTM plan based on features and personas."""
    roadmap = state.roadmap or {}
    key_features = list({f for s in roadmap.values() for f in s})[:3]
    personas = ["Startup CTO", "Product Manager"]

    content = f"Launch Campaign:\n- Features: {', '.join(key_features)}\n- Personas: {', '.join(personas)}\n- Launch date: Next Monday"
    state.gtm_assets = {"features": key_features, "personas": personas}
    state.launch_plan = content
    print(content)
    return state
