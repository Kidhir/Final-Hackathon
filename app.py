# app.py
import streamlit as st
from workflow_graph import pm_graph
from state import GraphState

st.set_page_config(page_title="🧠 PM Agent Workflow")
st.title("🧠 AI-Powered PM Agent")

# UI inputs
job_description = st.text_area("📄 Job Description", height=100)
resumes = st.text_area("👥 Candidate Resumes (1 per line)", height=150)

# Trigger agents
if st.button("🚀 Run Agent Workflow"):
    with st.spinner("Running agents..."):
        state = GraphState(
            job_description=job_description,
            resumes=resumes.splitlines(),
            iteration_count=0  # Ensure initialized
        )

        raw_output = pm_graph.invoke(state)
        final_state = GraphState(**raw_output)  # ✅ Properly convert output

        st.subheader("👥 Talent Acquisition")
        if final_state.ranked_candidates:
            for cand in final_state.ranked_candidates:
                st.markdown(f"- **{cand['resume']}** — Score: {cand['score']}")

        st.subheader("🗺 Roadmap Plan")
        if final_state.roadmap:
            for sprint, features in final_state.roadmap.items():
                st.markdown(f"**{sprint}**: {', '.join(features)}")

        st.subheader("📊 Sprint Progress Report")
        st.text(final_state.progress_report)

        st.subheader("🚀 GTM Launch Plan")
        st.text(final_state.launch_plan)

        st.subheader("🔁 Feedback & Suggestions")
        if final_state.improvement_suggestions:
            for suggestion in final_state.improvement_suggestions:
                st.markdown(f"- {suggestion}")
