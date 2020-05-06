from POM.Home_page import Home_Page
from POM.Sign_In import Sign_In
from Lib import Lib
import json


# Go tu URL
#Click to Sign in Home page
#Fill email address and password
#Click sign in button
#Verify that you sign in succsessfully

def test_1():
    try:
        obj_lib=Lib()
        #create and open browser
        browser=obj_lib.open_browser()
        #load page
        obj_lib.page_load(browser)
        #load Sign_in page and input data
        obj_sign_in=Sign_In(browser)
        with open("config.json") as f:
            data = json.load(f)
        email_address=data["eMail"]
        password=data["password"]
        obj_home=Home_Page(browser)
        browser.find_element(*obj_home.sign_in).click()
        obj_lib.wait_for_element(browser, obj_sign_in.email_address)
        browser.find_element(*obj_sign_in.email_address).send_keys(email_address)
        browser.find_element(*obj_sign_in.password).send_keys(password)
        browser.find_element(*obj_sign_in.sign_in_bnt).click()
        #Gind "My account" text on Home sign in page
        browser.find_element(*obj_sign_in.my_account_title)
        print("Find 'My accound' text")
    except:
        print("Error sign in!")
        obj_lib.save_screenshot(browser)
    finally:
        obj_lib.close_browser(browser)
    




        