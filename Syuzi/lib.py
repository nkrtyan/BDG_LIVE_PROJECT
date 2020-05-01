from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Exp
import os
import sys
import json

class LIB:
    #create chrome driver
    def open_browser(self):
        try:
            with open('config.json') as f:
                data = json.load(f) 
                browser = webdriver.Chrome(data['driver_path'])
                browser.maximize_window()
                return browser
        except:
            print("error with open browser")
    

    #navigate to given element
    def page_load(self,browser):
        try:
            with open('config.json') as f:
                data=json.load(f)
                browser.get(data['url'])
        except:
            print ("can't load page")


    
    #open txt file and write there text
    def write_to_file(self,text):
        try:
            with open("text.txt", "w") as f:
                f.write("\n" + str(text))
        except:
            print("error with writing file")



    #move to element
    def move_to_element(self,browser,element):
        try:
            action = ActionChains(browser)
            action.move_to_element(element).perform()
        except:
            print("Can't move")


    #wait for element
    def wait_for_element(self,browser,element):
        try:
            WebDriverWait(browser, 100).until(Exp.visibility_of_element_located(element))
        except:
            print("error with waiting element")


    #data parsing
    def get__data(self, key):
       try:
            with open("data.json") as f:
                data = json.load(f)
                return data[key]
                
        except:
            print("data parsing error")
 



    def save_screeshot(self, browser):
    #save screenshot




    #close browser
    def close_browser(self):
        try:
            browser.quit()
        except:
            print("can't close browser")

