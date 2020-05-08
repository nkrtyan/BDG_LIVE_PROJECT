from selenium.webdriver.common.by import By

class Contact_Us:
    #locators

    subject_heading = (By.ID,"id_contact")
    email_address   = (By.ID,"email")
    order_reference = (By.XPATH, "//select[@name='id_order']")
    attach_file     = (By.ID, "fileUpload")
    choose_bnt      = (By.XPATH,"//span[@class='action']")
    sent_bnt        = (By.XPATH,"//span[text()='Send']")
    message_box     = (By.ID,"message")

    def __init__(self, browser):
        self.browser=browser

