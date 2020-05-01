from selenium.webdriver.common.by import By

class Contact_us_page:

    # Locators
    subject_heading  = ( By.ID, 'id_contact')
    email_address    = ( By.ID, 'email')
    order_reference  = ( By.ID, 'id_order')
    upload_field     = (By.ID, 'fileUpload')
    send_button      = (By.XPATH,"//span[text()='Send']")
    message_field    = ( By.ID, 'message')
#Nell jan pls  explain how i can locate upload button not field?

    # init
    def __init__(self, browser):
        self.browser = browser