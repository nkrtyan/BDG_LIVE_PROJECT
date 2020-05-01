from selenium.webdriver.common.by import By
class Home_Page:

    #locators
    contact_us  = (By.XPATH,"//div[@id='contact-link']//a")
    sign_in     = (By.XPATH, "//a[@class='login']")
    search      = (By.ID, "search_query_top")
    add_to_cart = (By.XPATH, "//a[@href='http://automationpractice.com/index.php?controller=order']")
    li_women    = (By.XPATH, "//a[@title='Women']")
    li_dresses  = (By.XPATH, "//a[@title='Dresses']")
    li_t_shirts = (By.XPATH, "//a[@title='T-shirts']")
    pic_names   = (By.XPATH, "//ul[@id='homefeatured']//child::li")  #------7 hat a berum
    #price       = (By.XPATH, "//span[@class='price product-price' and @itemprop='price']") 28 hata berum mez petq e arajin 14  
    price       = (By.XPATH, "//*[@id='homefeatured']/li//div[2]//span[@class='price product-price']") # 14 hat a berum 

  

    def __init__(self, browser):
        self.browser=browser

