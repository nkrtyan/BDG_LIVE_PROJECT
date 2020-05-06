from POM.Home_page import Home
from POM.Sign_in_page import Sign_in
from lib import LIB
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
import pytest


def test_1():
    try:
        #create lib page object
        obj_lib=LIB()

        # open browser
        browser=obj_lib.open_browser()
        
        # navigate to the url
        browser.page_load(browser)

        # create Sign_in_page object
        obj_sign_in=Sign_in(browser)

        # parse data from config.json 
        with open('config.json') as f:
            data=json.load(f)
        email_address=data['email']
        password=data['password']

        # create Home_page object 
        obj_home=Home(browser)

        # click on Sign In button of the Home page
        browser.find_element(*obj_home.sign_in).click()

        # wait for the element to be visible in Sign in page
        obj_lib.wait_for_element(browser, obj_sign_in.email_address)

        # submit the email address and password parsed from config.json to be signed with
        browser.find_element(*obj_sign_in.email_address).send_keys(email_address)
        browser.find_element(*obj_sign_in.password).send_keys(password)

        # click the sign in button
        browser.find_element(*obj_sign_in.sign_in_button).click()


    except:
        print('Test 1 failed!')

        # save the screenshot of the test file which has failed
        obj_lib.save_screenshot(browser)
    
    finally:
        # close the browser
        obj_lib.close_browser(browser)        

