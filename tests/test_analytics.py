import allure
import pytest
from seleniumbase import BaseCase

from pages.analytics_page import AnalyticsPage
from pages.customer_reviews_page import CustomerReviewsPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from locators.home import Home
import os


@allure.feature("Analytics page")
class TestAnalytics:
    @classmethod
    @pytest.fixture(scope="function", autouse=True)
    def setup(cls, base_driver):
        """
        前置步骤
        :return:
        """
        cls.login_page = LoginPage(base_driver)
        cls.home_page = HomePage(base_driver)
        cls.analytics_page = AnalyticsPage(base_driver)
        cls.driver = BaseCase(base_driver)

    @allure.story("点击左侧菜单Shipment成功进入页面")
    def test_open_analytics_shipment_page_100858(self):
        self.login_page.login_in()
        self.analytics_page.go_to_analytics_page()

    @allure.story("Shipment报表中，切换筛选条件按order date 成功显示数据")
    def test_analytics_shipment_filter_100859(self):
        self.login_page.login_in()
        self.analytics_page.go_to_analytics_page()
        self.analytics_page.shipment_filter()

    @allure.story("Shipment报表中，点击view report进入shipment report页面并显示正常")
    def test_analytics_shipment_view_report_100860(self):
        self.login_page.login_in()
        self.analytics_page.go_to_analytics_page()
        self.analytics_page.shipment_view_report()

    @allure.story("点击左侧菜单On time report成功进入页面")
    def test_analytics_on_time_shipment_100861(self):
        self.login_page.login_in()
        self.analytics_page.go_to_analytics_page()
        self.analytics_page.on_time_shipment()

    @allure.story("On time report报表中，按order date + last 7days查看报表数据成功")
    def test_analytics_on_time_shipment_filter_100862(self):
        self.login_page.login_in()
        self.analytics_page.go_to_analytics_page()
        self.analytics_page.on_time_shipment_filter()

    @allure.story("点击左侧菜单Transit time成功进入页面")
    def test_analytics_transit_time_100863(self):
        self.login_page.login_in()
        self.analytics_page.go_to_analytics_page()
        self.analytics_page.go_to_transit_time()

    @allure.story("点击左侧菜单Notification成功进入页面")
    def test_analytics_notification_100864(self):
        self.login_page.login_in()
        self.analytics_page.go_to_analytics_page()
        self.analytics_page.go_to_notification()

    @allure.story("Notification报表中，选择按last 7 days成功查询报表")
    def test_analytics_notification_last_7days_100865(self):
        self.login_page.login_in()
        self.analytics_page.go_to_analytics_page()
        self.analytics_page.notification_last_7days()

    @allure.story("点击左侧菜单Tracking page成功进入页面")
    def test_analytics_tracking_page_100866(self):
        self.login_page.login_in()
        self.analytics_page.go_to_analytics_page()
        self.analytics_page.go_to_tracking_page()

    @allure.story("Tracking page报表中，选择last 7 days成功查看报表")
    def test_analytics_tracking_page_filter_100867(self):
        self.login_page.login_in()
        self.analytics_page.go_to_analytics_page()
        self.analytics_page.tracking_page_filter()


if __name__ == "__main__":
    pytest.main(["-s", os.path.abspath(__file__)])
