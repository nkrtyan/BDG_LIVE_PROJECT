from selenium import webdriver
from selenium.webdriver.common.by import By

class Contact_us:

    # ___Locators___

    subject_heading_id =   (By.ID,"id_contact")
    email_id =             (By.ID,"email")
    order_referance_name = (By.NAME,"id_order")
    attach_file_id =       (By.ID,"uniform-fileUpload")
    send_btn_id =          (By.ID,"submitMessage")
    message_id =           (By.ID,"message")

    def __init__(self, browser):
        self.browser = browser