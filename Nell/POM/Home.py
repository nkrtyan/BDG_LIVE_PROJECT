from Lib import LIB
from selenium.webdriver.common.by import By

class Home:

    #---locators---
    logo                    =(By.XPATH,"//*[@id='header_logo']//img")
    women_tab               =(By.XPATH,"//*[@id='block_top_menu']//a[@title='Women']")
    dresses_tab             =(By.XPATH,"//*[@id='block_top_menu']//a[@title='Dresses']") 
    t_shirts_tab            =(By.XPATH,"//*[@id='block_top_menu']//a[@title='T-shirts']")
    contact_us              =(By.ID,'contact-link')
    sign_in                 =(By.XPATH,"//*[@id='header']//a[@class='login']")
    cart                    =(By.XPATH,"//div[@class='shopping_cart']/a")
    search_input            =(By.ID,"search_query_top")
    search_btn              =(By.XPATH,"//*[@id='searchbox']//button[@type='submit']")
    product_name            =(By.XPATH,"//ul[@class='product_list grid row']//a[@class='product-name']")
    product_price           =(By.XPATH, "//p[@class='product-desc']//following::span[@itemprop='price']")
    add_to_cart_btn         =(By.XPATH,"//div[@class='button-container']//span[text()='Add to cart']")
    close_popup_icn         =(By.XPATH,"//*[@id='layer_cart']//span[@title='Close window']")
    popup_success_message   =(By.XPATH,"(//*[@id='layer_cart']//h2)[1]")
    

    def __init__(self, browser):
        self.browser = browser
