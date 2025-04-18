import pytest
from ..pages.main_page import AuthorizationForm
from ..pages.main_page import Main_Page
from ..pages.locators import MainPageAuthorization
import time

user_data = {
        "email": f"test0123456789@example.com",
        "password": "qwerty123"
    }

@pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
def test_authorization(browser, jira_client):
    main_page = Main_Page(browser)
    main_page.open()
    
    authorization_form = main_page.open_authorization_form()
    authorization_form.fill_form(user_data)
    authorization_form.push_button_login()
    assert authorization_form.is_element_present(*MainPageAuthorization.MAIN_PAGE_TITLE_PRIVAT_ROOM), "Есть кнопка личный кабинет"
    
def test_authorization_broke(browser, jira_client):
    main_page = Main_Page(browser)
    main_page.open()
    
    authorization_form = main_page.open_authorization_form()
    authorization_form.fill_form(user_data)
    authorization_form.push_button_login()
    assert authorization_form.is_element_present(*MainPageAuthorization.LOCATORS_BROKE), "Это тест никогда не будет работать"