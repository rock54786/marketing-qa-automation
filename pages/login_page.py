import allure

from locators.home_page_locators import HomePageLocators
from locators.login_page_locators import LoginPageLocators
from seleniumbase import encryption, BaseCase
from config import ENV


class LoginPage:
    """
    登录页面场景
    """

    def __init__(self, driver):
        self.driver = BaseCase(driver)

    @allure.step("login")
    def login_in(self):
        """
        密码登录
        :return:
        """
        self.driver.type(LoginPageLocators.email, ENV.USER_NAME)
        self.driver.type(LoginPageLocators.password, encryption.decrypt(ENV.PASSWORD))
        self.driver.click(LoginPageLocators.login_btn)
        assert self.driver.wait_for_element_visible(HomePageLocators.welcome_title_txt, 20), "login failed"
