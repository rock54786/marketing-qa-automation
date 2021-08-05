import json
import time

import allure
from seleniumbase import BaseCase

from locators.analytics import Analytics
from locators.customer_reviews import CustomerReviews
from locators.home import Home


class AnalyticsPage:
    """
    Analytics
    """

    def __init__(self, driver):
        self.base = driver
        self.driver = BaseCase(driver)

    @allure.step("go to Analytics - shipment page")
    def go_to_analytics_page(self):
        self.driver.click(Home.analytics_menu)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Analytics.header_title_txt) == 'Shipment'

    @allure.step("shipment-filter by ordered at ")
    def shipment_filter(self):
        self.driver.click(Analytics.filter_ddl)
        self.driver.click(Analytics.filter_action_order_at)
        self.driver.wait_for_ready_state_complete()
        card_headers = self.driver.find_visible_elements(Analytics.card_header_title_txt)
        assert card_headers[0].text == 'Total shipments'
        assert card_headers[1].text == 'Shipments by transit time'
        assert card_headers[2].text == 'Shipments by couriers and destination'
        assert card_headers[3].text == 'Exception shipments'

    @allure.step("shipment-view report")
    def shipment_view_report(self):
        self.driver.click(Analytics.view_report)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Analytics.header_title_txt) == 'Shipment report'
        self.driver.sleep(2)
        assert len(self.driver.find_visible_elements(Analytics.shipment_report_detail_table_tr)) > 0

    @allure.step("on-time shipment")
    def on_time_shipment(self):
        self.driver.click(Analytics.on_time_shipment)
        self.driver.wait_for_ready_state_complete()
        self.driver.sleep(2)
        assert 'On-time shipment' in self.driver.get_text(Analytics.header_title_txt)
        self.driver.wait_for_element_visible("span:contains('On-time shipments over time')")
        self.driver.wait_for_element_visible("span:contains('Delivery performance')")
        self.driver.wait_for_element_visible("span:contains('On-time status distribution')")

    @allure.step("On time report报表中，按order date + last 7days查看报表数据成功")
    def on_time_shipment_filter(self):
        self.driver.click(Analytics.on_time_shipment)
        self.driver.wait_for_ready_state_complete()
        self.driver.sleep(2)
        del self.driver.driver.requests
        self.driver.click(Analytics.filter_ddl)
        self.driver.click(Analytics.filter_action_order_at)
        self.driver.click(Analytics.filter_calendar)
        self.driver.select_option_by_index(Analytics.calendar_input, 2)
        self.driver.js_click(Analytics.calendar_apply_btn)
        self.driver.sleep(2)
        for request in self.driver.driver.requests:
            if request.response and 'automizely' in request.url:
                status_code = request.response.status_code
                assert status_code == 200
        assert 'On-time shipment' in self.driver.get_text(Analytics.header_title_txt)
        self.driver.wait_for_element_visible("h2:contains('On-time shipments over time')")
        self.driver.wait_for_element_visible("h2:contains('Delivery performance')")
        self.driver.wait_for_element_visible("h2:contains('On-time status distribution')")

    @allure.step("go to transit time")
    def go_to_transit_time(self):
        self.driver.click(Analytics.transit_time_submenu)
        self.driver.wait_for_ready_state_complete()
        self.driver.sleep(2)
        assert self.driver.get_text(Analytics.header_title_txt) == "Transit time"

        for request in self.driver.driver.requests:
            if request.response and 'transit-time-report' in request.url:
                # data = json.loads(request.response.body.decode('utf-8'))
                status_code = request.response.status_code
                assert status_code == 200

    @allure.step("go to Notification")
    def go_to_notification(self):
        self.driver.click(Analytics.notification_submenu)
        self.driver.wait_for_ready_state_complete()
        self.driver.sleep(2)
        assert self.driver.get_text(Analytics.header_title_txt) == "Notification"
        self.driver.wait_for_element_visible("h2:contains('Total notifications')")
        self.driver.wait_for_element_visible("h2:contains('SMS engagement')")
        self.driver.wait_for_element_visible("h2:contains('Email engagement')")

        for request in self.driver.driver.requests:
            if request.response and 'notification' in request.url:
                status_code = request.response.status_code
                assert status_code == 200

    @allure.step("Notification报表中，选择按last 7 days成功查询报表")
    def notification_last_7days(self):
        self.driver.click(Analytics.notification_submenu)
        self.driver.wait_for_ready_state_complete()
        self.driver.sleep(2)
        del self.driver.driver.requests
        self.driver.click(Analytics.notification_calendar)
        self.driver.select_option_by_index(Analytics.calendar_input, 2)
        self.driver.js_click(Analytics.calendar_apply_btn)
        self.driver.sleep(2)
        for request in self.driver.driver.requests:
            if request.response and 'notification' in request.url:
                status_code = request.response.status_code
                assert status_code == 200
        self.driver.wait_for_element_visible("h2:contains('Total notifications')")
        self.driver.wait_for_element_visible("h2:contains('SMS engagement')")
        self.driver.wait_for_element_visible("h2:contains('Email engagement')")

    @allure.step("点击左侧菜单Tracking page成功进入页面")
    def go_to_tracking_page(self):
        del self.driver.driver.requests
        self.driver.click(Analytics.tracking_page_submenu)
        self.driver.wait_for_ready_state_complete()
        self.driver.sleep(2)
        assert self.driver.get_text(Analytics.header_title_txt) == "Tracking page"
        for request in self.driver.driver.requests:
            if request.response and 'automizely' in request.url:
                # data = json.loads(request.response.body.decode('utf-8'))
                status_code = request.response.status_code
                assert status_code == 200

    @allure.step("Tracking page报表中，选择last 7 days成功查看报表")
    def tracking_page_filter(self):
        self.driver.click(Analytics.tracking_page_submenu)
        self.driver.wait_for_ready_state_complete()
        self.driver.sleep(2)
        del self.driver.driver.requests
        self.driver.click(Analytics.notification_calendar)
        self.driver.select_option_by_value(Analytics.calendar_input, "last 7 days")
        self.driver.js_click(Analytics.calendar_apply_btn)
        self.driver.sleep(2)
        for request in self.driver.driver.requests:
            if request.response and 'automizely' in request.url:
                status_code = request.response.status_code
                assert status_code == 200
        assert 'Tracking page' in self.driver.get_text(Analytics.header_title_txt)
        self.driver.wait_for_element_visible("h2:contains('Page views')")
        self.driver.wait_for_element_visible("h2:contains('Marketing assets performance')")
        self.driver.wait_for_element_visible("h2:contains('Marketing clicks')")
        self.driver.wait_for_element_visible("h2:contains('Product recommendations performance')")
