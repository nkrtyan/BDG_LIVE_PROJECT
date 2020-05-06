from POM.home import Home
from POM.sign_in import Sign_in
from lib import LIB
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json

def test_1():
    try:
        obj_lib = LIB()
        browser = obj_lib.open_browser()
        browser.page_load(browser)
        obj_sign_in = Sign_in(browser)
        with open ("config.json") as f:
            data = json.load(f)
        email_address = data["email"]
        password = data["password"]
        obj_home = Home(browser)
        browser.find_element(*obj_home.sign_in).click()
        obj_lib.wait_for_element(browser, obj_sign_in.email_address)
        browser.find_element(*obj_sign_in.email_address).send_keys(email_address)
        browser.find_element(*obj_sign_in.password).send_keys(password)
        browser.find_element(*obj_sign_in.sign_in_btn).click()
        browser.find_element(*obj_sign_in.my_account_title)

    except:
        print ("test failed")
        obj_lib.save_screenshot(browser)

    finally:
        obj_lib.close_browser(browser)
    
#---Nel, use comments always
# in except block need to add raise exception for see error in cmd
