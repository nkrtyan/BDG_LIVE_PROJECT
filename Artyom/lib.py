from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import json
import os
import sys

class LIB :
    #create Chrome driver
    def open_browser(self):
        try:
            with open ("config.json") as f:
                data = json.load(f)
            browser = webdriver.Chrome(data["driver_path"])
            browser.maximize_window()
        except:
            print("Something went wrong during browser opening")

    #navigate to given url
    def page_load (self, browser):
        try:
            with open ("config.json") as f:
                data = json.load(f)
            browser.get(data["url"])
        except:
            print("Something went wrong during page loading")
    
    #open txt file with log name and write there given text
    def write_to_file (self, text):
        try:
            with open ("log.txt" , "w+") as file:
                return file.write ("\n" + str(text))
        except:
            print ("Error during writing the file")
    
    #move to givent element
    def move_to_element(self, browser, element):
        try:
            action = ActionChains(browser)
            action.move_to_element(element).perform()
        except:
            print("Cannot move to the given element")
    
    #wait for given element to be visible in UI
    def wait_for_element(self, browser, element):
        try:
            WebDriverWait(browser, 100).until(EC.visibility_of_element_located(element))
        except:
            print("element is not visible")
    #wait for given elements to be visible in UI
    def wait_for_elements(self, browser, elements):
        try:
            WebDriverWait(browser, 100).until(EC.visibility_of_elements_located(elements))
        except:
            print("elements are not visible")
    
    #data parsing
    def get_data(self, key):
        try:
            with open ("data.json") as f:
                data = json.load(f)
            return data[key]
        except:
            print("error during data getting")
    
    #save screenshot
    def save_screenshot (self, browser):
        current_filename = os.path.basename(sys.argv[0]:[-3])  #---Nel, should be [0][:-3]
        try:
            browser.save_screenshot(f'Test\{current_filename}_screenshot.png')
        except:
            print ("Screenshot is not saved")
    
    #close browser
    def close_browser (self, browser):
        try:
            browser.quit()
        except:
            print ("driver is not closed")

    



