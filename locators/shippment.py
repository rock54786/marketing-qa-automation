class Shipment:
    """
    Shipment page Locators
    """
    add_shipment_btn = "span:contains('Add shipment')"
    tracking_num_txt = "input[name='tracking_number']"
    courier_txt = "input[placeholder='Select courier']"
    save_shipment_btn = "span:contains('Save shipment')"
    view_shipment_btn = "span:contains('View shipment')"
    view_shipment_toast = "div.Polaris-Frame-Toast"
    filter_shipment_txt = "input[placeholder='Filter shipments']"
    shipment_count_lbl = "section[data-test-id='shipments-list-count']>div>span"
    origin_filter = "#Activator-origin"
    destination_filter = "#Activator-destination"
    courier_filter = "#Activator-courier"
    status_filter = "#Activator-status"
    filter_first_item = "div.Polaris-Popover__Section span.Polaris-Checkbox"
    filter_search = "input[placeholder='Search']"
    table_first_row_chkbox = "ul.Polaris-ResourceList>li span.Polaris-Choice__Control"
    table_first_row_tracking_num_txt = "ul.Polaris-ResourceList>li:nth-child(1) div.flex-item:nth-child(1)>div span"
    menu_del_btn = "div.Polaris-ButtonGroup--segmented >div:nth-child(6)"
    pop_delete_shipment_btn = "div[role='dialog'] button.Polaris-Button--primary"
    #shipment detail page
    update_status_btn = "span:contains('Update status')"