import pytest

from seleniumbase import BaseCase
from config import ENV


@pytest.fixture(scope="function", autouse=True)
def driver(base_driver):
    """
    获取驱动
    :return:
    """
    driver = BaseCase(base_driver)
    driver.maximize_window()
    driver.open(ENV.URL)
    yield base_driver
    # driver.quit_all_drivers()
