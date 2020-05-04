from selenium.webdriver.common.by import By


class Contact_us_page:

    # Locators
    subject_heading  = (By.ID,'id_contact')
    email_address    = (By.ID,'email')
    order_reference  = (By.ID,'id_order')
    attach_file      = (By.LINK_TEXT,'Choose File')
    send_button      = (By.ID,'submitMessage')
    message_field    = (By.ID,'message')

    # Constructor
    def __init__(self, browser):
        self.browser = browser