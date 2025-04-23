from selenium.webdriver.common.by import By


class MainPageLocators:
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "div.login_links.hidden-xs a[href='#modal_register']")
    AUTHORIZATION_BUTTON = (By.CSS_SELECTOR, "div.login_links.hidden-xs a[href='#modal_login']")
    SEARCH_FIELD = (By.CSS_SELECTOR, "#woocommerce-product-search-field-0")
    SEARCH_BUTTON =  (By.CSS_SELECTOR, "#header > div.header_top > div > div > div > div.header_search > a > span")
    SEARCH_BUTTON_IN_SEARCH_BUTTON = (By.CSS_SELECTOR,"#header > div.header_top > div > div > div > div.header_search > div > form > button")

class MainPageAuthorizationForm():
	EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, "input[type='email'][name='email'][class='form-control']")
	PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, "input[name='password'][type='password'][class='form-control']")
	BUTTON_AUTHORIZATION = (By.CSS_SELECTOR, "#modal_login > div > div > div.modal-body > form > div:nth-child(5) > button > div")

class MainPageAuthorization():
	ONLY_LOCATOR_TITLE = ("#header > div.header_top > div > div > div > div.login_links.hidden-xs > a:nth-child(1) > span")
	MAIN_PAGE_TITLE_PRIVAT_ROOM = (By.XPATH, "//span[contains(text(), 'Личный кабинет')]")
	LOCATORS_BROKE = (By.XPATH, "//span[contains(text(), 'Личный кабинет аххаххахаха')]")
 
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
    
class ProductPage():
    ADD_TO_CARD = (By.CSS_SELECTOR, "#product-152358 > div.summary.entry-summary.product_content.col-lg-7.col-md-7.col-sm-7.col-xs-12 > form > div.single_variation_wrap > div > button")

class ProductAddToCardForm():
    PRODUCT_TITLE =(By.CSS_SELECTOR,"#modal_add_to_cart > div > div > div.modal-header > div > span.product_title")
    CLOSE_FORM_LOCATOR = (By.CSS_SELECTOR,"#modal_add_to_cart > div > div > div.modal-header > button") 
