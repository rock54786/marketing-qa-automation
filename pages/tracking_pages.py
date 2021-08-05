import allure
import calendar
import time
from seleniumbase import BaseCase
from locators.home import Home
from locators.tracking_pages import TrackingPagesLocator


class TrackingPages:
    """
    Tracking pages
    """

    def __init__(self, driver):
        self.driver = BaseCase(driver)

    @allure.step("add tracking page")
    def add_tracking_page(self):
        self.driver.click(Home.tracking_pages_menu)
        self.driver.wait_for_ready_state_complete()
        self.driver.click(TrackingPagesLocator.add_tracking_page_btn)
        ts = calendar.timegm(time.gmtime())
        page_name = "auto_page_" + str(ts)
        self.driver.type(TrackingPagesLocator.tracking_page_name_txt, page_name)
        self.driver.wait_for_ready_state_complete()
        self.driver.sleep(2)
        self.driver.click(TrackingPagesLocator.save_btn)
        self.driver.wait_for_ready_state_complete()
        self.driver.sleep(2)
        header_title = self.driver.get_text(TrackingPagesLocator.header_title_txt)
        assert header_title == page_name
        return page_name

    @allure.step("edit tracking page")
    def edit_tracking_page(self):
        self.driver.click(Home.tracking_pages_menu)
        self.driver.wait_for_ready_state_complete()
        self.driver.click(TrackingPagesLocator.row2_action_btn)
        self.driver.click(TrackingPagesLocator.action_edit_btn)
        ts = calendar.timegm(time.gmtime())
        self.driver.type(TrackingPagesLocator.facebook_txt, "test" + str(ts))
        self.driver.sleep(2)
        self.driver.click(TrackingPagesLocator.save_btn)
        self.driver.sleep(5)

    @allure.step("customize theme")
    def customize_theme(self):
        self.driver.click(Home.tracking_pages_menu)
        self.driver.wait_for_ready_state_complete()
        self.driver.click(TrackingPagesLocator.row2_action_btn)
        self.driver.click(TrackingPagesLocator.action_edit_btn)
        self.driver.click(TrackingPagesLocator.customize_btn)
        self.driver.click(TrackingPagesLocator.primary_font_btn)
        self.driver.click(TrackingPagesLocator.dropdown_list_first_option)
        ts = calendar.timegm(time.gmtime())
        self.driver.type(TrackingPagesLocator.header_msg_txt, "header" + str(ts))
        self.driver.type(TrackingPagesLocator.footer_msg_txt, "footer" + str(ts))
        self.driver.type(TrackingPagesLocator.destination_url_txt, "https://www.baidu.com/" + str(ts))
        self.driver.sleep(2)
        self.driver.click(TrackingPagesLocator.save_btn)
        self.driver.sleep(5)
