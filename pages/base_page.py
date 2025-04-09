from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

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
    


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)

        except NoSuchElementException:
            return False

        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
