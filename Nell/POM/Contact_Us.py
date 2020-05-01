from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Lib import LIB


class Contact_Us:

    #---locators---
    subject_heading      = (By.XPATH, '//select[@id="id_contact"]')
    email_address        = (By.ID, 'email')
    order_reference      = (By.ID, 'id_order')
    input_message_text   = (By.ID, 'message')
    send_button          = (By.ID, 'submitMessage')


    #---methods---
    def __init__(self, browser):
        self.browser = browser

        



