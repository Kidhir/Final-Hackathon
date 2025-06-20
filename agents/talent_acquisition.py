# agents/talent_acquisition.py

import pdfplumber
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
    """Main agent to handle resume parsing, matching, and scoring."""
    resume_path = state.resume_path
    jd_text = state.job_description or "Looking for a Python developer with ML skills"

    # Fallback to mocked resumes
    if not state.resumes:
        state.resumes = [
            "Product Manager with Agile and Scrum experience",
            "Technical Lead with AI/ML background",
            "Business Analyst with SaaS and B2B focus"
        ]

    # Simulate scoring logic with integers out of 100
    scores = [90 - 10 * i for i in range(len(state.resumes))]  # ✅ Use full score
    state.ranked_candidates = [
        {"resume": r, "score": s}
        for r, s in zip(state.resumes, scores)
    ]

    # If PDF provided, parse and simulate match
    if resume_path:
        parsed = parse_resume(resume_path)
        resume_text = parsed.get("text", "")
        if "error" in parsed:
            state.notes = parsed["error"]
            return state

        match_score = sum(1 for word in jd_text.lower().split() if word in resume_text.lower())

        if match_score > 3:
            interview = schedule_interview("Jane Doe")
            state.recommendations = ["Jane Doe"]
            state.interview_details = interview
        else:
            state.recommendations = []
            state.interview_details = {}
            state.notes = "No strong match found from resume."
    return state
