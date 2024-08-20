import time

import pytest

from pages.login_page import LoginPage
import json


@pytest.mark.usefixtures("setup_teardown")
class TestLogin:
    def test_login_successful(self):
        # login_page = LoginPage(self.driver)
        # user_name, password = login_page.get_login_details()
        # login_page.click_github()
        # login_page.login(user_name, password)
        time.sleep(15)
        title = self.driver.title
        expected_title = "Get started"
        assert expected_title == title, f"Expected title '{expected_title}' but got '{title}'"


