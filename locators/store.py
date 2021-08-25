from seleniumbase import By
from seleniumbase import BaseCase


class Store:
    """
    Store page Locators
    """

    home_menu = "span.Polaris-Navigation__Text:contains('Home')"
    store_password = "input#password.form-input"
    store_password_confirm = "button"
    popup_iframe = "iframe#automizely_marketing_popup_bars"
    popup_header = "div.mars41.mars45"
    popup_description = "div.mars46.mars54.mars57.mars47.mars63"