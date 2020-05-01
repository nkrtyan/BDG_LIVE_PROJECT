from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #Nel, this lib also important, you use it
from selenium.webdriver.support import expected_conditions as expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import json
import os
import sys

'''
Lib class has the following methods
1. open_browser
2. page_load
3. write_to_file
4. move_to_element
5. wait_to_element
6. wait_to_elements
7. get_data
8. save_screenshot
9. close_browser
'''

class LIB:

    #create Chrome driver
    def open_browser(self):
        try:
            with open('config.json') as f:
                data=json.load(f)
            browser=webdriver.Chrome(data['driver_path'])
            browser.maximize_window()
            return browser
        except:
            print("Something went wrong during browser opening!")

    #navigate to url-page
    def page_load(self, browser):
        try:
            with open('config.json') as f:
                data=json.load(f)
            browser.get(data['url'])
        except:
            print("There are some problems with page loading!")

    #open txt file with log name and write there given text
    def write_to_file(self, text):
        try:
            with open("log.txt", "a") as f:
                return f.write("\n" +str(text))
        except:
            print("Error during writting file!")

    #move to given element
    def move_to_element(self, browser, element):
        try:
            action=ActionChains(browser)
            action.move_to_element(element).perform()
        except:
            print("Can't move element!")

    #wait for given element to be vissible in UI
    def wait_for_element(self, browser, element):
        try:
            WebDriverWait(browser, 10).until(EC.persence_of_element_located(element))
        except:
            print("Can't located element!")


    def wait_for_elements(self, browser, elements):
        try:
            WebDriverWait(browser, 100).until(
                EC.persence_of_all_elements_located(elements)
            )
        except:
            print("Can't all elements located!")

    #data parsing
    def get_data(self, key):
        try:
            with open('data.json') as f:
                data=json.load(f)
            return data[key]
        except:
            print("Can't get data!")

    #save screenshot
    def save_screenshot(self, browser):
        current_filename=os.path.basename(sys.argv[0][:-3])
        try:
            browser.save_screenshot(f'Test\\{current_filename}_screenshot.png') #Nel, it will works with one \
        except:
            print("Screenshot is not saved!")

    #close browser
    def close_browser(self, browser):
        try:
            browser.quit()
        except:
            print("There are some problem with closing!")
    
