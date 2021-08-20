import allure

from locators.home import Home
from locators.login import Login
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
        self.driver.type(Login.email, ENV.USER_NAME)
        self.driver.type(Login.password, encryption.decrypt(ENV.PASSWORD))
        self.driver.click(Login.login_btn)
        self.driver.wait_for_element_visible(Home.welcome_title_txt, 20)
        assert self.driver.get_title() == "Automizely Marketing", "Fail to login"
