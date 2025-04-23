from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import MainPageAuthorizationForm as MPAUF , MainPageLocators as MPL, MainPageRegistration as MPR
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .my_account_page import My_Account_Page
from selenium.common.exceptions import TimeoutException

class Main_Page(BasePage):
    def open_registration_form(self):
        register_btn = self.wait.until(
            EC.presence_of_element_located(MPL.REGISTRATION_BUTTON)
        )
        register_btn.click()
        return RegistrationForm(self.driver)
    
    def open_authorization_form(self):
        auth_btn = self.wait.until(
            EC.presence_of_element_located(MPL.AUTHORIZATION_BUTTON)
        )
        auth_btn.click()
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
					self.wait.until(EC.visibility_of_element_located(locator)).send_keys(value)
					print(f"Field {locator[1]} filled with: {value}")
				except TimeoutException:
					print(f"Element {locator[1]} not found!")
					raise

	def push_button_login(self):
		self.driver.find_element(*MPAUF.BUTTON_AUTHORIZATION).click()

	# def is_authorized(self):
	# 	time.sleep(15)
	# 	print(self.driver.find_element(*MainPageAuthorization.MAIN_PAGE_TITLE).text)
 
 
class RegistrationForm(BasePage):
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
                self.wait.until(EC.visibility_of_element_located(locator)).send_keys(value)
                print(f"Field {locator[1]} filled with: {value}")
            except TimeoutException:
                print(f"Element {locator[1]} not found!")
                raise
    def push_button_registration(self):
        print(self.driver.find_element(*MPR.BUTTON_REGISTRATION).text)
        self.driver.find_element(*MPR.BUTTON_REGISTRATION).click()
        return My_Account_Page(self.driver)
            
        
    # def is_success_message_present(self):
    #     try:
    #         self.find_element(self.SUCCESS_MESSAGE)
    #         return True
    #     except:
    #         return False

