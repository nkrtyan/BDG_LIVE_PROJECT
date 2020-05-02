from selenium.webdriver.common.by import By

class Home:

    # ---locators---

    contact_us         = (By.XPATH, "//a[@title='Contact Us']")
    sign_in            = (By.XPATH, "//a[contains(text(),'Sign in')]")
    sign_out           = (By.XPATH, "//a[@class='logout']")
    search             = (By.ID, 'search_query_top')
    chart              = (By.XPATH, "//a[@title='View my shopping cart']")
    women              = (By.XPATH, "//a[@class='sf-with-ul'][contains(text(),'Women')]")
    dresses            = (By.XPATH, "//*[@id='block_top_menu']/ul/li[2]/a[1]")
    t-shirts           = (By.XPATH, '//*[@id="block_top_menu"]/ul/li[3]/a')
    
    
    # init
    def __init__(self, browser):
        self.browser=browser
