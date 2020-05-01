from selenium import webdriver
from selenium.webdriver.common.by import By

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
    product_names_xpath =  (By.XPATH,'//*[@id="center_column"]/ul//h5/a')
    product_prices_xpath = (By.XPATH,'//*[@id="center_column"]/ul//span')

    def __init__(self, browser):
        self.browser = browser
