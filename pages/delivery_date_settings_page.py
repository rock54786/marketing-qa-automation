import json
import time

import allure
from seleniumbase import BaseCase

from locators.analytics import Analytics
from locators.customer_reviews import CustomerReviews
from locators.delivery_date_settings import DeliveryDateSettings
from locators.home import Home
from locators.order_lookup_widget import OrderLookupWidget


class DeliveryDateSettingsPage:
    """
    Delivery date settings
    """

    def __init__(self, driver):
        self.base = driver
        self.driver = BaseCase(driver)

    @allure.step("go to Delivery date settings page")
    def go_to_delivery_date_settings_page(self):
        self.driver.click(Home.delivery_date_settings_menu)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(DeliveryDateSettings.header_title_txt) == 'Promised delivery date'
        self.driver.wait_for_element_visible("h2:contains('Promised delivery date')")
        self.driver.wait_for_element_visible("h2:contains('Order cutoff & processing time')")
        self.driver.wait_for_element_visible("h2:contains('Transit time')")


