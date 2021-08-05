import allure
import pytest
from seleniumbase import BaseCase

from pages.apps_page import AppsPage
from pages.connections_page import ConnectionsPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
import os

from pages.order_lookup_widget_page import OrderLookupWidgetPage


@allure.feature("Apps")
class TestApps:
    @classmethod
    @pytest.fixture(scope="function", autouse=True)
    def setup(cls, base_driver):
        """
        前置步骤
        :return:
        """
        cls.login_page = LoginPage(base_driver)
        cls.home_page = HomePage(base_driver)
        cls.apps_page = AppsPage(base_driver)
        cls.driver = BaseCase(base_driver)

    @allure.story("菜单点击App跳转App页面选择页面")
    def test_apps_page_100872(self):
        self.login_page.login_in()
        self.apps_page.go_to_apps_page()





if __name__ == "__main__":
    pytest.main(["-s", os.path.abspath(__file__)])
