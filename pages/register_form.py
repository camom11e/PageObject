from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from selenium.common.exceptions import TimeoutException

class RegisterModal(BasePage):
    def fill_form(self, user_data):
        fields = {
            (By.NAME, "first_name"): user_data["first_name"],
            (By.NAME, "last_name"): user_data["last_name"],
            (By.CSS_SELECTOR, "input[name='phone'][type='tel']"): user_data["phone"],
            (By.CSS_SELECTOR, "input[type='email'][name='email'][class='form-control required']"): user_data["email"],
            (By.CSS_SELECTOR, "input[name='city']"): user_data["city"],
            (By.CSS_SELECTOR, "input[name='password'][type='password'][class='form-control required']"): user_data["password"],
            (By.CSS_SELECTOR, "input[name='repeat_password'][type='password'][class='form-control required']"): user_data["repeat_password"]
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


