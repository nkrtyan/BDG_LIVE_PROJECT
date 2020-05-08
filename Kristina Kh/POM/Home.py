from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.key import Keys
from selenium.webdriver.support.ui import Select

class Home:

    # ---locators---

    contact_us         = (By.XPATH, "//a[@title='Contact Us']")
    sign_in            = (By.XPATH, "//a[contains(text(),'Sign in')]")
    sign_out           = (By.XPATH, "//a[@class='logout']")
    search_btn         = (By.ID, 'search_query_top')
    chart              = (By.XPATH, "//a[@title='View my shopping cart']")
    women_tab          = (By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]//a[@title = "Women"]')
    dresses_tab        = (By.XPATH, "//*[@id='block_top_menu']/ul/li[2]/a[1]")
    t_shirts_tab       = (By.XPATH, '//*[@id="block_top_menu"]/ul/li[3]/a')
    menu_content       = (By.XPATH, "//ul[@class='sf-menu clearfix menu-content sf-js-enabled sf-arrows']/child::li[i]")
    product_name       = (By.XPATH, "//ul[@class='product_list grid row']//a[@class='product-name']")
    product_price      = (By.XPATH, "//p[@class ='product-desc']//following::span[@itemprop='price']")
    
    
    # init
    def __init__(self, browser):
        self.browser = browser

    # click contact us 
    def click_contact_us(self, browser):
        self.browser.find_element(*self.contact_us).click()

    #return product name and price lists
    def give_product_name_and_price(self, browser):
        product_name_list = []
        product_price_list = []
        Lib.wait_for_elements(self, browser, self.product_name)
        product_names = self.browser.find_elements(*self.product_name)
        for i in products_names:
            product_name_list.append(i.text)
        product_prices = self.browser.find_elements(*self.product_price)
        for i in product_prices:
            product_price_list.append(i.text)
    

    #Delete every second element
    del product_price_list[1::2] 
    return dict(zip(product_name_list,product_price_list))