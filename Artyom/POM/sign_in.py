from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.keys import Keys
 

class Sign_in:
    
    #locators of sing in page
    email_address       = (By.ID , "email")
    password            = (By.ID , "passwd")    
    sign_in_btn         = (By.ID , "SubmitLogin")
    my_account_title    = (By.XPATH , "//a[contains(text(),'My account')]")

def __init__(self, browser):
    self.browser = browser


