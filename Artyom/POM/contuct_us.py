from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.keys import Keys

class Contuc_us:

    #locators
    subject_heading   = (By.ID , "uniform-id_contact")
    email_address     = (By.ID , "email")
    order_reference   = (By.ID , "id_order")
    attach_file       = (By.ID , "fileUpload")
    message_field     = (By.ID , "message")

def __init__(self , browser):
    self.browser = browser