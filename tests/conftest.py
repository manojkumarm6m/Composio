import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from pages.login_page import LoginPage


@pytest.fixture(autouse=True)
def setup_teardown(request):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")  # Ensure headless mode for CI environments
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
    chrome_options.add_argument("--window-size=1920x1080")  # Set window size for headless mode

    # Initialize the WebDriver with ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Maximize window (not effective in headless mode but included for completeness)
    driver.maximize_window()

    # Assign the driver to the request's class to be accessible in tests
    request.cls.driver = driver

    # Perform the login process
    driver.get("https://app.composio.dev/")
    login_page = LoginPage(driver)
    user_name, password = login_page.get_login_details()
    login_page.click_github()
    login_page.login(user_name, password)

    yield

    # Teardown: Quit the WebDriver session
    driver.quit()
