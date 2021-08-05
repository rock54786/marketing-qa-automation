import json

import allure
import requests
from seleniumbase import BaseCase

from locators.shippment import Shipment
from util.tracking_num_util import TrackingNumUtil


class ShipmentPage:
    """
    主页
    """

    def __init__(self, driver):
        self.driver = BaseCase(driver)

    @allure.step("Add shipment")
    def add_shipment(self, slug=None, status=None):
        self.driver.click(Shipment.add_shipment_btn)
        tracking_nums = TrackingNumUtil.get_tracking_nums(slug, status)
        num = tracking_nums[0]
        self.driver.type(Shipment.tracking_num_txt, num["tracking_number"])
        self.driver.sleep(2)
        # If cannot autocomplete courier, input it
        if self.driver.get_attribute(Shipment.courier_txt, "value") == "":
            self.driver.type(Shipment.courier_txt, num["slug"])
        self.driver.click(Shipment.save_shipment_btn)
        self.driver.wait_for_element_visible(Shipment.view_shipment_btn)
        toast = self.driver.get_text(Shipment.view_shipment_toast)
        assert "%s has been added." % num["tracking_number"] in toast, "Fail to add shipment"
        TrackingNumUtil.disable_in_cache(num["tracking_number"])

    @allure.step("Get shipment list")
    def get_shipment_list(self):
        authorization = "Bearer " + self.driver.execute_script('return localStorage.getItem("__am_t_k");')
        am_org_Id = "db5dbb60bc5548eaaf85ee8c7be88703"
        url = "https://secure-api.aftership.io/data/trackings/v1/search"
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) " \
                          "Chrome/91.0.4472.164 Safari/537.36 ", "authorization": authorization,
            "AM-ORGANIZATION-ID": am_org_Id}
        params = {"include_facets": True, "limit": 20}
        resp = requests.get(url, params=params, headers=headers)
        return resp.json()
        # resp.json()["data"]["trackings"][0]["tracking_number"]

    @allure.step("Filter by Origin")
    def filter_by_origin(self):
        self.driver.click(Shipment.origin_filter)
        self.driver.type(Shipment.filter_search, "United States")
        self.driver.click(Shipment.filter_first_item)
        self.driver.click(Shipment.filter_shipment_txt)
        self.driver.sleep(2)
        row_count = len(self.driver.find_visible_elements('ul.Polaris-ResourceList>li'))
        for r in range(row_count):
            t = self.driver.get_text(
                "ul.Polaris-ResourceList>li:nth-child(%d) div.flex-item:nth-child(%d)>div" % (r + 1, 3))
            assert t.startswith("USA"), "搜索条件不起作用"
        self.driver.click("button[aria-label='Remove Origin in United States of America']")
        self.driver.wait_for_ready_state_complete()

    @allure.step("Filter by Destination")
    def filter_by_destination(self):
        self.driver.click(Shipment.destination_filter)
        self.driver.type(Shipment.filter_search, "United States")
        self.driver.click(Shipment.filter_first_item)
        self.driver.click(Shipment.filter_shipment_txt)
        self.driver.sleep(2)
        row_count = len(self.driver.find_visible_elements('ul.Polaris-ResourceList>li'))
        for r in range(row_count):
            t = self.driver.get_text(
                "ul.Polaris-ResourceList>li:nth-child(%d) div.flex-item:nth-child(%d)>div" % (r + 1, 3))
            assert t.endswith("USA"), "搜索条件不起作用"
        self.driver.click("button[aria-label='Remove Destination in United States of America']")
        self.driver.wait_for_ready_state_complete()

    @allure.step("Filter by courier")
    def filter_by_courier(self):
        self.driver.click(Shipment.courier_filter)
        self.driver.type(Shipment.filter_search, "USPS")
        self.driver.click(Shipment.filter_first_item)
        self.driver.click(Shipment.filter_shipment_txt)
        self.driver.sleep(2)
        row_count = len(self.driver.find_visible_elements('ul.Polaris-ResourceList>li'))
        for r in range(row_count):
            t = self.driver.get_text(
                "ul.Polaris-ResourceList>li:nth-child(%d) div.flex-item:nth-child(%d)>div" % (r + 1, 4))
            assert t.startswith("USPS"), "搜索条件不起作用"
        self.driver.click("button[aria-label='Remove Courier in USPS']")
        self.driver.wait_for_ready_state_complete()

    @allure.step("Filter by status")
    def filter_by_status(self):
        self.driver.click(Shipment.status_filter)
        self.driver.click(Shipment.filter_first_item)
        self.driver.click(Shipment.filter_shipment_txt)
        self.driver.sleep(2)
        row_count = len(self.driver.find_visible_elements('ul.Polaris-ResourceList>li'))
        for r in range(row_count):
            t = self.driver.get_text(
                "ul.Polaris-ResourceList>li:nth-child(%d) div.flex-item:nth-child(%d)>div" % (r + 1, 2))
            assert t == "Delivered", "搜索条件不起作用"
        self.driver.click("button[aria-label='Remove Status in Delivered']")
        self.driver.wait_for_ready_state_complete()

    @allure.step("Delete shipment")
    def delete_shipment(self):
        self.driver.click(Shipment.table_first_row_chkbox)
        tracking_num = self.driver.get_text(Shipment.table_first_row_tracking_num_txt)
        self.driver.click(Shipment.menu_del_btn)
        self.driver.sleep(2)
        self.driver.click(Shipment.pop_delete_shipment_btn)
        self.driver.wait_for_ready_state_complete()
        new_tracking_num = self.driver.get_text(Shipment.table_first_row_tracking_num_txt)
        assert tracking_num != new_tracking_num, "Fail to delete shipment"

    @allure.step("Go to shipment detail")
    def go_to_shipment_detail(self):
        self.driver.click(Shipment.table_first_row_tracking_num_txt)
        self.driver.wait_for_ready_state_complete()
        self.driver.wait_for_element_visible(Shipment.update_status_btn)
