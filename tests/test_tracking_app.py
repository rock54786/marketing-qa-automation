import allure
import pytest
from seleniumbase import BaseCase
from pages.login_page import LoginPage
from pages.home_page import HomePage
import os

from pages.tracking_app_page import TrackingAppPage


@allure.feature("Tracking app page")
class TestTrackingApp:
    @classmethod
    @pytest.fixture(scope="function", autouse=True)
    def setup(cls, base_driver):
        """
        前置步骤
        :return:
        """
        cls.login_page = LoginPage(base_driver)
        cls.home_page = HomePage(base_driver)
        cls.tracking_app_page = TrackingAppPage(base_driver)
        cls.driver = BaseCase(base_driver)

    @allure.story("能通过左侧菜单成功进入页面")
    def test_open_tracking_app_page_100857(self):
        self.login_page.login_in()
        self.tracking_app_page.go_to_tracking_app_page()


if __name__ == "__main__":
    pytest.main(["-s", os.path.abspath(__file__)])
