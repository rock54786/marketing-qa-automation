import allure
import pytest
from seleniumbase import BaseCase
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.tracking_pages import TrackingPages

import os


@allure.feature("Tracking pages")
class TestTrackingPages:
    @classmethod
    @pytest.fixture(scope="function", autouse=True)
    def setup(cls, base_driver):
        """
        前置步骤
        :return:
        """
        cls.login_page = LoginPage(base_driver)
        cls.home_page = HomePage(base_driver)
        cls.tracking_pages = TrackingPages(base_driver)
        cls.driver = BaseCase(base_driver)

    @allure.story("点击add tracking page输入tracking name可成功创建新的tracking")
    def test_add_tracking_page_100853(self):
        self.login_page.login_in()
        self.tracking_pages.add_tracking_page()

    @allure.story("点击action -> edit 进入编辑tracking page页面，修改内容后成功保存")
    def test_edit_tracking_page_100854(self):
        self.login_page.login_in()
        self.tracking_pages.edit_tracking_page()

    @allure.story("点击action -> edit ->customize 进入编辑主题页面，修改内容后保存成功")
    def test_edit_tracking_page_100855(self):
        self.login_page.login_in()
        self.tracking_pages.customize_theme()

if __name__ == "__main__":
    pytest.main(["-s", os.path.abspath(__file__)])
