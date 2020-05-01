from selenium.webdriver.common.by import By

class Home_page:

    #Locators 
    page_logo      = (By.XPATH,'//*[@id="header_logo"]/a/img')
    contact_us     = (By.XPATH,'//*[@id="contact-link"]/a')
    sign_in        = (By.XPATH,'//*[@id="contact-link"]/a')
    women          = (By.XPATH,'//*[@id="block_top_menu"]/ul/li[1]/a')
    dresses        = (By.XPATH,'//*[@id="block_top_menu"]/ul/li[2]/a')
    t_shirts       = (By.XPATH,'//*[@id="block_top_menu"]/ul/li[3]/a')   
    cart           = (By.XPATH, "//a[@title='View my shopping cart']")
    search_field   = (By.ID,       'search_query_top')
    search_submit  = (By.NAME,     'submit_search')
    best_sellers   = (By.LINK_TEXT,'Best Sellers')


    # init
    def __init__(self, browser):
        self.browser = browser