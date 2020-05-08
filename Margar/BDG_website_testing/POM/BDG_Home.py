from Lib import LIB
from selenium.webdriver.common.by import By

class Home:

    #---locators---

    our_courses    = (By.ID, "nav-menu-item-3629")
    our_trainers   = (By.ID, "nav-menu-item-3450")
    blog           = (By.ID, "nav-menu-item-3630")
    about_us       = (By.ID, "nav-menu-item-3442")
    faq            = (By.ID, "nav-menu-item-3445")
    contact_us     = (By.ID, "nav-menu-item-3446")
    language       = (By.ID, "nav-menu-item-3817")

    show_all                  = (By.XPATH, ".//div[@class='eltdf-plf-inner']//li[1]")
    programming               = (By.XPATH, ".//div[@class='eltdf-plf-inner']//li[2]")
    management                = (By.XPATH, ".//div[@class='eltdf-plf-inner']//li[3]")
    finance_and_accounting    = (By.XPATH, ".//div[@class='eltdf-plf-inner']//li[4]")
    human_resources           = (By.XPATH, ".//div[@class='eltdf-plf-inner']//li[5]")
    marketing_and_PR          = (By.XPATH, ".//div[@class='eltdf-plf-inner']//li[6]")
    design                    = (By.XPATH, ".//div[@class='eltdf-plf-inner']//li[7]")

    parent_div = (By.XPATH, './/div[@class="eltdf-cl-inner eltdf-outer-space "]')

    def __init__(self, browser):
        self.browser = browser


