from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from selenium.common.exceptions import TimeoutException
from .locators import MainPageAuthorizationForm, MainPageAuthorization


class AuthorizationForm(BasePage):
	def fill_form(self, user_data):
		fields = {
            (By.CSS_SELECTOR, "input[type='email'][name='email'][class='form-control']"): user_data["email"],
            (By.CSS_SELECTOR, "input[name='password'][type='password'][class='form-control']"): user_data["password"]}
		
		for locator, value in fields.items():
				print(locator,":",value     )
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

	def is_authorized(self):
		print(self.driver.find_element(*MainPageAuthorization.MAIN_PAGE_TITLE).text)