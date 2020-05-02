from selenium.webdriver.common.by import By

class Contact_Us:

    # locators

    send_message_titl = (By.XPATH, "//*[@class='page-subheading']")
    subject_heading   = (By.XPATH, "//select[@id='id_contact']")
    email_address     = (By.ID, 'email')
    order_reference   = (By.ID, 'id_order')
    attach_file       = (By.ID, 'fileUpload')
    message           = (By.ID, 'message')
    submit_message    = (By.XPATH, "//button[@id='submitMessage']")

    # init
    def __init__(self, browser):
        self.browser=browser
