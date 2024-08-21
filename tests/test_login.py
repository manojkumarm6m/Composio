import time

import pytest

from pages.login_page import LoginPage
import json


@pytest.mark.usefixtures("setup_teardown")
class TestLogin:
    def test_login_successful(self):
        pass
        # time.sleep(15)
        # title = self.driver.title
        # expected_title = "Get started"
        # assert expected_title == title, f"Expected title '{expected_title}' but got '{title}'"


