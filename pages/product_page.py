from .base_page import BasePage
from .locators import ProductPage as PR, ProductAddToCardForm as PATCF
from selenium.webdriver.support import expected_conditions as EC


class Product_page(BasePage):
    def add_to_card(self):
        self.wait.until(EC.presence_of_element_located(PR.ADD_TO_CARD))
        self.driver.find_element(*PR.ADD_TO_CARD).click()
        return FormAddProductPage(self.driver)

class FormAddProductPage(BasePage):
    
    def checkProductTitle(self, nameProuct):
        self.wait.until(EC.presence_of_element_located(PATCF.PRODUCT_TITLE).text)
        print(EC.presence_of_element_located(PATCF.PRODUCT_TITLE).text)
        assert  EC.presence_of_element_located(PATCF.PRODUCT_TITLE).text == nameProuct
    
    def closeForm(self):
        self.driver.find_element(*PATCF.CLOSE_FORM_LOCATOR).click()
        return Product_page(self.driver)
        