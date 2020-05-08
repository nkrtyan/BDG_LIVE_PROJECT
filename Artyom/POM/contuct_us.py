from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from lib import LIB

class Contuct_us:

    #locators
    subject_heading   = (By.ID , "uniform-id_contact")
    email_address     = (By.ID , "email")
    order_reference   = (By.ID , "id_order")
    attach_file       = (By.ID , "fileUpload")
    message_field     = (By.ID , "message")
    send_button       = (By.ID , "submitMessage")

#methods
    def __init__(self , browser):
        self.browser = browser

    #choose subject heading
    def choose_subject_heading(self, browser):
        LIB.wait_for_element(self, browser , self.subject_heading)
        select_text = LIB.get_data(self , key = "subject_heading")
        element = self.browser.find_element(*self.subject_heading)
        element.click()
        select = Select(element)
        select.select_by_visible_text(select_text)

    # input email address
    def input_email_address(self):
        email = LIB.get_data(self, key = "valid_email")
        self.browser.find_element(*self.email_address).send_keys(email)
    
    # input order reference
    def input_reference(self):
        ref = LIB.get_data(self, key = "references")
        self.browser.find_element(*self.order_reference).send_keys(ref)
    
    # input message field
    def input_message(self):
        mes = LIB.get_data(self, key = "contact_us_input_message")
        self.browser.find_element(*self.message_field).send_keys(mes)
    
    # click send button
    def click_send(self):
        self.browser.find_element(*self.send_button).click()
    
    # input invalid email
    def input_invalid_email(self):
        inv_email = LIB.get_data(self , key = "invalid_email")
        self.browser.find_element(*self.email_address).send_keys(inv_email)
    
