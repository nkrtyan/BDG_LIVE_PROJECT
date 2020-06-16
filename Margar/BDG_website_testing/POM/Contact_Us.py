from selenium.webdriver.common.by import By
from  Lib import LIB as L
import time

class CONTACT_US:

    # ---locators---
    name_field         = (By.NAME, "your-name")
    email_field        = (By.NAME, "your-email")
    phone_number_field = (By.NAME, "your-subject")
    message_field      = (By.NAME, "your-message")
    send_button        = (By.XPATH, './/input[@type="submit"]')
    fields_error       = (By.XPATH, './/div[@class="wpcf7-response-output wpcf7-display-none wpcf7-validation-errors"]')
    field_error_out    = (By.XPATH, './/span[@class="wpcf7-not-valid-tip"]')

    #init
    def __init__(self, browser):
        self.browser = browser


    def fill_wrong_email(self, browser):
        name_field = browser.find_element(*self.name_field)
        name_field.clear()
        name_field.send_keys(L().get_data("name_for_contact"))
        email_field = browser.find_element(*self.email_field)
        email_field.clear()
        email_field.send_keys(L().get_data("wrong_email_for_contact"))
        phone_field = browser.find_element(*self.phone_number_field)
        phone_field.clear()
        phone_field.send_keys(L().get_data("phone_num_for_contact"))
        message_field = browser.find_element(*self.message_field)
        message_field.clear()
        message_field.send_keys(L().get_data("message_for_contact"))
        browser.find_element(*self.send_button).click()
        time.sleep(8)


    def fill_without_email(self, browser):
        name_field = browser.find_element(*self.name_field)
        name_field.clear()
        name_field.send_keys(L().get_data("name_for_contact"))
        phone_field = browser.find_element(*self.phone_number_field)
        phone_field.clear()
        phone_field.send_keys(L().get_data("phone_num_for_contact"))
        message_field = browser.find_element(*self.message_field)
        message_field.clear()
        message_field.send_keys(L().get_data("message_for_contact"))
        browser.find_element(*self.send_button).click()
        time.sleep(8)

    def fill_without_name(self, browser):
        email_field = browser.find_element(*self.email_field)
        email_field.clear()
        email_field.send_keys(L().get_data("right_email_for_contact"))
        phone_field = browser.find_element(*self.phone_number_field)
        phone_field.clear()
        phone_field.send_keys(L().get_data("phone_num_for_contact"))
        message_field = browser.find_element(*self.message_field)
        message_field.clear()
        message_field.send_keys(L().get_data("message_for_contact"))
        browser.find_element(*self.send_button).click()
        time.sleep(8)