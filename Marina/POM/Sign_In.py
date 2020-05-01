from selenium.webdriver.common.by import By

class Sign_In:
    #locators
    email_address    = (By.ID,"email")
    password         = (By.ID, "passwd")   
    sign_in_bnt      = (By.ID, "SubmitLogin") 
    my_account_title = (By.XPATH,"//h1[text()='My account']")

    def __init__(self, browser):
        self.browser=browser
