import allure
import pytest
from seleniumbase import BaseCase

from pages.delivery_date_settings_page import DeliveryDateSettingsPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
import os

from pages.order_lookup_widget_page import OrderLookupWidgetPage


@allure.feature("Delivery date settings page")
class TestDeliveryDateSettings:
    @classmethod
    @pytest.fixture(scope="function", autouse=True)
    def setup(cls, base_driver):
        """
        前置步骤
        :return:
        """
        cls.login_page = LoginPage(base_driver)
        cls.home_page = HomePage(base_driver)
        cls.delivery_date_page = DeliveryDateSettingsPage(base_driver)
        cls.driver = BaseCase(base_driver)

    @allure.story("点击菜单Deliver date setings成功进入PDD设置页面 ")
    def test_delivery_date_settings_page_100869(self):
        self.login_page.login_in()
        self.delivery_date_page.go_to_delivery_date_settings_page()




if __name__ == "__main__":
    pytest.main(["-s", os.path.abspath(__file__)])
