from seleniumbase import By
from seleniumbase import BaseCase


class Home:
    """
    Home page Locators
    """

    home_menu = "span.Polaris-Navigation__Text:contains('Home')"
    popup_menu = "span.Polaris-Navigation__Text:contains('Popup campaigns')"
    tools_menu = "span.Polaris-Navigation__Text:contains('Conversion tools')"
    emails_menu = "span.Polaris-Navigation__Text:contains('Emails')"
    push_menu = "span.Polaris-Navigation__Text:contains('Web push')"
    coupon_menu = "span.Polaris-Navigation__Text:contains('Coupon')"
    contact_menu = "span.Polaris-Navigation__Text:contains('Contacts')"
    view_store = "span.Polaris-Navigation__Text:contains('View your store')"
    store_password = "input#password.form-input"
    add_popup_btn = "span:contains('Add new popup')"
    edit_btn = "span.preview-clickable-true"
    edit_btn_test = ".Polaris-Button__Text"
    popup_title = "h1.Polaris-DisplayText"
    radio_button = ".Polaris-RadioButton__Backdrop"
    popup_tabs_tab = ".Polaris-Tabs__Tab"
    popup_tabs_title = ".Polaris-Tabs__Title"
    text_title = "h2.Polaris-Heading:contains('First step')"
    popup_text_input = ".Polaris-TextField__Input"
    popup_save = ".Polaris-Button__Text:contains('Save and publish')"
    popup_publish = "span.Polaris-Button__Text:contain('Publish')"
    shipment_menu = "span.Polaris-Navigation__Text:contains('Shipments')"
    notifications_menu = "span.Polaris-Navigation__Text:contains('Notifications')"
    tracking_pages_menu = "span.Polaris-Navigation__Text:contains('Tracking pages')"
    customer_reviews_menu = "span.Polaris-Navigation__Text:contains('Customer reviews')"
    tracking_app_menu = "span.Polaris-Navigation__Text:contains('Tracking app')"
    analytics_menu = "span.Polaris-Navigation__Text:contains('Analytics')"
    order_lookup_widget_menu = "span.Polaris-Navigation__Text:contains('Order lookup widget')"
    delivery_date_settings_menu = "span.Polaris-Navigation__Text:contains('Delivery date settings')"
    connections_menu = "span.Polaris-Navigation__Text:contains('Connections')"
    apps_menu = "span.Polaris-Navigation__Text:contains('Apps')"
    refer_to_earn_menu = "span.Polaris-Navigation__Text:contains('Refer to earn 15%')"
    setting_menu = "span.Polaris-Navigation__Text:contains('Settings')"
    welcome_title_txt = ".Polaris-Header-Title"
    plan_txt = "div.Polaris-Layout__Section--secondary  div.Polaris-Card__Header > h2"
    quote_usage_txt = "p.Polaris-DisplayText.Polaris-DisplayText--sizeMedium"
    shipment_num_txt = "section.c-top-mertics p.Polaris-DisplayText"





