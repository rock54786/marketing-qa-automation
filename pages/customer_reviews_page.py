import time

import allure
from seleniumbase import BaseCase

from locators.customer_reviews import CustomerReviews
from locators.home import Home


class CustomerReviewsPage:
    """
    customer reviews page
    """

    def __init__(self, driver):
        self.driver = BaseCase(driver)

    @allure.step("go to customer reviews page")
    def go_to_customer_reviews_page(self):
        self.driver.click(Home.customer_reviews_menu)
        self.driver.wait_for_ready_state_complete()
        assert self.driver.get_text(CustomerReviews.header_title_txt) == 'Customer reviews'
        assert self.driver.get_text(CustomerReviews.card_header_title_txt) == 'Average rating'
