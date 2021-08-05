import allure
import pytest
from seleniumbase import BaseCase

from pages.connections_page import ConnectionsPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
import os

from pages.order_lookup_widget_page import OrderLookupWidgetPage


@allure.feature("Connections")
class TestConnections:
    @classmethod
    @pytest.fixture(scope="function", autouse=True)
    def setup(cls, base_driver):
        """
        前置步骤
        :return:
        """
        cls.login_page = LoginPage(base_driver)
        cls.home_page = HomePage(base_driver)
        cls.connections_page = ConnectionsPage(base_driver)
        cls.driver = BaseCase(base_driver)

    @allure.story("成功进入connection页面并展示用户当前所有的connection")
    def test_connections_page_100870(self):
        self.login_page.login_in()
        self.connections_page.go_to_connections_page()

    @allure.story(" 点击Add connection 跳转选择App建立链接页面 ")
    def test_add_connection_100871(self):
        self.login_page.login_in()
        self.connections_page.add_connection()




if __name__ == "__main__":
    pytest.main(["-s", os.path.abspath(__file__)])
