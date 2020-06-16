from selenium import webdriver
from POM.Sign_in import Sign_in
from POM.Home import Home
from POM.Contact_Us import Contact_Us
from Lib import Lib
from selenium.webdriver.common.key import Keys
import json

'''
1. Go to URL
2. Click Sign In in Home Page
3. Fill email address and password
4. Click Sign In buttton
5. Verify that you signed sucessfuly
'''


def test_1():
    try:

        #open browser
        obj_lib = Lib()
        browser = obj_lib.open_browser()

        #navigate to url
        obj_lib.page_load(browser)

        #get  email and password from config file
        with open("config.json") as f:
            data = json.load(f)
            email_address = data["email"]
            password = data["password"]

        # Create Home page object
        obj_home = Home(browser)

        #click on Sign In
        browser.find_element(*obj_home.sign_in).click()
        #create Sign in object
        obj_sign_in = Sign_in(browser)

        # Fill email and password
        obj_lib.write_to_file(browser, obj_sign_in.email)
        browser.find_element(*obj_sign_in.email).send_keys(email_address)
        browser.find_element(*obj_sign_in.password).send_keys(password)
        #Click on Sign in button
        browser.find_element(*obj_sign_in.sign_in_btn).click()

        #verify that you were signed 
        browser.find_element(*obj_sign_in.my_account_title)
        print("Test run!")   
        
    
    
    except Exception as e:
        print(e)
        obj_lib.save_screenshot(browser) 
        print('Test run failed!')

    finally:

        #Close browser
        obj_lib.close_browser(browser)
        
#Nel, correct
