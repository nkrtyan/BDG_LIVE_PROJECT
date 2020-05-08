from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import json
import os
import sys


class Lib:

    # create Chrome
    def open_browser(self):
        try:
            with open("config.json") as f:
                data = json.load(f)
            browser = webdriver.Chrome(data['driver_path'])
            browser.maximize_window()
            return browser
        except:
            print("Something went wrong during the browser opening.")
     
    # navigate to given url-page
    def page_load(self, browser):
        try:
            with open ("config.json") as f:
                data = json.load(f)  
            browser.get(data[url])
        except:
            print("Something went wrong during the page loading.") 

    # open txt file with log name and write there given text
    def write_to_file(self, text):
        try:
            with open("log.txt","a") as file:
                return file.write("\n"+str(text))
        except:
            print("Something went wrong with writing.")

    # move to given element
    def move_to_element(self, browser):
        try:
            action = ActionChains(browser)
            action.move_to_element(element).perform()
        except:
            print(" Didn't move to given element.")     
    
    # wait for given element to be visible in UI
    def wait_for_element(self, browser, element):
        try:
            WebDriverWait(browser,60).until(EC.visibility_of_all_element_located(element))
            
        except:
            print("Element isn't visible.") 

    def wait_for_element(self, browser, elements):
        try:
            WebDriverWait(browser,60).until(EC.visibility_of_all_elements_located(elements))
            
        except:
            print("Elements aren't visible.") 

    # data parsing
    def get_data(self, key):
        try:
            with open("data.json") as f:
                data = json.load(f)
            return data[key]
            
        except:
            print("Data wasn't parsing.") 

    
    # save screenshot
    def save_screenshot(self, browser):
        current_filename = os.path.basenae(sys.argv[0][:-3])
        try:
            browser.save_screenshot(f'Test\\{current_filename}_screenshot.png')

        except:
            print("Screenshot was't saved.")
            
    # close browser
    def close_browser(self, browser):
        try:
            browser.quit()
        except:
            print("Something went wrong during the browser closeing.")
     