from POM.Home_page import Home
from POM.Sign_in_page import Sign_in
from lib import LIB
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
import pytest

'''
1. Navigate to the URL
2. Click on Women tab
3. Open file with 'log' name
4. Write in the file all the found products names with their prices
5. Close the browser
'''
# as a result returns a blank dictionary in txt file, can not find the problem 

def test_4():

        try:
            # create lib page object  
            obj_lib=LIB()

            # open browser
            browser=obj_lib.open_browser()

            # navigate to the url
            obj_lib.page_load(browser)

            # wait for the Women tab to be visible in Home page, locate it and click on it
            obj_home=Home(browser)
            obj_lib.wait_for_element(browser, obj_home.women)
            browser.find_element(*obj_home.women).click()

            # return dictionary with Women tab's products names and prices  
            products_names_prices = obj_home.find_products_name_price(browser)

            # write the products names and prices in log.txt file
            obj_lib.write_to_file(products_names_prices)    #!!!returns a blank dictionary in txt file, can not find the problem :(

        except Exception as e:
            # save the screenshot of the test file which has failed
            obj_lib.save_screenshot(browser)
            pytest.fail(e)
            print('Test 4 failed!')

        finally:
            # close the browser
            obj_lib.close_browser(browser)