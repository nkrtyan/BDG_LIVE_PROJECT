from selenium.webdriver.common.by import By
from Lib import LIB

class ABOUT_US:

    # ---locators---
    our_mission    =  (By.XPATH, './/div[@class="eltdf-title-info"]//h1[@class="eltdf-page-title entry-title"]')
    home           =  (By.XPATH, './/a[text()="Home"]')
    text_info_1    =  (By.XPATH, './/div[@class="wpb_wrapper"]//p[2]')
    text_info_2    =  (By.XPATH, './/div[@class="wpb_wrapper"]//p[3]')
    founders_title =  (By.XPATH, './/div[@class="eltdf-st-inner"]//h2')
    founder_1      =  (By.XPATH, './/div[@class="eltdf-section-title-holder  eltdf-st-standard eltdf-st-title-left eltdf-st-normal-space "]//div[@class="eltdf-st-inner"]//h2')
    founder_2      =  (By.XPATH, './/div[@class="eltdf-iwt clearfix  eltdf-iwt-icon-left eltdf-iwt-icon-medium eltdf-iwt-position-text_center"]//following::h2')


    #init
    def __init__(self, browser):
        self.browser = browser

    def return_text(self, browser, element):
        text = browser.find_element(*element)
        return text.text