from  selenium.webdriver.common.by import By

class Sign_in:
    #locators
    email_adr   = (By.ID, 'email')
    password    = (By.ID, 'passwd')
    sign_in     = (By.ID, 'SubmitLogin')
    forgot_pass = ( By.XPATH, "//a[contains(text(),'Forgot your password?')]")

    def __init__(self,browser):
        self.browser=browser
    
    # def fill_em_adress(self):

    # def fill_password(self):

    # def click_sign_in(self):
    
    # def cl_forg_pass(self:)
