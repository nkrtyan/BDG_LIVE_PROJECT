from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Exp
import os
import sys


import json

class Lib:

    def open_browser(self):
        try:
            with open('config.json') as file:
                data = json.load(file) 
            browser = webdriver.Chrome(data['driver_path'])
            browser.maximize_window()
            return browser
        except:
            print("Browser creation error")
 

    def page_load(self, browser):
        try:
            with open('config.json') as file:
               data = json.load(file)
            browser.get(data['url']) 
        except:
            print("Browser url getting error")


    def write_to_file(self, text):
        try:
            with open("text.txt", "a") as file:
                file.write("\n" + str(text))
        except:
            print("Writting error")


    def move_to_element(self, browser, element):
        try:
            act = ActionChains(browser)
            act.move_to_element(element).perform()
        except:
            print("Can  not move")

    def wait_for_element(self, browser, element):
        try:
            WebDriverWait(browser, 100).until(Exp.visibility_of_element_located(element))
        except:
            print("Wait for element error")

    def wait_for_elements(self, browser, elements):
        try:
            WebDriverWait(browser, 100).until(Exp.visibility_of_element_located(elements))
        except:
            print("Wait for elements error")
 
    def get__data(self, key):
        try:
            with open("data.json") as file:
                data = json.load(file)
            return data[key]
        except:
            print("Data getting error")


    def save_screeshot(self, browser):
        current_filname = os.path.basename(sys.argv[0][:-3])
        try:
            browser.save_screeshot(f'Test\{current_filname}_screenshot.png')
        except:
            print("Screenshot is not saved")


    def close_browser(self, browser):
        try:
            browser.quit()
        except:
            print("Browser  did not  close")






