from .base_page import BasePage
from .locators import  MyAccountPage as MAP
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage



from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class My_Account_Page(BasePage):
    def return_be_email_in_profile(self):
        by, selector = MAP.FILD_EMAIL
        self.wait.until(
            EC.presence_of_element_located(MAP.FILD_EMAIL)
        )
        return self.driver.find_element(*MAP.FILD_EMAIL).text
	# def should_be_name_in_profile(self):
    #  assert self.driver.find_element(*MAP.FILD_EMAIL)