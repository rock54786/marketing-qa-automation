import allure
import pytest
from seleniumbase import BaseCase
from pages.login_page import LoginPage
from pages.home_page import HomePage
import os

from pages.setting_page import SettingPage


@allure.feature("Setting")
class TestSetting:
    @classmethod
    @pytest.fixture(scope="function", autouse=True)
    def setup(cls, base_driver):
        """
        前置步骤
        :return:
        """
        cls.login_page = LoginPage(base_driver)
        cls.home_page = HomePage(base_driver)
        cls.setting_page = SettingPage(base_driver)
        cls.driver = BaseCase(base_driver)

    @allure.story("couriers，点击进入couriers设置页面")
    def test_setting_couriers_100874(self):
        self.login_page.login_in()
        self.setting_page.go_to_couriers_page()

    @allure.story("courier，设置页面中点击Inactive展示未活跃的courier")
    def test_setting_couriers_inactive_100875(self):
        self.login_page.login_in()
        self.setting_page.go_to_couriers_inactive_page()

    @allure.story("API keys，成功进入页面展示用户当前所有的api keys")
    def test_setting_api_keys_100876(self):
        self.login_page.login_in()
        self.setting_page.go_to_apikey_page()

    @allure.story("API keys，点击Gennerate API key创建一个新的key,然后删掉")
    def test_setting_api_keys_100877_100878(self):
        self.login_page.login_in()
        self.setting_page.setting_create_del_apikey_page()

    @allure.story("Billing，成功进入页面展示用户当前订阅的plan")
    def test_billing_view_plan_100879(self):
        self.login_page.login_in()
        self.setting_page.go_to_billing_page()

    @allure.story("Billing，点击plan右上角「...」upgrade弹出升级plan model")
    def test_billing_upgrade_plan_100880(self):
        self.login_page.login_in()
        self.setting_page.billing_upgrade_plan()

    @allure.story("Promised delivery date，成功进入设置PDD页面")
    def test_go_to_promised_delivery_date_100881(self):
        self.login_page.login_in()
        self.setting_page.go_to_promised_delivery_date_page()

    @allure.story(" Promised delivery date，点击enable 开启PDD,然后关闭PDD")
    def test_enable_disable_promised_delivery_date_100882_100883(self):
        self.login_page.login_in()
        self.setting_page.enable_disable_promised_delivery_date()

    @allure.story("Promised delivery date，在Order cutoff & processing time栏点击edit编辑保存成功")
    def test_order_cutoff_processing_time_100884(self):
        self.login_page.login_in()
        self.setting_page.order_cutoff_processing_time()

    @allure.story("Promised delivery date，点击「Add new transit time」新增一个transit time,并删除")
    def test_add_delete_new_transit_100885_100886(self):
        self.login_page.login_in()
        self.setting_page.add_delete_new_transit()

    @allure.story("Notifications，成功进入页面展示Notifications to yourself 设置")
    def test_go_to_notifications_100887(self):
        self.login_page.login_in()
        self.setting_page.go_to_notification_page()

    @allure.story("Notifications，INFO RECEIVED状态栏点击enable/disable可以开启关闭email")
    def test_go_to_notifications_100888(self):
        self.login_page.login_in()
        self.setting_page.notification_enable_disable_email()

    @allure.story("Notifications，INFO RECEIVED状态栏点击Email edit 进入模版编辑页面")
    def test_edit_email_template_100889(self):
        self.login_page.login_in()
        self.setting_page.edit_email_template()

if __name__ == "__main__":
    pytest.main(["-s", os.path.abspath(__file__)])
