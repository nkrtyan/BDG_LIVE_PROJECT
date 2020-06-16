from selenium.webdriver.common.by import By

class OUR_TRAINERS:

    # ---locators---
    trainer_Nelli = (By.XPATH, './/a[text()="Nelli Krtyan"]')



    #init
    def __init__(self, browser):
        self.browser = browser
