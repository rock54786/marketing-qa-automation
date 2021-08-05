import json
import time

import allure
from seleniumbase import BaseCase
from locators.connections import Connections
from locators.home import Home


class ConnectionsPage:
    """
    Delivery date settings
    """

    def __init__(self, driver):
        self.base = driver
        self.driver = BaseCase(driver)

    @allure.step("go to Connections page")
    def go_to_connections_page(self):
        self.driver.click(Home.connections_menu)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Connections.header_title_txt) == 'Connections'
        self.driver.sleep(2)
        assert len(self.driver.find_visible_elements(Connections.table_rows)) > 0

    @allure.step("add connection")
    def add_connection(self):
        self.driver.click(Home.connections_menu)
        self.driver.wait_for_ready_state_complete()
        self.driver.sleep(2)
        self.driver.click(Connections.add_connections)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Connections.header_title_txt) == 'Apps'

