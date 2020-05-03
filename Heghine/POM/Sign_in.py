  
from  selenium.webdriver.common.by import By

class Sign_in_page:

    # Locators
    email_create       = (By.ID,"email_create")
    em_create_submit   = (By.ID,"SubmitCreate")
    email_address      = (By.ID,"email")
    password           = (By.ID,"passwd")
    sign_in_button     = (By.ID,"SubmitLogin")
    forgot_password    = (By.XPATH,'//*[@id="login_form"]//a')
    
    # Constructor
    def __init__(self, browser):
        self.browser = browser