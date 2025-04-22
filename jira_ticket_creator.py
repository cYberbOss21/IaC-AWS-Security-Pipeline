import os
import json
import requests
from dotenv import load_dotenv

# Load credentials from .env
load_dotenv(dotenv_path=os.path.expanduser("~/.jira_secrets.env"))

JIRA_URL = os.getenv("JIRA_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
JIRA_PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY")

auth = (JIRA_EMAIL, JIRA_API_TOKEN)
headers = {
    "Content-Type": "application/json"
}

# Load Checkov scan results
with open("checkov_results.json", "r") as f:
    findings = json.load(f)

# Create a ticket for each failed check
for result in findings:
    title = f"{result['check_id']} - {result['check_name']}"
    desc = f"""
Resource: {result['resource']}
File: {result['file_path']}
Line: {result['file_line_range']}
Check Type: {result['check_type']}
Guideline: {result.get('guideline', 'N/A')}
"""

    payload = {
        "fields": {
            "project": {"key": JIRA_PROJECT_KEY},
            "summary": title,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": desc
                            }
                        ]
                    }
                ]
            },
            "issuetype": {"name": "Task"}
        }
    }

    response = requests.post(
        f"{JIRA_URL}/rest/api/3/issue",
        headers=headers,
        json=payload,
        auth=auth
    )

    if response.status_code == 201:
        print(f"[+] Created Jira ticket: {title}")
    else:
        print(f"[!] Failed to create ticket: {title}")
        print("Response:", response.status_code, response.text)
