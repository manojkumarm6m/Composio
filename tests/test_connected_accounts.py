import time

import pytest
from pages.connected_accounts_page import ConnectedAccounts


@pytest.mark.usefixtures("setup_teardown")
class TestConnectedAccounts:

    def test_login_successful(self):
        contd_ac = ConnectedAccounts(self.driver)
        time.sleep(5)
        contd_ac.click_connected_accounts()
        contd_ac.click_github()
        contd_ac.execute_actions()

