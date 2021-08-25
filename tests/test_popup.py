import allure
import pytest
from seleniumbase import BaseCase
from pages.store_page import StorePage
from pages.login_page import LoginPage
from pages.popup_page import PopupPage
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
        cls.popup_page = PopupPage(base_driver)
        cls.store_page = StorePage(base_driver)
        cls.driver = BaseCase(base_driver)

    @allure.story("检查已有popup是否能成功保存")
    def test_popup_save(self):
        self.login_page.login_in()
        self.driver.sleep(2)
        self.home_page.go_to_popup_page()
        self.home_page.go_to_popup_edit()
        self.home_page.go_to_popup_test()
        self.home_page.reset_popup_test()

    @allure.story("检查C端页面popup是否与配置一致")
    def test_toc_popup(self):
        self.login_page.login_in()
        self.driver.sleep(2)
        self.home_page.go_to_store()
        self.store_page.login_in()
        self.store_page.check_popup_header()
        self.store_page.check_popup_description()


if __name__ == "__main__":
    pytest.main(["-s", os.path.abspath(__file__)])
