import allure
from seleniumbase import BaseCase
from locators.home import Home
from locators.notifications import Notifications
from locators.shippment import Shipment


class NotificationsPage:
    """
    通知
    """

    def __init__(self, driver):
        self.driver = BaseCase(driver)

    @allure.step("go to email&sms page")
    def go_to_email_sms_page(self):
        self.driver.click(Notifications.emails_sms_submenu)
        self.driver.wait_for_ready_state_complete()
        selected = self.driver.get_attribute(Notifications.to_customers_tab, "aria-selected")
        assert selected == "true", "To customers 没有默认选中"

    @allure.step("go to tracking page settings")
    def go_to_tracking_page_setting(self):
        self.driver.click(Notifications.emails_sms_submenu)
        self.driver.wait_for_ready_state_complete()
        self.driver.click(Notifications.to_subscribers_tab)
        self.driver.click(Notifications.go_to_tracking_page_settings)
        assert self.driver.get_text(Notifications.page_headers_title) == "Tracking pages"

    @allure.step("go to yours settings")
    def go_to_yours_setting(self):
        self.driver.click(Notifications.emails_sms_submenu)
        self.driver.wait_for_ready_state_complete()
        self.driver.click(Notifications.to_yours_tab)
        self.driver.click(Notifications.go_to_yours_settings)
        assert self.driver.get_text(Notifications.page_headers_title) == "Notifications"

    @allure.step("go to webhooks")
    def go_to_webhooks(self):
        self.driver.click(Notifications.webhooks_submenu)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Notifications.page_headers_title) == "Webhooks"

    @allure.step("go to Notification history")
    def go_to_notification_history(self):
        self.driver.click(Notifications.notification_history_submenu)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Notifications.page_headers_title) == "Notification history"
