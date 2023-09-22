import os
import time
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import datetime


class OpenAICore:
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    def __init__(self, url_path):
        self.url_path = url_path
        self.driver = None

    def start_browser(self):
        try:
            options = Options()
            options.add_argument('--headless=new')

            # Инициализация WebDriver
            s = Service(executable_path=ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=s, options=options)
            self.driver.set_window_size(1920, 1080)
        except Exception as e:
            not_cd = 'Не удается найти или получить драйвер для Chrome! Введите корректный путь к ChromeDriver!'
            raise Exception(not_cd + str(e))


    def open_open_ai(self):
        try:
            # Открытие веб-сайта
            self.driver.get(self.url_path)

        except Exception as e:
            raise Exception("Ошибка при открытии веб-сайта: " + str(e))

    def auth_mail(self, email):
        try:
            wait = WebDriverWait(self.driver, 25)
            input_email_xpath = '//input[@name="username"]'
            input_email = wait.until(EC.presence_of_element_located((By.XPATH, input_email_xpath)))
            input_email.send_keys(email)
            time.sleep(1)
            input_email.send_keys(Keys.ENTER)
        except Exception as ex:
            print(f'Ошибка ввода email => {ex}')

    def auth_pass(self, password):
        try:
            wait = WebDriverWait(self.driver, 25)
            input_password_xpath = '//input[@name="password"]'
            input_password = wait.until(EC.presence_of_element_located((By.XPATH, input_password_xpath)))
            input_password.send_keys(password)
            input_password.send_keys(Keys.ENTER)
            time.sleep(1)
        except Exception as ex:
            print(f'Ошибка ввода password => {ex}')

    def check_auth(self):
        try:
            error_mess = self.driver.find_element(By.CLASS_NAME, 'ulp-input-error-message')
            return error_mess
        except Exception as ex:
            return False

    def get_cookie_auth(self):
        try:
            coockie_auth = self.driver.get_cookies()[0]['value']
            str(coockie_auth)
            return coockie_auth
        except Exception as ex:
            print(f'Ошибка получения куки: {ex}')

    def close_browser(self):
        try:
            if self.driver:
                self.driver.quit()
        except Exception as e:
            raise Exception(f"[{self.formatted_datetime}] Ошибка при закрытии браузера: " + str(e))
