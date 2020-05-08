from POM.Contact_Us import Contact_Us
from POM.Home import Home
from Lib import Lib
from selenium import webdriver
from selenium.webdriver.common.key import Keys

'''
1. Go to URL
2. Click to Contact Us button
3. Fill all fields in  Contact Us and click on Send button
4. Validate that success message displays
5. Close browser
'''
def test_2():
    try:
        #open browser
        obj_lib = Lib()
        browser = obj_lib.open_browser()

        # navigate to URL
        obj_lib.page_load(browser)

        #create contact us and home object
        obj_contact_us = Contact_Us(browser)
        obj_home = Home(browser)

        # steps
        obj_home.click_contact_us(browser)
        obj_contact_us.choose_subject_heading(browser)
        obj_contact_us.input_email_address()
        obj_contact_us.input_order_reference()
        obj_contact_us.input_message()
        obj_contact_us.click_contact_us()
        # verify that message is sending successfully
        success_message = obj_lib.get_data('contact_us_success_message')
        assert success_message in browser.page_source
        print ('Test run pass!')
    except:

        obj_lib.save_screenshot(browser) 
        print('Test run failed!')
    finally:

        #Close browser
        obj_lib.close_browser(browser)       
