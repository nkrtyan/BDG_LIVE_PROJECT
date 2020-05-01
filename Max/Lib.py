from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import json
import os
import sys


class Lib:
    # Activate Chrome driver
    def open_browser(self):
        try:
            with open("config.json") as file:
                data = json.load(file)
                browser = webdriver.Chrome(data["driver_path"])
                browser.maximize_window()
                return browser
        except:
            print("Cannot open browser:(open_browser)")
    
    # Get the link & load
    def page_load(self, browser):
        try:
            with open("config.json") as file:
                data = json.load(file)
            browser.get(data["url"])
        except:
            print("Cannot load the page:(page_load)")

    # Open txt file & write given text
    def write_to_file(self, text):
        try:
            with open("info.txt", "a") as file:
                return file.write("\n" + srt(text))
        except:
            print("Cannot write text:(write_to_file)")

    # Scroll to selected element
    def move_to_element(self, browser, element):
        try:
            act = ActionChains(browser)
            act.move_to_element(element).perform()
        except:
            print("Cannot scroll to element:(move_to_element)")

    # Wating for selected element to appear
    def wait_for_element(self, browser, element):
        try:
            WebDriverWait(browser,60).until(EC.visibility_of_element_located(element))
        except:
            print("Cannot wait for element:(wait_for_element)")

    # Waiting for selected elementS to appear
    def wait_for_elements(self, browser, elements):
        try:
            WebDriverWait(browser,60).until(EC.visibility_of_any_elements_located(elements))
        except:
            print("Cannot wait for element:(wait_for_elements)")

    # Get data from data.json
    def get_data(self, key):
        try:
            with open("data.json") as file:
                data = json.load(file)
            return data[key]
        except:
            print("Cannot getting data from json:(get_data)")

    # Saving screenshots
    def save_screenshot(self, browser):
        current_filename = os.path.basename(sys.argv[0][:-3])
        try:
            browser.save_screenshot(f"Test\{current_filename}_screenshot.png")
        except:
            print("Cannot save screenshot:(save_screenshot)")

    # Closing the browser
    def close_browser(self, browser):
        try:
            browser.quit()
        except:
            print("Cannot close browser:(close_browser)")