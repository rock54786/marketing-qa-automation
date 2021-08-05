import allure
import pytest
from seleniumbase import BaseCase

from pages.login_page import LoginPage
from pages.home_page import HomePage
import os

from pages.refer_to_earn_page import ReferToEarnPage


@allure.feature("ReferToEarn")
class TestReferToEarn:
    @classmethod
    @pytest.fixture(scope="function", autouse=True)
    def setup(cls, base_driver):
        """
        前置步骤
        :return:
        """
        cls.login_page = LoginPage(base_driver)
        cls.home_page = HomePage(base_driver)
        cls.refer_to_earn = ReferToEarnPage(base_driver)
        cls.driver = BaseCase(base_driver)

    @allure.story("通过点击菜单Refer to earn 15% 成功进入页面")
    def test_refer_to_earn_100873(self):
        self.login_page.login_in()
        self.refer_to_earn.go_to_refer_to_earn_page()




if __name__ == "__main__":
    pytest.main(["-s", os.path.abspath(__file__)])
