import json
import time

import allure
from seleniumbase import BaseCase

from locators.apps import Apps
from locators.connections import Connections
from locators.home import Home


class ReferToEarnPage:
    """
    apps
    """

    def __init__(self, driver):
        self.base = driver
        self.driver = BaseCase(driver)

    @allure.step("Refer to earn page")
    def go_to_refer_to_earn_page(self):
        self.driver.click(Home.refer_to_earn_menu)
        self.driver.switch_to_newest_window()
        self.driver.wait_for_ready_state_complete()
        self.driver.sleep(2)
        assert self.driver.get_text(Apps.header_title_txt) == 'Refer & earn rewards (AfterShip & Returns Center only)'




