import pytest
from ..pages.main_page import MainPage
from jira import JIRA
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv(override=True)

JIRA_SERVER = os.getenv("JIRA_WEBSIDE")
JIRA_USERNAME = os.getenv("JIRA_EMAIL")
JIRA_API_KEY = os.getenv("JIRA_API_TOKEN")

jira = JIRA(
    server=JIRA_SERVER,
    basic_auth=(JIRA_USERNAME, JIRA_API_KEY)
)
def test_failed(browser):
    main_page = MainPage(browser)
    main_page.open()
    try:
        assert "UPPER"  in browser.page_source.lower()
    except AssertionError as e:
        print("Тест был специально провалем, для проверки соединения с JIRA!")
        print(jira.projects())
        print(jira.issue_types())
        for i in jira.issue_types():
            if i.name.lower() in ["bug", "баг", "ошибка"]:
                bug_type = i

        jira_issue = jira.create_issue(
            {
                "project": {"key": "SEL"},
                "summary": "Задача тестовая",
                "description": f"Проверка JIRA\n\nДата:  {datetime.now()}",
                "issuetype": {"id": "10038"}
            }
        )

        jira.add_attachment(jira_issue.key, "Скриншот_ошибки.png")
        raise e