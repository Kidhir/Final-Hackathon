# agents/talent_acquisition.py

import pdfplumber
from pydantic import BaseModel  # ✅ Add this import
from state import GraphState

def parse_resume(file_path: str) -> dict:
    try:
        with pdfplumber.open(file_path) as pdf:
            text = "\n".join(page.extract_text() or "" for page in pdf.pages)
        return {"text": text}
    except Exception as e:
        return {"error": str(e)}

def schedule_interview(candidate_name: str, time_slot: str = "Tomorrow 3 PM") -> dict:
    return {
        "candidate": candidate_name,
        "slot": time_slot,
        "zoom_link": f"https://zoom.us/fake/{candidate_name.lower().replace(' ', '-')}"
    }

def talent_acquisition_agent(state: GraphState) -> GraphState:
    """Main agent to handle resume, matching, and scheduling."""
    resume_path = state.resume_path or "resumes/sample.pdf"
    jd_text = state.job_description or "Looking for a Python developer with ML skills"

    parsed = parse_resume(resume_path)
    resume_text = parsed.get("text", "")

    if "error" in parsed:
        state.recommendations = []
        state.interview_details = {}
        state.notes = parsed["error"]
        return state

    # Simulate candidate match (simple keyword match)
    match_score = 0
    for word in jd_text.lower().split():
        if word in resume_text.lower():
            match_score += 1

    if match_score > 3:
        interview = schedule_interview("Jane Doe")
        state.recommendations = ["Jane Doe"]
        state.interview_details = interview
    else:
        state.recommendations = []
        state.interview_details = {}
        state.notes = "No strong match found."

    return state
