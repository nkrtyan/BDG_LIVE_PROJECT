from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from lib import LIB


class Home:

    # Home page locators
    contact_us      =(By.ID, 'contact-link')
    search_field    =(By.ID, 'search_query_top')
    sign_in         =(By.CSS_SELECTOR, 'a[title="Log in to your customer account"]')
    cart            =(By.CSS_SELECTOR, 'a[title="View my shopping cart"]')
    women           =(By.LINK_TEXT, 'Women')
    dresses         =(By.LINK_TEXT, 'Dresses')
    t_shirts        =(By.LINK_TEXT, 'T-shirts')


  
    # page constructor
    def __init__(self, browser):
        self.browser=browser

    def click_contact_us(self, browser):
        LIB.wait_for_element(self, browser, self.contact_us)
        self.browser.find_element(*self.contact_us).click()
