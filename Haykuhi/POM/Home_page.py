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
    product_names   =(By.XPATH, '//a[contains(@class, "product-name")]')
    product_prices  =(By.XPATH, '//span[contains(@class, "price product-price")]')
   


  
    # page constructor
    def __init__(self, browser):
        self.browser=browser

    # find the product names and prices
    def find_products_name_price(self, browser):
        product_names_list = []
        product_prices_list=[]
        # wait for the product names elements to be visible in the UI
        LIB.wait_for_elements(self, browser, self.product_names)
        # locate the product names elements 
        product_names = self.browser.find_elements(*self.product_names)
        # iterate in product names and append the elements' texts to the list
        for i in product_names:
            product_names_list.append(i.text)

        # locate the product prices elements
        product_prices = self.browser.find_elements(*self.product_prices)
        # iterate in product prices and append the elements' texts to the list
        for i in product_prices:
            product_prices_list.append(i.text)
        # delete every second element counting from the first one 
        #del product_prices_list[1::2] 
        # create dictionary from the 2 lists and return it
        return dict(zip(product_names_list, product_prices_list))

#Nel, very good, you unmderstand function meaning