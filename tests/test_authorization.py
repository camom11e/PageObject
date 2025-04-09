import pytest
from ..pages.main_page import MainPage
from ..pages.locators import MainPageAuthorization
import time



@pytest.fixture
def user_data():
    return {
        "email": f"test0123456789@example.com",
        "password": "qwerty123"
    }

def test_authorization(browser, user_data, jira_client):
    main_page = MainPage(browser)
    main_page.open()
    
    authorization_form = main_page.open_authorization_form()
    authorization_form.fill_form(user_data)
    authorization_form.push_button_login()
    assert authorization_form.is_element_present(*MainPageAuthorization.MAIN_PAGE_TITLE_PRIVAT_ROOM), "Есть кнопка личный кабинет"
    

def test_authorization_broke(browser, user_data, jira_client):
    main_page = MainPage(browser)
    main_page.open()
    
    authorization_form = main_page.open_authorization_form()
    authorization_form.fill_form(user_data)
    authorization_form.push_button_login()
    assert authorization_form.is_element_present(*MainPageAuthorization.LOCATORS_BROKE), "Это тест никогда не будет работать"