from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import sys
import json

'''class Lib methods
1.open_browser
2.page_load
3.write_to_file
4.move_to_element
5.wait_for_element
6.wait_for_elements
7.get_data
8.save_screenshot
9.close_browser'''

#1.open_browser
class Lib:
    def open_browser(self):
        try:
            with open('config.json') as file:
                data=json.load(file)
            browser=webdriver.Chrome(data['driver_path'])
            browser.maximize_window()
            return browser
        except:
            print("Something went wrong while opening the browser")

#2.page_load

    def page_load(self, browser):
        try:
            with open ("config.json") as f: 
                data = json.load(f)
            browser.get(data['url'])
        except:
            print("Something went wrong with page loading!")


#3.write_to_file with log name and write there given text
    def write_to_file (self,text):
        try:
            with open("log.txt", "a") as file:
                return file.write("\n"+str(text))
        except:
            print("Error has been faced during writing to file!")

#4.move_to_element
    def move_to_element(self, browser, element):
            try:
                action=ActionChains(browser)
                action.move_to_element(element).perform()
            except:
                print("Impossible moving to element!")

    #5.wait_for_element
    def wait_for_element(self, browser, element):
            try:
                WebDriverWait(browser, 100).until (EC.visibility_of_element_located(element))
            except:
                print("Can't locat element!")

    #6.wait_for_elements
    def wait_for_elements(self, browser, elements):
            try:
                WebDriverWait(browser, 100).until(EC.visibility_of_any_elements_located(elements))
            except:
                print("Can't locate elements!")

    #7.get_data
    def get_data(self, key):
        try:
            with open('data.json') as f:
                data=json.load(f)
                return data[key]
        except:
            print("Can't get data!")

    #8.save_screenshot
    def save_screeshot(self, browser):
        current_filename = os.path.basename(sys.argv[0][:-3])
        try:
            browser.save_screeshot(f'Test\\{current_filename}_screenshot.png')
        except:
            print("Screenshot is not saved")

    #9.close_browser
    def close_browser(self, browser):
        try:
            browser.quit()
        except:

            print("Browser is not  closed!")

