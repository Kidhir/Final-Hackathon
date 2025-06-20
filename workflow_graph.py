# workflow_graph.py

import sys
sys.setrecursionlimit(1000)  # ✅ Increases Python's recursion depth

from langgraph.graph import StateGraph
from state import GraphState

from agents.talent_acquisition import talent_acquisition_agent
from agents.roadmap_planning import roadmap_planning_agent
from agents.progress_monitoring import progress_monitoring_agent
from agents.gtm_strategy import gtm_strategy_agent
from agents.sales_feedback import sales_feedback_agent

# ✅ Initialize graph WITHOUT config
builder = StateGraph(GraphState)

# Register agents
builder.add_node("talent_agent", talent_acquisition_agent)
builder.add_node("roadmap_planner", roadmap_planning_agent)
builder.add_node("progress_monitor", progress_monitoring_agent)
builder.add_node("gtm_agent", gtm_strategy_agent)
builder.add_node("feedback_collector", sales_feedback_agent)

# Set edges
builder.set_entry_point("talent_agent")
builder.add_edge("talent_agent", "roadmap_planner")
builder.add_edge("roadmap_planner", "progress_monitor")
builder.add_edge("progress_monitor", "gtm_agent")

# Conditional flow to feedback agent
def condition_func(state: GraphState) -> str:
    return "continue" if state.sales_data else "stop"

builder.add_conditional_edges("gtm_agent", condition_func, {
    "continue": "feedback_collector",
    "stop": "feedback_collector"
})

# Finish point
builder.set_finish_point("feedback_collector")

# Compile graph
pm_graph = builder.compile()
