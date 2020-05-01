from selenium.webdriver.common.by import By

class Contact_us_page:

    # Locators
    subject_heading  = ( By.ID, 'id_contact')
    email_address    = ( By.ID, 'email')
    order_reference  = ( By.ID, 'id_order')
    upload_field     = (By.ID, 'fileUpload')
    send_button      = (By.XPATH,"//span[text()='Send']")
    message_field    = ( By.ID, 'message')



    # init
    def __init__(self, browser):
        self.browser = browser
    
    #Nell jan pls  explain how i can locate upload button not field?
    #Ann jan, you firstly locate attache file element and send_keys the image giving the path
    def uploade_file(self, browser):
        file_selected    = (By.XPath, '//*[@id="fileUpload"]')
        browser.find_element(*file_selected).send_keys('local path of your image')