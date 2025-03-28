from .base_page import BasePage
from .register_modal import RegisterModal
from .auth_modal import AuthModal
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    REGISTER_BUTTON = (By.CSS_SELECTOR, "div.login_links.hidden-xs a[href='#modal_register']")
    AUTH_BUTTON = (By.CSS_SELECTOR, "div.login_links.hidden-xs a[href='#modal_login']")
    
    def open_registration_modal(self):
        register_btn = self.wait.until(
            EC.presence_of_element_located(self.REGISTER_BUTTON)
        )
        self.execute_script("arguments[0].scrollIntoView(true);", register_btn)
        self.execute_script("arguments[0].click();", register_btn)
        return RegisterModal(self.driver)
    
    def open_auth_modal(self):
        auth_btn = self.wait.until(
            EC.presence_of_element_located(self.AUTH_BUTTON)
        )
        self.execute_script("arguments[0].scrollIntoView(true);", auth_btn)
        self.execute_script("arguments[0].click();", auth_btn)
        return AuthModal(self.driver)