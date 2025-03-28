import time
import random
from .base_page import BasePage
from selenium.webdriver.common.by import By

class RegisterPage(BasePage):
    def pull_registers_button(self):
        try:
            # 1. Находим все кнопки отправки формы внутри элементов с классом form-group
            buttons = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".form-group button[type='submit']")))
            # 2. Перебираем кнопки и ищем ту, у которой текст "Зарегистрироваться"
            for button in buttons:
                if button.text.strip() == "Зарегистрироваться":
                    #3. Нажимаем на кнопку
                    button.click()
                    print("Кнопка 'Зарегистрироваться' успешно нажата!")
                    break  # Останавливаем цикл после нажатия
            else:  # Если цикл завершился без break (кнопка не найдена)
                print("Кнопка 'Зарегистрироваться' не найдена.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    
    def register_new_user(self, email=None, password="Test1234!"):
        self.pull_registers_button()
        return email
    
    def is_success_message_present(self):
        try:
            self.find_element(self.SUCCESS_MESSAGE)
            return True
        except:
            return False