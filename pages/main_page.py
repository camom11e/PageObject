from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import MainPageAuthorizationForm as MPAUF , MainPageLocators as MPL, MainPageRegistration as MPR
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from selenium.common.exceptions import TimeoutException

class Main_Page(BasePage):
    def open_registration_form(self):
        register_btn = self.wait.until(
            EC.presence_of_element_located(MPL.REGISTRATION_BUTTON)
        )
        self.execute_script("arguments[0].scrollIntoView(true);", register_btn)
        register_btn.click()
        # elem = self.driver.find_element(*MPL.REGISTRATION_BUTTON)/
        # text = elem.text
        # self.execute_script("arguments[0].click();", register_btn)
        return RegistrationForm(self.driver)
    
    def open_authorization_form(self):
        auth_btn = self.wait.until(
            EC.presence_of_element_located(MPL.AUTHORIZATION_BUTTON)
        )
        self.execute_script("arguments[0].scrollIntoView(true);", auth_btn)
        self.execute_script("arguments[0].click();", auth_btn)
        return AuthorizationForm(self.driver)
    

class AuthorizationForm(Main_Page):
	def fill_form(self, user_data):
		fields = {
            MPAUF.EMAIL_INPUT_FIELD : user_data["email"],
            MPAUF.PASSWORD_INPUT_FIELD : user_data["password"]
        }
		
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
		self.driver.find_element(*MPAUF.BUTTON_AUTHORIZATION).click()

	# def is_authorized(self):
	# 	time.sleep(15)
	# 	print(self.driver.find_element(*MainPageAuthorization.MAIN_PAGE_TITLE).text)
 
 
class RegistrationForm(Main_Page):
    def fill_form(self, user_data):
        fields = {
            MPR.FIRST_NAME_INPUT_FIELD: user_data["first_name"],
            MPR.LAST_NAME_INPUT_FIELD: user_data["last_name"],
            MPR.PHONE_NAME_INPUT_FIELD: user_data["phone"],
            MPR.EMAIL_NAME_INPUT_FIELD: user_data["email"],
            MPR.CITY_NAME_INPUT_FIELD: user_data["city"],
            MPR.PASSWORD_NAME_INPUT_FIELD: user_data["password"],
            MPR.REPEAT_PASSWORD_NAME_INPUT_FIELD: user_data["repeat_password"]
        }
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
    def push_button_registration(self):
        print(self.driver.find_element(*MPR.BUTTON_REGISTRATION).text)
        self.driver.find_element(*MPR.BUTTON_REGISTRATION).click()
            
        
    # def is_success_message_present(self):
    #     try:
    #         self.find_element(self.SUCCESS_MESSAGE)
    #         return True
    #     except:
    #         return False

