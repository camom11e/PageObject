import pytest
from selenium import webdriver
from ..pages.main_page import MainPage
import time

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
--
def test_registration(browser, user_data):
    main_page = MainPage(browser)
    main_page.open()
    
    register_modal = main_page.open_registration_modal()
    register_modal.fill_form(user_data)
    



    assert "успешно" in browser.page_source.lower()
    
    
    
import pytest
from ..pages.main_page import MainPage
from ..pages.locators import MainPageAuthorization
import time

user_data = {
        "email": f"test0123456789@example.com",
        "password": "qwerty123"
    }


def test_authorization(browser, jira_client):
    main_page = MainPage(browser)
    main_page.open()
    
    authorization_form = main_page.open_authorization_form()
    authorization_form.fill_form(user_data)
    authorization_form.push_button_login()
    assert authorization_form.is_element_present(*MainPageAuthorization.MAIN_PAGE_TITLE_PRIVAT_ROOM), "Есть кнопка личный кабинет"
    
def test_authorization_broke(browser, jira_client):
    main_page = MainPage(browser)
    main_page.open()
    
    authorization_form = main_page.open_authorization_form()
    authorization_form.fill_form(user_data)
    authorization_form.push_button_login()
    assert authorization_form.is_element_present(*MainPageAuthorization.LOCATORS_BROKE), "Это тест никогда не будет работать"