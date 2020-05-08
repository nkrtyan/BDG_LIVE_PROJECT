from POM.Home_page import Home_Page
from Lib import Lib
from POM.Contact_Us import Contact_Us
from selenium.webdriver.support.ui import Select
import json


# Go to URL
# Click "Contact us"
# Fill all field in Contact us and click on Send button
# Validate that Success message display
# Close browser

def test_2():
    try:
        obj_lib=Lib()
        #open browser
        browser=obj_lib.open_browser()
        #load page
        obj_lib.page_load(browser)
        obj_home=Home_Page(browser)
        #find and click on Contact us button
        browser.find_element(*obj_home.contact_us).click()
        obj_contact=Contact_Us(browser)
        obj_lib.wait_for_element(browser, obj_contact.subject_heading)
        #find and select  Subject Heading field
        element = browser.find_element(*obj_contact.subject_heading)
        element.click()
        subject_name=obj_lib.get_data(key='subject_heading')
        select=Select(element)
        select.select_by_visible_text(subject_name)
        
        #find and input in email field
        
        with open("config.json") as f:
            data=json.load(f)
        browser.find_element(*obj_contact.email_address).send_keys(data["eMail"])
        #find and input textin message box
        message_text=obj_lib.get_data(key='contact_us_input_message')
        browser.find_element(*obj_contact.message_box).send_keys(message_text)
        #find Send button and click
        send=browser.find_element(*obj_contact.sent_bnt)
        obj_lib.move_to_element(browser,send)
        send.click()
        #assert seccess message
        success_message=obj_lib.get_data(key="contact_us_success_message")
        assert success_message in browser.page_source
    except:
        print("Contact us page not test is fail ")
        obj_lib.save_screenshot(browser)
    finally:
        #close browser
        obj_lib.close_browser(browser)


#Nel, good







    


    


    

