import pytest

@pytest.fixture
def login_data():
    return {
        "email": "test123@example.com",  # Замените на реальный email
        "password": "Password123!"   # Замените на реальный пароль
    }

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