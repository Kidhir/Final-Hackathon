# state.py
from pydantic import BaseModel
from typing import Optional, List, Dict

class GraphState(BaseModel):
    # Talent Acquisition Agent
    resume_path: Optional[str] = None
    job_description: Optional[str] = None
    resumes: Optional[List[str]] = None
    recommendations: Optional[List[str]] = []
    interview_details: Optional[Dict] = {}
    notes: Optional[str] = None
    ranked_candidates: Optional[List[Dict]] = None  # ✅ Fix for Talent Agent output

    # Roadmap Planning Agent
    feature_requests: Optional[List[str]] = None
    market_research: Optional[str] = None
    team_capacity: Optional[str] = None
    roadmap: Optional[Dict] = None
    competitor_features: Optional[List[str]] = None

    # Progress Monitoring Agent
    sprint_progress: Optional[str] = None
    delay_risk: Optional[str] = None
    progress_report: Optional[str] = None

    # GTM Strategy Agent
    launch_plan: Optional[str] = None
    campaign_kit: Optional[List[str]] = None
    gtm_assets: Optional[Dict] = None

    # Sales & Feedback Agent
    sales_data: Optional[Dict] = None
    user_feedback: Optional[List[str]] = None
    improvement_suggestions: Optional[List[str]] = None
    feedback_summary: Optional[str] = None

    # Shared State
    iteration_count: Optional[int] = 0
