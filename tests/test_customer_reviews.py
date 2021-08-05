import allure
import pytest
from seleniumbase import BaseCase

from pages.customer_reviews_page import CustomerReviewsPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from locators.home import Home
import os


@allure.feature("Customer reviews page")
class TestCustomerReviews:
    @classmethod
    @pytest.fixture(scope="function", autouse=True)
    def setup(cls, base_driver):
        """
        前置步骤
        :return:
        """
        cls.login_page = LoginPage(base_driver)
        cls.home_page = HomePage(base_driver)
        cls.customer_reviews_page = CustomerReviewsPage(base_driver)
        cls.driver = BaseCase(base_driver)

    @allure.story("通过左侧菜单成功打开页面")
    def test_open_customer_reviews_page_100856(self):
        self.login_page.login_in()
        self.customer_reviews_page.go_to_customer_reviews_page()



if __name__ == "__main__":
    pytest.main(["-s", os.path.abspath(__file__)])
