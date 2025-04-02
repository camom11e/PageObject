import pytest
from selenium import webdriver
from ..pages.main_page import MainPage
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def user_data():
    return {
        "first_name": "Иван",
        "last_name": "Петров",
        "phone": "7913" + str(int(time.time()))[-7:],
        "email": f"test{int(time.time())}@example.com",
        "city": "Москва",
        "password": "Qwerty123!",
        "repeat_password": "Qwerty123!"
    }

def test_registration(browser, user_data):
    main_page = MainPage(browser)
    browser.get("https://sibkofe.ru/")
    
    register_modal = main_page.open_registration_modal()
    register_modal.fill_form(user_data)
    



    assert "успешно" in browser.page_source.lower()