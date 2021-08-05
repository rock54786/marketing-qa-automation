import json
import time

import allure
from seleniumbase import BaseCase

from locators.apps import Apps
from locators.connections import Connections
from locators.home import Home


class AppsPage:
    """
    apps
    """

    def __init__(self, driver):
        self.base = driver
        self.driver = BaseCase(driver)

    @allure.step("go to apps page")
    def go_to_apps_page(self):
        self.driver.click(Home.apps_menu)
        self.driver.switch_to_newest_window()
        self.driver.wait_for_ready_state_complete()
        self.driver.sleep(2)
        assert self.driver.get_text(Apps.header_title_txt) == 'Apps'




