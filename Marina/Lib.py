from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
import json
import os
import sys
#Lib class methods 

class Lib:
    #1. open_browser
    def open_browser(self):
        try:
            with open('config.json') as f:
                data=json.load(f)
            browser = webdriver.Chrome(data['driver_path'])
            browser.maximize_window()
            return browser
        except:
            print("browser did not open!")



    #2. page_load
    def page_load(self, browser):
        try:
            with open('config.json') as f:
                data=json.load(f)
                browser.get(data['url'])
            #self.browser.get(data['url'])
        except:
            print("Page is not load!!!")

    #3. write_to_file
    def write_to_file(self, text):
        try:
            with open ('log.txt',"a") as log_file:
                return log_file.write("\n" + str(text))
        except:
            print("Error! Didn't write to file")

    #4. move_to_element
    def move_to_element(self, browser, element):
        try:
            action = ActionChains(browser)
            action.move_to_element(element).perform()
        except:
            print("Can not move to element!")

    #5. wait_for_element
    def wait_for_element(self, browser, element):
        try:
            WebDriverWait(browser,100).until(EC.visibility_of_element_located(element))
        except:
            print("Element is not visible!") 

    #6. wait_for_elements
    def wait_for_elements(self,browser,elements):
        try:
            WebDriverWait(browser,100).until(EC.visibility_of_all_elements_located(elements))
        except:
            print("All elemets are not visible!")  

    #7. get_data
    def get_data(self, key):
        try:
            with open("data.json") as f:
                data=json.load(f)
                return data[key]
        except:
            print("Error read the keys!")

    #8. save_screenshot
    def save_screenshot(self, browser):
        fln_name=os.path.basename(sys.argv[0][:-3])
        try:
            browser.save_screenshot(f'Test\\{fln_name}_screenshot.png')
        except:
            print("Can not save Screenshot!")
    
    #9. close_browser
    def close_browser(self, browser):
        try:
            self.browser.quit()
        except:
            print("Error! Browser is not close!")




