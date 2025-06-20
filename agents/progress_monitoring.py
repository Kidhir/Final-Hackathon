# agents/progress_monitoring.py
import os
import requests
from state import GraphState
from integrations.jira_reader import fetch_active_sprint_issues

def progress_monitoring_agent(state: GraphState) -> GraphState:
    """Reads real Jira sprint status and updates progress report."""
    try:
        issues = fetch_active_sprint_issues()

        if issues and "error" in issues[0]:
            state.progress_report = f"Jira error: {issues[0]['error']}"
            return state

        # Count issue status
        status_counts = {}
        for issue in issues:
            status = issue.get("status", "Unknown")
            status_counts[status] = status_counts.get(status, 0) + 1

        report_lines = [f"{k}: {v}" for k, v in status_counts.items()]
        summary = "\n".join(report_lines)

        # Simple logic to flag delays
        if status_counts.get("To Do", 0) > 2:
            delay_note = "🚨 Sprint at risk due to many unresolved tasks."
        else:
            delay_note = "✅ Sprint is on track."

        state.progress_report = f"Sprint Status:\n{summary}\n{delay_note}"
        return state

    except Exception as e:
        state.progress_report = f"Error fetching Jira sprint: {str(e)}"
        return state


def send_slack_alert(message: str):
    webhook = os.getenv("SLACK_WEBHOOK_URL")
    if webhook:
        try:
            requests.post(webhook, json={"text": message})
        except Exception as e:
            print(f"Slack alert failed: {e}")

def analyze_progress(sprint_data):
    delays = [i for i in sprint_data if i.get("status") not in ("Done", "Closed")]
    if delays:
        send_slack_alert("🚨 Sprint Alert: Some tasks are delayed in the active sprint!")
    return {
        "total": len(sprint_data),
        "delayed": len(delays),
        "summary": f"{len(delays)} delayed out of {len(sprint_data)}"
    }
