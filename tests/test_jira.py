import datetime
import os
from jira import JIRA
from dotenv import load_dotenv
from ..jira.jira_token import JIRA_TOKEN

load_dotenv(override=True)


JIRA_SERVER = os.getenv(JIRA_TOKEN.JIRA_WEBSIDE)
JIRA_USERNAME = os.getenv(JIRA_TOKEN.JIRA_EMAIL)
JIRA_API_KEY = os.getenv(JIRA_TOKEN.JIRA_API_TOKEN)

jira = JIRA(
    server=JIRA_SERVER,
    basic_auth=(JIRA_USERNAME, JIRA_API_KEY)
)

print(jira.projects())
print(jira.issue_types())

for i in jira.issue_types():
    if i.name.lower() in ["bug", "баг", "ошибка"]:
        bug_type = i

jira_issue = jira.create_issue(
    {
        "project": {"key": "SL"},
        "summary": "Задача тестовая",
        "description": f"Ошибка НАЗВАНИЕ_ОШИБКИ\n\nДата:  {datetime.datetime.now()}",
        "issuetype": {"id": "10038"}
    }
)

jira.add_attachment(jira_issue.key, "Безымянный.png")