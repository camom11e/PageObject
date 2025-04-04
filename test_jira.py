import datetime
from jira import JIRA
import conftest

jira = JIRA(
    server=conftest.JIRA_SERVER,
    basic_auth=(conftest.JIRA_USERNAME, conftest.JIRA_API_KEY)
)

print(jira.projects())
print(jira.issue_types())

for i in jira.issue_types():
    if i.name.lower() in ["bug", "баг", "ошибка"]:
        bug_type = i

jira_issue = jira.create_issue(
    {
        "project": {"key": "SEL"},
        "summary": "Задача тестовая",
        "description": f"Ошибка НАЗВАНИЕ_ОШИБКИ\n\nДата:  {datetime.datetime.now()}",
        "issuetype": {"id": "10038"}
    }
)

jira.add_attachment(jira_issue.key, "Безымянный.png")