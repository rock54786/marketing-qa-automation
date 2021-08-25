import allure
from seleniumbase import BaseCase
from locators.store_page_locators import StorePageLocators


class StorePage:
    """
    主页
    """

    def __init__(self, driver):
        self.base = driver
        self.driver = BaseCase(driver)

    @allure.step("go to popup tab")
    def login_in(self):
        self.driver.type(StorePageLocators.password, "1")
        self.driver.click(StorePageLocators.password_confirm)

    @allure.step("check popup header")
    def check_popup_header(self):
        self.driver.sleep(5)
        self.driver.switch_to_frame(StorePageLocators.popup_iframe)
        a = self.driver.get_text(StorePageLocators.popup_header)
        print(a)
        self.driver.assert_text("Automizely Header Test: Get $10.00 OFF your first order!",
                                StorePageLocators.popup_header)

    @allure.step("check popup description")
    def check_popup_description(self):
        self.driver.assert_text \
            ("Automizely Description Test: Join our email list to receive updates and exclusive offers.",
             StorePageLocators.popup_description)
