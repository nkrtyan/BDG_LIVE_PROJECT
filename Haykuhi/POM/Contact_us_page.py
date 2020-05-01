from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Contact_us:

    # Contact Us page locators
    subject_heading     =(By.ID, 'id_contact')
    email_address       =(By.ID, 'email')
    order_reference     =(By.ID, 'id_order')
    attach_file         =(By.ID, 'fileUpload')
    submit_button       =(By.ID, 'submitMessage')
    message_field       =(By.ID, 'message')


    # page constructor
    def __init__(self, browser):
        self.browser=browser