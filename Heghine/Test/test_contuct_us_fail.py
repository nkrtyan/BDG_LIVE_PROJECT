from Lib import Lib
from POM.Contact_Us import Contact_Us
from POM.Homepage import Homepage
from selenium import webdriver
import pytest


'''
1. Go to URL
2. Click to Contact US button
3. Fill all fields besides Message field in Contact Us
4. click on Send button
5. Check that Validate message displays 
6. Close browser
'''

def test_2():
    try:
        #open browser
        obj_lib = Lib()
        browser = obj_lib.open_browser()

        # navigate to url
        obj_lib.page_load(browser)

        #create contuct_us object
        obj_contuct_us = Contact_Us(browser)
        obj_home = Homepage(browser)

        #steps
        obj_home.click_contuct_us(browser)
        obj_contuct_us.choose_subject_heading(browser)
        obj_contuct_us.input_email_address()
        obj_contuct_us.input_order_referenc()
        obj_contuct_us.click_send_button()

        #Verify that validation message displayes
        success_message = obj_lib.get_data('contact_us_error_message')
        assert success_message in browser.page_source
        print('Test run pass!')

    except Exception as e:
        obj_lib.save_screenshot(browser)
        print(e)
        raise
    # or 
    #  except Exception as e:
    #         # save the screenshot of the test file which has failed
    #         obj_lib.save_screenshot(browser)
    #         pytest.fail(e)
    #         print('Test 3 failed!')

    finally:
        #Close browser
        obj_lib.close_browser(browser)
            

#Nel, use pytest.fail(e) or just raise for exception in except block