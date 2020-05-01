from selenium.webdriver.common.by import By

class Sign_in:

    #Locators
    email_address    = (By.ID, 'email')
    password         = (By.ID, 'passwd')
    sign_in_btn      = (By.ID, 'SubmitLogin')
    my_account_title = (By.XPATH, "//h1[text()='My account']")
    forgot_password  = ( By.XPATH, '//a[@href="http://automationpractice.com/index.php?controller=password"]')

    #init
    def __init__(self, browser):
        self.browser=browser