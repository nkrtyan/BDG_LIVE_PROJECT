from POM.home import Home
from POM.sign_in import Sign_in
from lib import LIB
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

"""
Scenario steps
1. Go to URL
2. Click to Sign In in Home Page
3. Fill email address and password
4. Click Sign In button
5. Verify that you signed successfully

"""


def test_1():
    try:
        
        # get emai and password from config file
        with open ("config.json") as f:
            data = json.load(f)
        email_address = data["email"]
        password      = data["password"]

        # open the browser
        obj_lib = LIB()
        browser = obj_lib.open_browser()

        # navigate to url
        browser.page_load(browser)

        # create object of Sign_in class
        obj_sign_in = Sign_in(browser)

        # create object of Home class
        browser.find_element(*obj_home.sign_in).click()

        # waiting for email field, and filling email and password
        obj_lib.wait_for_element(browser, obj_sign_in.email_address)
        browser.find_element(*obj_sign_in.email_address).send_keys(email_address)
        browser.find_element(*obj_sign_in.password).send_keys(password)

        # click to sign_in button
        browser.find_element(*obj_sign_in.sign_in_btn).click()

        # check that we are in the correct page
        browser.find_element(*obj_sign_in.my_account_title)

    except:
        obj_lib.save_screenshot(browser)
        print ("test failed")
        
    finally:
        obj_lib.close_browser(browser)
    
#---Nel, use comments always
# in except block need to add raise exception for see error in cmd
