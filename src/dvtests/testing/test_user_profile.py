from time import sleep

import pytest
from selenium.webdriver.common.by import By

from ..conftest import login_normal_user


class TestUserProfile:
    def test_user_profile_navigate(self, test_config, config, browser):
        if not test_config["tests"]["user-profile-navigate"]["test"]:
            pytest.skip("Test not configured to be executed.")

        for name, driver in browser.items():
            driver = login_normal_user(
                driver, test_config, config, config.USER_NORMAL, config.USER_NORMAL_PWD,
            )

            assert test_config["instance"]["title"] == driver.title
            driver.find_element(By.ID, "userDisplayInfoTitle").click()
            sleep(3)
            driver.find_element(By.LINK_TEXT, "My Data").click()
            sleep(3)
            assert (
                test_config["tests"]["user-profile-navigate"]["title"] == driver.title
            )
            driver.find_element(By.LINK_TEXT, "Notifications").click()
            sleep(3)
            driver.find_element(By.LINK_TEXT, "Account Information").click()
            sleep(3)
            driver.find_element(By.LINK_TEXT, "API Token").click()
            sleep(3)
