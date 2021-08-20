import time
from seleniumbase import By
import allure
from seleniumbase import BaseCase
from locators.store import Store
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from locators.shippment import Shipment


class StorePage:
    """
    主页
    """

    def __init__(self, driver):
        self.base = driver
        self.driver = BaseCase(driver)

    @allure.step("go to popup tab")
    def login_in(self):
        self.driver.type(Store.store_password, "1")
        self.driver.click(Store.store_password_confirm)

    @allure.step("check popup header")
    def check_popup_header(self):
        self.driver.sleep(5)
        self.driver.switch_to_frame(Store.popup_iframe)
        a = self.driver.get_text(Store.popup_header)
        print(a)
        self.driver.assert_text("Automizely Header Test: Get $10.00 OFF your first order!", Store.popup_header)

    @allure.step("check popup description")
    def check_popup_description(self):
        self.driver.assert_text\
            ("Automizely Description Test: Join our email list to receive updates and exclusive offers.", Store.popup_description)
