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

    def __init__(self, browser):
        self.browser = browser

# Click on contact us btn

    def click_on_contact_us(self, browser):
        try:
            Lib.wait_for_element(self, browser, self.contact_us_id)
            self.browser.find_element(*self.contact_us_id).click()
        except:
            print("Cannot act: click_on_contact_us")

# Get product name and price

    def get_product_name_price(self, browser):
        prod_name_list = []
        prod_price_list = []
        Lib.wait_for_element(self, browser, self.product_names_xpath)

        prod_names = self.browser.find_elements(*self.product_names_xpath)
        for each in prod_names:
            prod_name_list.append(each.text) 

        prod_prices = self.browser.find_elements(*self.product_prices_xpath)
        for each in prod_prices:
            prod_price_list.append(each.text)
            
        # del prod_price_list[1::2]
        return dict(zip(prod_name_list, prod_price_list))