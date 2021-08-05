import time

import allure
from seleniumbase import BaseCase
from locators.home import Home
from locators.tracking_app import TrackingApp


class TrackingAppPage:
    """
    Tracking app page
    """

    def __init__(self, driver):
        self.driver = BaseCase(driver)

    @allure.step("go to tracking app page")
    def go_to_tracking_app_page(self):
        self.driver.click(Home.tracking_app_menu)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(TrackingApp.header_title_txt) == 'AfterShip tracking app'
        card_headers = self.driver.find_visible_elements(TrackingApp.card_header_title_txt)
        assert card_headers[0].text == 'Benefit'
        assert card_headers[1].text == 'Here’s what it’ll look like'
