from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Sign_in:

    # page locators
    email_address       =(By.ID, "email")
    password            =(By.ID, "passwd")
    sign_in_button      =(By.ID, "SubmitLogin")
    my_account_title    =(By.XPATH, "//h1[text()='My account']")
    
    # page constructor
    def __init__(self, browser):
        self.browser=browser

