from selenium.webdriver.common.by import By

class MainPageAuthorizationForm():
	EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, "input[type='email'][name='email'][class='form-control']")
	PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, "input[name='password'][type='password'][class='form-control']")
	BUTTON_AUTHORIZATION = (By.CSS_SELECTOR, "#modal_login > div > div > div.modal-body > form > div:nth-child(5) > button")

class MainPageAuthorization():
	MAIN_PAGE_TITLE = (By.CSS_SELECTOR, "#header > div.header_top > div > div > div > div.login_links.hidden-xs > a:nth-child(1) > span")