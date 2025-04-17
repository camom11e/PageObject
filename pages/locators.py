from selenium.webdriver.common.by import By

class MainPageAuthorizationForm():
	EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, "input[type='email'][name='email'][class='form-control']")
	PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, "input[name='password'][type='password'][class='form-control']")
	BUTTON_AUTHORIZATION = (By.CSS_SELECTOR, "#modal_login > div > div > div.modal-body > form > div:nth-child(5) > button > div")

class MainPageAuthorization():
	ONLY_LOCATOR_TITLE = ("#header > div.header_top > div > div > div > div.login_links.hidden-xs > a:nth-child(1) > span")
	MAIN_PAGE_TITLE_PRIVAT_ROOM = (By.XPATH, "//span[contains(text(), 'Личный кабинет')]")
	LOCATORS_BROKE = (By.XPATH, "//span[contains(text(), 'Личный кабинет аххаххахаха')]")
	LOCATOR_SEARCH = (By.XPATH, "//span[contains(text(), 'Личный кабинет аххаххахаха')]")
