import pytest
from selenium import webdriver


@pytest.fixture
def login_data():
    return {
        "email": "test123@example.com",  
        "password": "Password123!"
        }

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()



def pytest_terminal_summary(terminalreporter):
    passed = terminalreporter.stats.get('passed', [])
    failed = terminalreporter.stats.get('failed', [])
    
    with open("report.txt", "w") as f:
        if passed:
            f.write("Пройденные тесты:\n")
            for test in passed:
                f.write(f"- {test.nodeid}\n")
        if failed:
            f.write("\nПроваленные тесты:\n")
            for test in failed:
                f.write(f"- {test.nodeid}\n")

def pytest_addoption():
    pass
#фикстура
def jira_client(request):
    if request.config.getoption("jira"):
        pass