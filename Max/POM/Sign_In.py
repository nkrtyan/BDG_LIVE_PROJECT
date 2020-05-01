from selenium import webdriver
from selenium.webdriver.common.by import By

class Sing_in:

    # ___Locators___

    email_id =               (By.ID,"email")
    password_id =            (By.ID,"passwd")
    submit_btn_id =          (By.ID,"SubmitLogin")
    my_account_title_xpath = (By.XPATH,"//*[@id='center_column']/h1")

    def __init__(self, browser):
        self.browser = browser