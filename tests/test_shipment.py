import allure
import pytest
from seleniumbase import BaseCase

from locators.shippment import Shipment
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.shipment_page import ShipmentPage
from locators.home import Home
import os


@allure.feature("Shipment page")
class TestShipment:
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

    @allure.story("输入正确的tracking number和courier创建tracking")
    def test_add_shipment_100843(self):
        self.login_page.login_in()
        self.home_page.go_to_shipments_page()
        self.shipment_page.add_shipment()

    @allure.story("通过输入具体的tracking number 查询shipment并能查到结果")
    def test_search_shipment_by_num_100844(self):
        self.login_page.login_in()
        self.home_page.go_to_shipments_page()
        tracking_num = self.shipment_page.get_shipment_list()["data"]["trackings"][0]["tracking_number"]
        self.driver.type(Shipment.filter_shipment_txt, tracking_num)
        self.driver.sleep(2)
        assert self.driver.get_text(Shipment.shipment_count_lbl) == 'Showing 1 of 1 results', "查询失败"

    @allure.story("通过选择orgin/destination/courier/status能筛选满足条件的shipment")
    def test_filter_100845(self):
        self.login_page.login_in()
        self.home_page.go_to_shipments_page()
        self.shipment_page.filter_by_origin()
        self.shipment_page.filter_by_destination()
        self.shipment_page.filter_by_courier()
        self.shipment_page.filter_by_status()

    @allure.story("选择一条shipment并成功delete")
    def test_delete_shipment_100846(self):
        self.login_page.login_in()
        self.home_page.go_to_shipments_page()
        self.shipment_page.delete_shipment()

    @allure.story("点击shipment list中 shipment可成功进入详情页面")
    def test_go_to_shipment_detail_100847(self):
        self.login_page.login_in()
        self.home_page.go_to_shipments_page()
        self.shipment_page.go_to_shipment_detail()


if __name__ == "__main__":
    pytest.main(["-s", os.path.abspath(__file__)])
