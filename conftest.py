import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from datetime import datetime
import pytest
import os
from selenium import webdriver
from jira import JIRA
from dotenv import load_dotenv

load_dotenv(override=True)

JIRA_SERVER = os.getenv("JIRA_WEBSIDE")
JIRA_USERNAME = os.getenv("JIRA_EMAIL")
JIRA_API_KEY = os.getenv("JIRA_API_TOKEN")

@pytest.fixture
def browser(request):
    hub_url = "http://10.11.23.230:5555/wd/hub"
    param = request.param if hasattr(request, "param") else "chrome"
    if param == "chrome":
        language = request.config.getoption("languages")
        options = ChromeOptions()
        options.page_load_strategy = 'normal'
        # 'normal' для обычной загрузки страницы
        # 'eager'  для не ожидает загрузки всей странции 
        # 'none'   для отсутствия ожидания 
        options.add_experimental_option("prefs", {"intl.accept_languages": language})
    elif param == "firefox":
        options = FirefoxOptions()
    else:
        options = EdgeOptions()

    browser = webdriver.Remote(
        command_executor=hub_url,
        options=options
    )

    yield browser

    browser.quit()


def pytest_addoption(parser):
    parser.addoption("--languages", action="store", default="ru", help="Выберите язык")
    parser.addoption("--jira", action="store_true", help="Включить интеграцию с Jira")

@pytest.fixture(scope="session")
def jira_client(request):
    if request.config.getoption("jira"):
        jira = JIRA(
            server=JIRA_SERVER,
            basic_auth=(JIRA_USERNAME, JIRA_API_KEY)
        )
        return jira


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and (report.outcome == "failed" or (hasattr(report, "wasxfail") and report.outcome == "passed")):
        if "browser" in item.funcargs:
            browser = item.funcargs["browser"]
            browser.save_screenshot("Скриншот_ошибки.png")

        if "jira_client" in item.funcargs:
            jira = item.funcargs["jira_client"]
            if jira:
                issue_type = jira.issue_types()
                bug_type = issue_type[4]

                issue_dict = {
                    "project": {"key": "SEL"},
                    "summary": f"{item.name}",
                    "description": f"Ошибка: {report.longreprtext}\n\nДата: {datetime.now()}",
                    "issuetype": {"id": bug_type.id}
                }

                new_issue = jira.create_issue(fields=issue_dict)
                jira.add_attachment(new_issue.key, "Скриншот_ошибки.png")