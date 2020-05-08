from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Home:
    #locators
    contuct_us     = (By.ID , "contact-link")
    sign_in        = (By.XPATH , "//a[contains(text(),'Sign in')]")
    women          = (By.LINK_TEXT , "Women")
    dresses        = (By.LINK_TEXT , "Dresses")
    t_shirts       = (By.LINK_TEXT , "T-shirts")
    search_field   = (By.ID , "search_query_top")
    search_btn     = (By.NAME , "submit_search")
    cart           = (By.XPATH , "//span[@class='ajax_cart_no_product']")

    def __init__(self, browser):
        self.browser = browser

    # clicking to contuct us
    def click_contuct_us(self, browser):
        LIB.wait_for_element(self, browser, self.contact_us)
        self.browser.find_element(*self.contact_us).click()

