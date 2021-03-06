import allure
from seleniumbase import BaseCase
from locators.home_page_locators import HomePageLocators
from locators.popup_page_locators import PopupPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from locators.store_page_locators import StorePageLocators


class PopupPage:
    """
    主页
    """

    def __init__(self, driver):
        self.base = driver
        self.driver = BaseCase(driver)

    @allure.step("go to popup tab")
    def go_to_popup_page(self):
        self.driver.click(HomePageLocators.popup_menu)
        self.driver.click(HomePageLocators.popup_menu)
        self.driver.wait_for_element_visible(PopupPageLocators.add_popup_btn)

    @allure.step("go to default popup")
    def go_to_popup_page(self):
        self.driver.click(HomePageLocators.popup_menu)
        self.driver.sleep(1)
        self.driver.wait_for_element_visible(PopupPageLocators.add_popup_btn)

    @allure.step("go to popup edit")
    def go_to_popup_edit(self):
        ActionChains(self.base).move_to_element(
            self.base.find_elements_by_css_selector(PopupPageLocators.edit_btn)[4]).perform()
        self.base.find_elements_by_css_selector(PopupPageLocators.edit_btn)[4].click()
        self.driver.wait_for_element_visible(PopupPageLocators.title)

    @allure.step("in popup page click to Text tab")
    def go_to_popup_test(self):
        self.base.find_elements_by_css_selector(PopupPageLocators.tabs_tab)[4].click()
        self.driver.wait_for_element_visible(PopupPageLocators.text_title)

    @allure.step("reset header")
    def reset_popup_test(self):
        self.base.find_elements_by_css_selector(PopupPageLocators.text_input)[0].send_keys(Keys.COMMAND, 'a')
        self.base.find_elements_by_css_selector(PopupPageLocators.text_input)[0]. \
            send_keys("Automizely Header Test: PopupPageLocators $10.00 OFF your first order!")
        self.base.find_elements_by_css_selector(PopupPageLocators.text_input)[1].send_keys(Keys.COMMAND, 'a')
        self.base.find_elements_by_css_selector(PopupPageLocators.text_input)[1]. \
            send_keys("Automizely Description Test: Join our email list to receive updates and exclusive offers.")
        self.driver.click(PopupPageLocators.save)
        self.driver.sleep(1)
        self.base.find_elements_by_css_selector(PopupPageLocators.edit_btn)[4].click()

    @allure.step("go to store")
    def go_to_store(self):
        self.driver.click(HomePageLocators.view_store)
        self.driver.switch_to_newest_window()

    @allure.step("store popup check")
    def store_popup_check(self):
        self.driver.type(self, StorePageLocators.password, "1")

    @allure.step("go to home page")
    def go_to_home_page(self):
        self.driver.click(HomePageLocators.home_menu)
        self.driver.click(HomePageLocators.home_menu)  # 总会有一次点击不生效的情况
        self.driver.wait_for_element_visible(HomePageLocators.welcome_title_txt)
