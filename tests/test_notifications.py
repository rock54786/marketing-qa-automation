import allure
import pytest
from seleniumbase import BaseCase

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.notifications_page import NotificationsPage
from pages.shipment_page import ShipmentPage
from locators.home import Home
import os


@allure.feature("Notifications page")
class TestNotifications:
    @classmethod
    @pytest.fixture(scope="function", autouse=True)
    def setup(cls, base_driver):
        """
        前置步骤
        :return:
        """
        cls.login_page = LoginPage(base_driver)
        cls.home_page = HomePage(base_driver)
        cls.shipment_page = ShipmentPage(base_driver)
        cls.notifications_page = NotificationsPage(base_driver)
        cls.driver = BaseCase(base_driver)

    @allure.story("点击Emails & SMS进入页面，Email and SMS默认显示to customers当前配置")
    def test_emails_sms_100848(self):
        self.login_page.login_in()
        self.home_page.go_to_notifications_page()
        self.notifications_page.go_to_email_sms_page()

    @allure.story("选择to subscribers 并点击 go to tracking page setting 成功跳转页面")
    def test_to_subscribers_100849(self):
        self.login_page.login_in()
        self.home_page.go_to_notifications_page()
        self.notifications_page.go_to_email_sms_page()
        self.notifications_page.go_to_tracking_page_setting()

    @allure.story("选择to yourself并点击 go to setting 成功跳转页面")
    def test_to_yours_setting_100850(self):
        self.login_page.login_in()
        self.home_page.go_to_notifications_page()
        self.notifications_page.go_to_email_sms_page()
        self.notifications_page.go_to_yours_setting()

    @allure.story("左侧菜单点击webhooks可以成功进入Webhooks")
    def test_webhooks_100851(self):
        self.login_page.login_in()
        self.home_page.go_to_notifications_page()
        self.notifications_page.go_to_webhooks()

    @allure.story("左侧菜单点击Notification history成功进入Notification history页面")
    def test_notification_history_100852(self):
        self.login_page.login_in()
        self.home_page.go_to_notifications_page()
        self.notifications_page.go_to_notification_history()
if __name__ == "__main__":
    pytest.main(["-s", os.path.abspath(__file__)])
