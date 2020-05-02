from selenium.webdriver.common.by import By

class Home_page:

    #LOCATORS
    logo            = (By.XPATH, "//img[@class='logo img-responsive']")
    search_field    = (By.ID, "search_query_top")
    sumbit_search   = (By.NAME, 'submit_search')
    women_dress_btn = (By.XPATH, "//a[@class='sf-with-ul'][contains(text(),'Women')]")
    dresses_btn     = (By.XPATH, "//li[@class='sfHover']//a[@class='sf-with-ul'][contains(text(),'Dresses')]")
    t_shirts_btn    = (By.XPATH, "//li[@class='sfHover']//a[contains(text(),'T-shirts')]")
    best_seller_btn = (By.XPATH, "//a[@class='blockbestsellers']")
    cart_btn        = (By.CSS_SELECTOR, "a[title='View my shopping cart']")

    def __init__(Self,browser):
        self.browser=browser




