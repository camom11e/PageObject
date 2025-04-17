from .base_page import BasePage
from .register_form import RegisterModal
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import MainPageAuthorizationForm

class Main_Page(BasePage):
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "div.login_links.hidden-xs a[href='#modal_register']")
    AUTH_BUTTON = (By.CSS_SELECTOR, "div.login_links.hidden-xs a[href='#modal_login']")
    
    def open_registration_modal(self):
        register_btn = self.wait.until(
            EC.presence_of_element_located(self.REGISTRATION_BUTTON)
        )
        self.execute_script("arguments[0].scrollIntoView(true);", register_btn)
        self.execute_script("arguments[0].click();", register_btn)
        return RegisterModal(self.driver)
    
    def open_authorization_form(self):
        auth_btn = self.wait.until(
            EC.presence_of_element_located(self.AUTH_BUTTON)
        )
        self.execute_script("arguments[0].scrollIntoView(true);", auth_btn)
        self.execute_script("arguments[0].click();", auth_btn)
        return AuthorizationForm(self.driver)
    

class AuthorizationForm(BasePage):
	def fill_form(self, user_data):
		fields = {
            (By.CSS_SELECTOR, "input[type='email'][name='email'][class='form-control']"): user_data["email"],
            (By.CSS_SELECTOR, "input[name='password'][type='password'][class='form-control']"): user_data["password"]}
		
		for locator, value in fields.items():
				print(locator, ":", value)
				try:
					element = self.wait.until(
						EC.visibility_of_element_located(locator)
					)
					self.driver.execute_script(
						"arguments[0].value = arguments[1];", 
						element, 
						value
					)
					print(f"Field {locator[1]} filled with: {value}")
				except TimeoutException:
					print(f"Element {locator[1]} not found!")
					raise

	def push_button_login(self):
		self.driver.find_element(*MainPageAuthorizationForm.BUTTON_AUTHORIZATION).click()

	# def is_authorized(self):
	# 	time.sleep(15)
	# 	print(self.driver.find_element(*MainPageAuthorization.MAIN_PAGE_TITLE).text)