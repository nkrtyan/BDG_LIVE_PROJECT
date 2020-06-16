from selenium import webdriver
from selenium.webdriver.common.by import By
from Lib import Lib

class Homepage:

    # ___Locators___
    contact_us_id =        (By.ID,"contact-link")
    sing_in_xpath =        (By.XPATH,'//*[@id="header"]/div[2]//a')
    cart_xpath =           (By.XPATH,'//*[@id="header"]//div[3]/div/a')
    search_field_id =      (By.ID,"search_query_top")
    search_btn_name =      (By.NAME,"submit_search")
    women_menu_xpath =     (By.XPATH,'//*[@id="block_top_menu"]/ul/li[1]/a')
    dresses_menu_xpath =   (By.XPATH,'//*[@id="block_top_menu"]/ul/li[2]/a')
    t_shirts_menu_xpath =  (By.XPATH,'//*[@id="block_top_menu"]/ul/li[3]/a')
    product_names_xpath =  (By.XPATH,"//ul[@class='product_list grid row']//a[@class='product-name']")
    product_prices_xpath = (By.XPATH,"//div[@class='right-block']//span[@class='price product-price'][contains(text(),'$')]")
    women_tab             =(By.XPATH,"//*[@id='block_top_menu']//a[@title='Women']")
    product_name            =(By.XPATH,"//ul[@class='product_list grid row']//a[@class='product-name']")
    product_price           =(By.XPATH, "//p[@class='product-desc']//following::span[@itemprop='price']")


    def __init__(self, browser):
        self.browser = browser


    #click Contact_Us 
    def click_contuct_us(self, browser):
        Lib.wait_for_element(self, browser, self.contact_us_id)
        self.browser.find_element(*self.contact_us_id).click()

    #return product name:price list
    def give_product_name_price(self, browser):
        produc_name_list = []
        produc_price_list=[]
        Lib.wait_for_elements(self, browser, self.product_name)
        produc_name = self.browser.find_elements(*self.product_name)
        for i in produc_name:
            produc_name_list.append(i.text)
        produc_price = self.browser.find_elements(*self.product_price)
        for i in produc_price:
            produc_price_list.append(i.text)
        del produc_price_list[1::2] #Delete every second element (counting from the firts) 
        return dict(zip(produc_name_list, produc_price_list))