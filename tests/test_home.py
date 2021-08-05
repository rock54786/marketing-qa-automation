import allure
import pytest
from seleniumbase import BaseCase

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.shipment_page import ShipmentPage
from locators.home import Home
import os


@allure.feature("Home page")
class TestHome:
    @classmethod
    @pytest.fixture(scope="function", autouse=True)
    def setup(cls, base_driver):
        """
        前置步骤
        :return:
        """
        cls.login_page = LoginPage(base_driver)
        cls.home_page = HomePage(base_driver)
        cls.shipment_page = ShipmentPage(base_driver)
        cls.driver = BaseCase(base_driver)

    @allure.story("正常展示welcome title")
    def test_welcome_title_100627(self):
        self.login_page.login_in()
        assert self.driver.get_text(Home.welcome_title_txt) == "Welcome, autotestaftership"

    @allure.story("正确显示当前org plan")
    def test_plan_100628(self):
        self.login_page.login_in()
        assert self.driver.get_text(Home.plan_txt) == "Pro 5K - Monthly"

    @allure.story("当前已用quota数值正确")
    def test_quota_usage_100629(self):
        self.login_page.login_in()
        usage = int(str(self.driver.get_text(Home.quote_usage_txt)).split(" ")[0])
        self.home_page.go_to_shipments_page()
        self.shipment_page.add_shipment()
        self.home_page.go_to_home_page()
        new_usage = 0
        for i in range(30):
            self.driver.wait_for_element_visible(Home.quote_usage_txt)
            new_usage = int(str(self.driver.get_text(Home.quote_usage_txt)).split(" ")[0])
            if new_usage == usage + 1:
                break
            else:
                self.driver.refresh_page()
                self.driver.sleep(2)
                continue
        assert new_usage == usage + 1, "使用quota值显示不正确"

    @allure.story("显示30天内shipment数量正确")
    def test_shipment_nums_30days_100630(self):
        self.login_page.login_in()
        self.driver.sleep(2)
        shipment_num = int(self.driver.get_text(Home.shipment_num_txt))
        self.home_page.go_to_shipments_page()
        self.shipment_page.add_shipment()
        self.home_page.go_to_home_page()
        new_shipment_num = 0
        for i in range(30):
            self.driver.wait_for_element_visible(Home.quote_usage_txt)
            new_shipment_num = int(self.driver.get_text(Home.shipment_num_txt))
            if new_shipment_num == shipment_num + 1:
                break
            else:
                self.driver.refresh_page()
                self.driver.sleep(2)
                continue
        assert new_shipment_num == shipment_num + 1, "使用quota值显示不正确"


if __name__ == "__main__":
    pytest.main(["-s", os.path.abspath(__file__)])
