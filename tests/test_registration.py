# import pytest
# from selenium import webdriver
from ..pages.main_page import Main_Page
from ..pages.locators import MainPageRegistration, RegistarationPage
from ..pages.main_page import RegistrationForm
import time
import pytest

user_data = {
        "first_name": "Иван",
        "last_name": "Петров",
        "phone": "7913" + str(int(time.time()))[-7:],
        "email": f"test{int(time.time())}@example.com",
        "city": "Москва",
        "password": "Qwerty123!",
        "repeat_password": "Qwerty123!"
    }
@pytest.mark.parametrize("browser", ["chrome"], indirect=True)
def test_registration(browser, jira_client):
    print(user_data)
    main_page = Main_Page(browser)
    main_page.open()
    registration_form = main_page.open_registration_form()
    registration_form.fill_form(user_data)
    registration_form.push_button_registration()
    time.sleep(1000)
    # assert RE.is_element_present(*MainPageAuthorization.MAIN_PAGE_TITLE_PRIVAT_ROOM), "Есть кнопка личный кабинет"
    # assert registration_form.is_element_present(*RegistarationPage.FILD_EMAIL).getText()
    
#  test1744992540@example.com #middle > div > div > div > div:nth-child(2) > div > div > div.col-lg-9.col-md-8.col-sm-12.col-xs-12 > div > div.dashboard > div.profile_info > div.email > span
#79134992540 #middle > div > div > div > div:nth-child(2) > div > div > div.col-lg-9.col-md-8.col-sm-12.col-xs-12 > div > div.dashboard > div.profile_info > div.phone > span
# Иван Петров 


#     assert "успешно" in browser.page_source.lower()
    
    
    
# import pytest
# from ..pages.main_page import MainPage
# from ..pages.locators import MainPageAuthorization
# import time

# user_data = {
#         "email": f"test0123456789@example.com",
#         "password": "qwerty123"
#     }


# def test_authorization(browser, jira_client):
#     main_page = MainPage(browser)
#     main_page.open()
    
#     authorization_form = main_page.open_authorization_form()
#     authorization_form.fill_form(user_data)
#     authorization_form.push_button_login()
#     assert authorization_form.is_element_present(*MainPageAuthorization.MAIN_PAGE_TITLE_PRIVAT_ROOM), "Есть кнопка личный кабинет"
    
# def test_authorization_broke(browser, jira_client):
#     main_page = MainPage(browser)
#     main_page.open()
    
#     authorization_form = main_page.open_authorization_form()
#     authorization_form.fill_form(user_data)
#     authorization_form.push_button_login()
#     assert authorization_form.is_element_present(*MainPageAuthorization.LOCATORS_BROKE), "Это тест никогда не будет работать"

