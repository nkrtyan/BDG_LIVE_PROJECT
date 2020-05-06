from selenium.webdriver.common.by import By

class Home:

    #---locators---

    contact_us         = (By.XPATH, "//a[@title='Contact Us']")
    sing_in            = (By.CLASS_NAME, 'login')
    sign_out           = (By.XPATH, "//a[@class='logout']")
    search             = (By.ID, 'search_query_top')
    chart              = (By.XPATH, "//a[@title='View my shopping cart']")
    menu_women         = (By.XPATH, "//a[@title='Women']")
    menu_content       = (By.XPATH, "//ul[@class='sf-menu clearfix menu-content sf-js-enabled sf-arrows']/child::li")
    product_name       = (By.XPATH, "//*[@id='center_column']/ul/li/div/div[2]/h5/a")
    product_price      = (By.XPATH, "//*[@id='center_column']/ul/li/div/div[2]/div[1]/span[@class='price product-price']")
    
    
    #init
    def __init__(self, browser):
        self.browser = browser
