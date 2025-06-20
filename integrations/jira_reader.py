import os
import requests
from typing import List, Dict
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()

JIRA_BASE_URL = os.getenv("JIRA_BASE_URL", "").replace("\\", "").strip().rstrip("/")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
JIRA_PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY", "KAN")

AUTH = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
HEADERS = {"Accept": "application/json"}

# Optional: show what URL is being hit
print("DEBUG: Using JIRA_BASE_URL =", JIRA_BASE_URL)


def fetch_active_sprint_issues() -> List[Dict]:
    """Fetch issues from the latest active sprint on board ID 1"""
    board_id = 1  # ✅ Explicitly use board ID 1

    try:
        sprint_url = f"{JIRA_BASE_URL}/rest/agile/1.0/board/{board_id}/sprint?state=active"
        sprints_resp = requests.get(sprint_url, headers=HEADERS, auth=AUTH)
        sprints_resp.raise_for_status()
        sprints_data = sprints_resp.json()
        sprint_id = sprints_data.get("values", [{}])[0].get("id")
        if not sprint_id:
            return [{"error": "No active sprints found."}]
    except Exception as e:
        return [{"error": f"Failed to fetch active sprint: {e}"}]

    try:
        issues_url = f"{JIRA_BASE_URL}/rest/agile/1.0/sprint/{sprint_id}/issue"
        issues_resp = requests.get(issues_url, headers=HEADERS, auth=AUTH)
        issues_resp.raise_for_status()
        issues_data = issues_resp.json()
        issues = issues_data.get("issues", [])
    except Exception as e:
        return [{"error": f"Failed to fetch sprint issues: {e}"}]

    return [
        {
            "key": issue.get("key"),
            "summary": issue["fields"]["summary"],
            "status": issue["fields"]["status"]["name"]
        } for issue in issues
    ]
