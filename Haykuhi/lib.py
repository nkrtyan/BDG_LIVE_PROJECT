from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
import json
import os
import sys

'''
LIB class includes the following methods:
1. open_browser
2. page_load
3. write_to_file
4. move_to_element
5. wait_for_element
6. wait_for_elements
7. get_data
8. save_screenshot
9. close_browser
'''

class LIB:
    
    # create Chrome driver
    def open_browser(self):
        try:
            with open('config.json') as f:
                data=json.load(f)
            browser=webdriver.Chrome(data['driver_path'])
            browser.maximize_window()
            return browser
        except:
            print("something failed when opening the browser!")

    # navigate to the given url
    def page_load(self, browser):
        try:
            with open('config.json') as f:
                data=json.load(f)
            browser.get(data['page_url'])   #why we use browser.get instead of self.browser.get?
        except:
            print("Something failed when loading the page!")

    # open a txt file and write a given info in it
    def write_to_file(self, text):
        try:
            with open('log.txt', 'w+') as file:
                file.write('/n' + str(text))
        except:
            file.close()
            print('Something failed when opening a txt file!')

    # move to a given element
    def move_to_element(self, browser, element):
        try:
            action=ActionChains(browser)
            action.move_to_element(element).perform()
        except:
            print('Something went wrong when moving to the element!')
    
    # wait for a given element to be visible on the UI
    def wait_for_element(self, browser, element):
        try:
            WebDriverWait(browser, 100).until(EC.visibility_of_element_located(element))
        except:
            print('The element is not located!')

    # wait for given elements to be visible on the UI
    def wait_for_elements(self, browser, elements):
        try:
            WebDriverWait(browser, 100).until(EC.visibility_of_elements_located(elements))
        except:
            print('The elements are not located!')
    
    # data parsing from the data.json file
    def get_data(self, key):
        try:
            with open('data.json') as f:
                data=json.load(f)
            return data[key]
        except:
            print("Something failed when parsing data!")

    # save the name of the current py file
    def save_screenshot(self, browser):
        current_filename=os.path.basename(sys.argv[0][:-3])
        try:
            browser.save_screenshot(f'Test\{current_filename}_screenshot.png')
        except:
            print('Failed when saving a screenshot!')

    # close the browser
    def close_browser(self, browser):
        try:
            browser.quit()
        except:
            print('Failed when closing the browser!')








