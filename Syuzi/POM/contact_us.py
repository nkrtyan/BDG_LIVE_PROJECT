  
from selenium.webdriver.common.by import By

class Contact_us:

    #locators
    return_home      = (By.XPATH, "//a[@class='home']")
    subject_heading  = (By.ID, "id_contact")
    email_field      = (By.ID, "email")
    other_reference  = (By.ID, "id_order")
    attach_file      = (By.ID, "fileUpload")
    send             = (By.XPATH, "//span[contains(text(),'Send')]")
    message          = (By.ID,"//span[contains(text(),'Send')]")

