from Lib import Lib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# import time

class Contact_us:

    # ___Locators___

    subject_heading_id =   (By.XPATH,"//select[@id='id_contact']")
    email_id =             (By.ID,"email")
    order_referance_name = (By.NAME,"id_order")
    attach_file_id =       (By.ID,"uniform-fileUpload")
    send_btn_id =          (By.ID,"submitMessage")
    message_id =           (By.ID,"message")

    def __init__(self, browser):
        self.browser = browser

# Choosing Subject Heading
    def choose_subject_heading(self, browser): # why use browser to understan browser

        try:
            Lib.wait_for_element(self, browser, self.subject_heading_id)
            choosen_text = Lib.get_data(self, key="subject_heading")
            element = self.browser.find_element(*self.subject_heading_id)
            element.click()
            select = Select(element)
            # time.sleep(7)
            select.select_by_visible_text(choosen_text)
            # time.sleep(10)

        except:
            print("Cannot act: choose_subject_heading")

# Entering valid email
    def input_email(self):

        try:
            # time.sleep(10)
            valid_email = Lib.get_data(self, key="valid_email")
            self.browser.find_element(*self.email_id).send_keys(valid_email)

        except:
            print("Cannot act: input_email")

# Entering referance
    def input_order_reference(self):

        try:
            reference_value = Lib.get_data(self, key="references")
            self.browser.find_element(*self.order_referance_name).send_keys(reference_value)

        except:
            print("Cannot act: input_order_reference")

# Writing message
    def input_message(self):

        try:
            message_text = Lib.get_data(self, key="contact_us_input_message")
            self.browser.find_element(*self.message_id).send_keys(message_text)

        except:
            print("Cannot act: input_message")
            
# Click on send button
    def click_on_send_btn(self):

        try:
            # time.sleep(7)
            self.browser.find_element(*self.send_btn_id).click()
            
        except:
            print("Cannot act: click_on_send_btn")