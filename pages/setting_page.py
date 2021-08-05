import json
import time

import allure
from seleniumbase import BaseCase
from locators.home import Home
from locators.setting import Setting


class SettingPage:
    """
    Setting
    """

    def __init__(self, driver):
        self.base = driver
        self.driver = BaseCase(driver)

    @allure.step("Setting-couriers")
    def go_to_couriers_page(self):
        self.driver.click(Home.setting_menu)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Setting.header_title_txt) == 'Settings'
        self.driver.sleep(2)
        self.driver.js_click(Setting.couriers_link)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Setting.header_title_txt) == 'Couriers'

    @allure.step("Setting-couriers-inactive")
    def go_to_couriers_inactive_page(self):
        self.driver.click(Home.setting_menu)
        self.driver.wait_for_ready_state_complete()
        self.driver.sleep(2)
        self.driver.js_click(Setting.couriers_link)
        self.driver.wait_for_ready_state_complete()
        self.driver.click(Setting.couriers_disable_btn)
        for btn in self.driver.find_visible_elements(Setting.couriers_enable_btns):
            assert btn.text == 'Enable'

    @allure.step("go to Setting-api keys pages")
    def go_to_apikey_page(self):
        self.driver.click(Home.setting_menu)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Setting.header_title_txt) == 'Settings'
        self.driver.sleep(2)
        self.driver.js_click(Setting.apikeys_link)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Setting.header_title_txt) == 'API keys'
        self.driver.sleep(2)
        assert len(self.driver.find_visible_elements(Setting.apikey_rows)) > 0

    @allure.step("Setting- create and delete apikey")
    def setting_create_del_apikey_page(self):
        self.driver.click(Home.setting_menu)
        self.driver.wait_for_ready_state_complete()
        self.driver.sleep(2)
        self.driver.js_click(Setting.apikeys_link)
        self.driver.wait_for_ready_state_complete()
        self.driver.sleep(2)
        before = len(self.driver.find_visible_elements(Setting.apikey_rows))
        self.driver.click(Setting.generate_apikeys_btn)
        self.driver.type(Setting.description_txt, "test_key")
        self.driver.sleep(1)
        self.driver.click(Setting.submit_generate_apikeys_btn)
        self.driver.sleep(2)
        self.driver.click(Setting.apikey_second_row_del_btn)
        self.driver.click(Setting.apikeys_del_btn)
        self.driver.sleep(2)
        after = len(self.driver.find_visible_elements(Setting.apikey_rows))
        assert before == after

    @allure.step("go to billing page")
    def go_to_billing_page(self):
        self.driver.click(Home.setting_menu)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Setting.header_title_txt) == 'Settings'
        self.driver.sleep(2)
        self.driver.js_click(Setting.billing_link)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Setting.header_title_txt) == 'Billing'
        self.driver.sleep(2)
        assert self.driver.get_text(Setting.billing_plan) == 'Pro 5K - Monthly'

    @allure.step(" Billing，点击plan右上角「...」upgrade弹出升级plan model")
    def billing_upgrade_plan(self):
        self.driver.click(Home.setting_menu)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Setting.header_title_txt) == 'Settings'
        self.driver.sleep(2)
        self.driver.js_click(Setting.billing_link)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Setting.header_title_txt) == 'Billing'
        self.driver.click(Setting.ellipsis_btn)
        self.driver.click(Setting.upgrade_btn)
        self.driver.wait_for_element_visible(Setting.update_plan_btn)

    @allure.step("go to Promised delivery date")
    def go_to_promised_delivery_date_page(self):
        self.driver.click(Home.setting_menu)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Setting.header_title_txt) == 'Settings'
        self.driver.sleep(2)
        self.driver.js_click(Setting.promised_delivery_date_link)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Setting.header_title_txt) == 'Promised delivery date'

    @allure.step("enable and disable Promised delivery date")
    def enable_disable_promised_delivery_date(self):
        self.driver.click(Home.setting_menu)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Setting.header_title_txt) == 'Settings'
        self.driver.sleep(2)
        self.driver.js_click(Setting.promised_delivery_date_link)
        self.driver.wait_for_ready_state_complete()
        self.driver.click(Setting.pdd_switch)
        self.driver.sleep(1)
        self.driver.click(Setting.pdd_enable_btn)
        self.driver.sleep(1)
        self.driver.click(Setting.pdd_switch)
        self.driver.click(Setting.pdd_disable_btn)

    @allure.step("Edit Order cutoff & processing time")
    def order_cutoff_processing_time(self):
        self.driver.click(Home.setting_menu)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Setting.header_title_txt) == 'Settings'
        self.driver.sleep(2)
        self.driver.js_click(Setting.promised_delivery_date_link)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Setting.header_title_txt) == 'Promised delivery date'
        before = self.driver.get_text(Setting.pdd_additional_business_day)
        self.driver.click(Setting.pdd_edit_btn)
        self.driver.click(Setting.pdd_additional_processing_time_chk)
        self.driver.click(Setting.pdd_submit_btn)
        self.driver.sleep(2)
        after = self.driver.get_text(Setting.pdd_additional_business_day)
        assert before != after

    @allure.step("Add new transit time and delete")
    def add_delete_new_transit(self):
        self.driver.click(Home.setting_menu)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Setting.header_title_txt) == 'Settings'
        self.driver.sleep(2)
        self.driver.js_click(Setting.promised_delivery_date_link)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Setting.header_title_txt) == 'Promised delivery date'
        # add transit
        self.driver.click(Setting.pdd_add_a_new_transit_time)
        self.driver.click(Setting.pdd_add_btn)
        self.driver.sleep(1)
        self.driver.click(Setting.pdd_asia_chk)
        self.driver.click(Setting.pdd_ship_zone_save_btn)
        self.driver.sleep(1)
        self.driver.click(Setting.pdd_save_btn)
        # delete transit
        self.driver.sleep(1)
        self.driver.click(Setting.pdd_transit_ellipsis_btn)
        self.driver.sleep(1)
        self.driver.click(Setting.pdd_del_btn)

    @allure.step("go to notification page")
    def go_to_notification_page(self):
        self.driver.click(Home.setting_menu)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Setting.header_title_txt) == 'Settings'
        self.driver.sleep(2)
        self.driver.js_click(Setting.notifications_link)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Setting.header_title_txt) == 'Notifications'
        self.driver.wait_for_text("Notifications to yourself")

    @allure.step("enable and disable email")
    def notification_enable_disable_email(self):
        self.driver.click(Home.setting_menu)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Setting.header_title_txt) == 'Settings'
        self.driver.sleep(2)
        self.driver.js_click(Setting.notifications_link)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Setting.header_title_txt) == 'Notifications'
        self.driver.click(Setting.notifications_enable_email_btn)
        self.driver.sleep(1)
        txt = self.driver.get_text(Setting.notifications_disable_email_btn)
        assert txt == 'Disable email'
        self.driver.click(Setting.notifications_disable_email_btn)
        self.driver.sleep(1)
        txt = self.driver.get_text(Setting.notifications_enable_email_btn)
        assert txt == 'Enable email'

    @allure.step("info received - edit email template")
    def edit_email_template(self):
        self.driver.click(Home.setting_menu)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Setting.header_title_txt) == 'Settings'
        self.driver.sleep(2)
        self.driver.js_click(Setting.notifications_link)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Setting.header_title_txt) == 'Notifications'
        self.driver.click(Setting.notifications_edit_email_link)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(Setting.notifications_editor_template_name) == 'Info received'

