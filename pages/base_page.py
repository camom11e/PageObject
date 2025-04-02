from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.base_url = "https://sibkofe.ru/"
    
    def open(self):
        self.driver.get(self.base_url)
    
    def execute_script(self, script, element=None):
        if element:
            return self.driver.execute_script(script, element)
        return self.driver.execute_script(script)
    
