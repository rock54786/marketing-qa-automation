import time

import allure
from seleniumbase import BaseCase
from locators.home import Home
from locators.shippment import Shipment


class HomePage:
    """
    主页
    """

    def __init__(self, driver):
        self.driver = BaseCase(driver)

    @allure.step("go to Shipments page")
    def go_to_shipments_page(self):
        self.driver.click(Home.shipment_menu)
        self.driver.wait_for_element_visible(Shipment.add_shipment_btn)

    @allure.step("go to home page")
    def go_to_home_page(self):
        self.driver.click(Home.home_menu)
        self.driver.click(Home.home_menu) #总会有一次点击不生效的情况
        self.driver.wait_for_element_visible(Home.welcome_title_txt)

    @allure.step("go to notifications page")
    def go_to_notifications_page(self):
        self.driver.click(Home.notifications_menu)
