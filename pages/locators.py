from selenium.webdriver.common.by import By


class MainPageLocators:
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "div.login_links.hidden-xs a[href='#modal_register']")
    AUTHORIZATION_BUTTON = (By.CSS_SELECTOR, "div.login_links.hidden-xs a[href='#modal_login']")

class MainPageAuthorizationForm():
	EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, "input[type='email'][name='email'][class='form-control']")
	PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, "input[name='password'][type='password'][class='form-control']")
	BUTTON_AUTHORIZATION = (By.CSS_SELECTOR, "#modal_login > div > div > div.modal-body > form > div:nth-child(5) > button > div")

class MainPageAuthorization():
	ONLY_LOCATOR_TITLE = ("#header > div.header_top > div > div > div > div.login_links.hidden-xs > a:nth-child(1) > span")
	MAIN_PAGE_TITLE_PRIVAT_ROOM = (By.XPATH, "//span[contains(text(), 'Личный кабинет')]")
	LOCATORS_BROKE = (By.XPATH, "//span[contains(text(), 'Личный кабинет аххаххахаха')]")
	LOCATOR_SEARCH = (By.XPATH, "//span[contains(text(), 'Личный кабинет аххаххахаха')]")
 
class MainPageRegistration():
    FIRST_NAME_INPUT_FIELD = (By.NAME, "first_name")
    LAST_NAME_INPUT_FIELD = (By.NAME, "last_name")
    PHONE_NAME_INPUT_FIELD = (By.CSS_SELECTOR, "input[name='phone'][type='tel']")
    EMAIL_NAME_INPUT_FIELD = (By.CSS_SELECTOR, "input[type='email'][name='email'][class='form-control required']")
    CITY_NAME_INPUT_FIELD = (By.CSS_SELECTOR, "input[name='city']")
    PASSWORD_NAME_INPUT_FIELD = (By.CSS_SELECTOR, "input[name='password'][type='password'][class='form-control required']")
    REPEAT_PASSWORD_NAME_INPUT_FIELD = (By.CSS_SELECTOR, "input[name='repeat_password'][type='password'][class='form-control required']")
    BUTTON_REGISTRATION = (By.CSS_SELECTOR,"#modal_register > div > div > div.modal-body > form > div:nth-child(12) > button > div")
    
class MyAccountPage():
    FILD_EMAIL = (By.CSS_SELECTOR,"#middle > div > div > div > div:nth-child(2) > div > div > div.col-lg-9.col-md-8.col-sm-12.col-xs-12 > div > div.dashboard > div.profile_info > div.email > span")
    FILD_PHONE_NUMBERS = (By.CSS_SELECTOR,"#middle > div > div > div > div:nth-child(2) > div > div > div.col-lg-9.col-md-8.col-sm-12.col-xs-12 > div > div.dashboard > div.profile_info > div.email > span" )
    #  test1745400594@example.com
     
 
 
