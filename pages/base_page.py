from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout  # Default wait time is 10 seconds

    def find_element(self, by, value):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def find_elements(self, by, value):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_all_elements_located((by, value))
        )

    def click_element(self, by, value):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            element.click()
        except TimeoutException:
            print(f"Element with {by} = '{value}' was not clickable after {self.timeout} seconds")

    def enter_text(self, by, value, text):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            print(f"Element with {by} = '{value}' was not visible after {self.timeout} seconds")

    def wait_for_element_to_be_clickable(self, by, value):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((by, value))
        )

    def wait_for_element_to_be_visible(self, by, value):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((by, value))
        )

    def get_login_details(self):
        file_path = os.path.join(os.path.dirname(__file__), '../test_data/login_data.json')
        with open(file_path, 'r', encoding='utf-16') as file:
            data = json.load(file)
        return data["login_details"]["username"], data["login_details"]["password"]

    def wait_for_element_visible(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )
