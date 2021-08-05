import json
import time

import allure
from seleniumbase import BaseCase

from locators.analytics import Analytics
from locators.customer_reviews import CustomerReviews
from locators.home import Home
from locators.order_lookup_widget import OrderLookupWidget


class OrderLookupWidgetPage:
    """
    Order Lookup Widget
    """

    def __init__(self, driver):
        self.base = driver
        self.driver = BaseCase(driver)

    @allure.step("go to Order lookup widget page")
    def go_to_Order_lookup_widget_page(self):
        self.driver.click(Home.order_lookup_widget_menu)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(OrderLookupWidget.header_title_txt) == 'Order lookup widget (Track button)'
        self.driver.wait_for_element_visible("h2:contains('Customize order lookup widget')")
        self.driver.wait_for_element_visible("h2:contains('Preview')")



