class Notifications:
    """
    Notifications page Locators
    """
    # email & sms
    page_headers_title = "h1.Polaris-Header-Title"
    emails_sms_submenu = "span.Polaris-Navigation__Text:contains('Emails & SMS')"
    to_customers_tab = "#customers"
    to_subscribers_tab = "#subscribers"
    to_yours_tab = "#yourself"
    go_to_tracking_page_settings = "span.Polaris-Button__Text:contains('Go to tracking page settings')"
    go_to_yours_settings = "span.Polaris-Button__Text:contains('Go to settings')"

    # webhooks
    webhooks_submenu = "span.Polaris-Navigation__Text:contains('Webhooks')"

    # Notification history
    notification_history_submenu = "span.Polaris-Navigation__Text:contains('Notification history')"
