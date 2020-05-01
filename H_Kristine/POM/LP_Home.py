from selenium.webdriver.common.by import By

class Home:

    #---locators---

    contact_us         = (By.XPATH, "//a[@title='Contact Us']")
    sign_out           = (By.XPATH, "//a[@class='logout']")
    search             = (By.ID, 'search_query_top')
    chart              = (By.XPATH, "//a[@title='View my shopping cart']")
    menu_content       = (By.XPATH, "//ul[@class='sf-menu clearfix menu-content sf-js-enabled sf-arrows']/child::li[i]")
    product_name       = (By.XPATH, "//*[@id='homefeatured']/li[i]//div[2]/h5/a[@class='product-name']")
    product_price      = (By.XPATH, "//*[@id='homefeatured']/li[i]//div[2]//span[@class='price product-price']")

    #init
    def __init__(self, browser):
        self.browser=browser
