from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ConnectedAccounts(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    CONNECTED_ACCOUNTS = (By.XPATH, '//span[text()="Connected accounts"]')
    CLICK_HERE_TO_CONNECT = (By.XPATH, '//a[text()="Click here"]')
    GITHUB_TEXT = (By.XPATH, '//div[text()="Github"]')
    SETUP_GIT_HUB = (By.XPATH, '//div[contains(text(),"Setup")]')
    SETUP_INTEGRATION_SAVE = (By.XPATH, '//button[contains(text(),"Save")]')
    CONNECT_TO_GITHUB = (By.XPATH, '//button[contains(text(), "Connect to ")]')
    CLOSE = (By.XPATH, "//div[contains(@class, 'hover:bg-red') and contains(@class, 'cursor-pointer')]")
    EXECUTE_ACTIONS = (By.XPATH, '//button[text()="Execute actions"]')
    EXECUTION_SUCCESS = (By.XPATH, '//div[text()="Request was sent successfully"]')

    def click_connected_accounts(self):
        self.click_element(*self.CONNECTED_ACCOUNTS)

    def click_github(self):
        self.click_element(*self.GITHUB_TEXT)

    def execute_actions(self):
        self.click_element(*self.EXECUTE_ACTIONS)

    def click_here(self):
        self.click_element(*self.CLICK_HERE_TO_CONNECT)

    def setup_git_hub_integration(self):
        self.click_element(*self.SETUP_GIT_HUB)

    def save_setup_integration(self):
        self.click_element(*self.SETUP_INTEGRATION_SAVE)

    def connect_to_github(self):
        self.click_element(*self.CONNECT_TO_GITHUB)

    def close(self):
        self.click_element(*self.CLOSE)

    def wait_for_element(self):
        return self.element_displayed(*self.EXECUTION_SUCCESS)

