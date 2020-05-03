  
from selenium.webdriver.common.by import By

class Home_page:

    # Locators 
    page_logo      = (By.XPATH,'//*[@id="header_logo"]/a/img')
    contact_us     = (By.XPATH,'//*[@id="contact-link"]/a')
    sign_in        =(By.XPATH,"//*[@id='header']//a[@class='login']")    
    women          = (By.XPATH,'//*[@id="block_top_menu"]/ul/li[1]/a')
    dresses        = (By.XPATH,'//*[@id="block_top_menu"]/ul/li[2]/a')
    t_shirts       = (By.XPATH,'//*[@id="block_top_menu"]/ul/li[3]/a')
    search_field   = (By.ID,'search_query_top')
    search_submit  = (By.NAME,'submit_search')
    cart           = (By.CSS_SELECTOR,'a[title="View my shopping cart"]')
    best_sellers   = (By.LINK_TEXT,'Best Sellers')

    # Constructor
    def __init__(self, browser):
        self.browser = browser