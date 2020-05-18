from POM.home import Home
from POM.contuct_us import Contuct_us
from lib import LIB
import json


"""
1. Go to URL
2. Click to Contact US button
3. Fill all fields besides Message field in Contact Us
4. click on Send button
5. Check that Validate message displays 
6. Close browser
"""
def test_3():
    try:
        #create objet of the LIB class . open browser and go to URL
        obj_lib = LIB()
        browser = obj_lib.open_browser()
        obj_lib.page_load(browser)
    
        # Creating homepage & contact us page objects
        obj_home = Home(browser)
        obj_contuct_us = Contuct_us(browser)

        # Filling all mandatory fields
        obj_contuct_us.choose_subject_heading(browser)
        obj_contuct_us.input_invalid_email()
        obj_contuct_us.input_reference()
        obj_contuct_us.click_send()

        #check error message
        error_message = obj_lib.get_data("contact_us_error_message")
        assert success_message in browser.page_source
        print("test passed")
    
    except:
        obj_lib.save_screenshot(browser)
        print("Test failed")
    
    finally:
        obj_lib.close_browser(browser)

#Nel, add pytest.fail(e) in except block to see exception in cmd


