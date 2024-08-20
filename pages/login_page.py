from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    USERNAME_FIELD = (By.NAME, 'login')  # Adjust locator as needed
    PASSWORD_FIELD = (By.NAME, 'password')  # Adjust locator as needed
    GIT_HUB_LOGIN = (By.XPATH, '//span[contains(text(), "Continue with Github")]')
    LOGIN_BUTTON = (By.NAME, 'commit')  # Adjust locator as needed

    def enter_username(self, username):
        self.enter_text(*self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.enter_text(*self.PASSWORD_FIELD, password)

    def click_login(self):
        self.click_element(*self.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_text(*self.USERNAME_FIELD, username)
        self.enter_text(*self.PASSWORD_FIELD, password)
        self.click_element(*self.LOGIN_BUTTON)

    def click_github(self):
        self.click_element(*self.GIT_HUB_LOGIN)
