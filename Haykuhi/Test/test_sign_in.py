from POM.Home_page import Home
from POM.Sign_in_page import Sign_in
from lib import LIB
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json


def test_1():
    try:
        obj_lib=LIB()
        browser=obj_lib.open_browser()
        browser.page_load(browser)

        obj_sign_in=Sign_in(browser)

    except:
        print('Test failed')
        obj_lib.save_screenshot(browser)
        

