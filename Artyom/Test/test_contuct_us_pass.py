from POM.home import Home
from POM.contuct_us import Contuct_us
from lib import LIB
import json


"""
1. Go to URL
2. Click to Contuct US button
3. Fill all fields in Contuct US and click on Send button
4. Validate that success message displayed
5. Close browser
"""
def test_2():

    try:
        #create objet of the LIB class . open browser and go to URL
        obj_lib = LIB()
        browser = obj_lib.open_browser()
        obj_lib.page_load(browser)

        # Creating homepage & contact us page objects
        obj_home = Home(browser)
        obj_contuct_us = Contuct_us(browser)

        # navigating to the contuct us page
        obj_home.click_contuct_us(browser)

        # Filling all mandatory fields
        obj_contuct_us.choose_subject_heading(browser)
        obj_contuct_us.input_email_address()
        obj_contuct_us.input_reference()
        obj_contuct_us.input_message()
        obj_contuct_us.click_send()

        #check success message
        success_message = obj_lib.get_data("contact_us_success_message")
        assert success_message in browser.page_source
        print("test passed")
    
    except:
        obj_lib.save_screenshot(browser)
        print("Test failed")
    
    finally:
        obj_lib.close_browser(browser)





