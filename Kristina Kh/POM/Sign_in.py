from selenium import webdriver
from selenium.webdriver.common.by import By

class Sign_in:
    
    # locators
    email_address    = (By.ID, 'email')
    password         = (By.ID, 'password') 
    sign_in_btn      = (By.ID, 'SubmitLogin') 
    my_account_title = (By.ID, "//a[contains(text(),'My account')]") 

    # init
    def __init__(self, browser):
        self.browser  = browser