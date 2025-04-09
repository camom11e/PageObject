import pytest
from ..pages.main_page import MainPage



@pytest.fixture
def user_data():
    return {
        "email": f"test0123456789@example.com",
        "password": "0123456789"
    }

def test_authorization(browser, user_data, jira_client):
    main_page = MainPage(browser)
    main_page.open()
    
    authorization_form = main_page.open_authorization_form()
    authorization_form.fill_form(user_data)
    authorization_form.push_button_login()

    authorization_form.is_authorized()
    

def test_authorization_second(browser, user_data, jira_client):
    main_page = MainPage(browser)
    main_page.open()
    
    authorization_form = main_page.open_authorization_form()
    authorization_form.fill_form(user_data)
    authorization_form.push_button_login()


    try:
        assert "личный кабинет хахахахах"  in browser.page_source.lower()
    except AssertionError as e:
        print("у вас ошибка")
        raise e