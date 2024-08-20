import time

import pytest

from pages.connected_accounts_page import ConnectedAccounts
from pages.login_page import LoginPage
import json


@pytest.mark.usefixtures("setup_teardown")
class TestConnectedAccounts:

    def test_login_successful(self):
        contd_ac = ConnectedAccounts(self.driver)
        contd_ac.click_connected_accounts()
        # contd_ac.click_click_here_to_connect()
        # contd_ac.click_github()
        # contd_ac.setup_git_hub_integration()
        # contd_ac.connect_to_github()
        # contd_ac.close()
        contd_ac.click_github()
        contd_ac.execute_actions()


