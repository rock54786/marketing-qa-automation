import allure
import pytest
from seleniumbase import BaseCase
from pages.login_page import LoginPage
from pages.home_page import HomePage
import os

from pages.order_lookup_widget_page import OrderLookupWidgetPage


@allure.feature("Order Lookup Widget page")
class TestOrderLookupWidget:
    @classmethod
    @pytest.fixture(scope="function", autouse=True)
    def setup(cls, base_driver):
        """
        前置步骤
        :return:
        """
        cls.login_page = LoginPage(base_driver)
        cls.home_page = HomePage(base_driver)
        cls.order_lookup_page = OrderLookupWidgetPage(base_driver)
        cls.driver = BaseCase(base_driver)

    @allure.story("成功进入Order lookup widget页面")
    def test_open_order_lookup_widget_page_100868(self):
        self.login_page.login_in()
        self.order_lookup_page.go_to_Order_lookup_widget_page()




if __name__ == "__main__":
    pytest.main(["-s", os.path.abspath(__file__)])
