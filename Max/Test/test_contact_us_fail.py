from Lib import Lib
from POM.Homepage import Homepage
from POM.Contact_us import Contact_us
import pytest
# import time

'''
1. Go to URL
2. Click to Contact US button
3. Fill all fields besides Message field in Contact Us
4. click on Send button
5. Check that Validate message displays 
6. Close browser
'''

def test_3():

    try:

# Open browser, maximazie window, get URL
        obj_lib = Lib()
        browser = obj_lib.open_browser()
        obj_lib.page_load(browser)

# Creating homepage & contact us page objects
        obj_homepage = Homepage(browser)
        obj_contact_us = Contact_us(browser)

# Click on contact us btn fill all fields send message
        obj_homepage.click_on_contact_us(browser)
        obj_contact_us.choose_subject_heading(browser)  # have a question for this part ?
        obj_contact_us.input_email()
        obj_contact_us.input_order_reference()
        # obj_contact_us.input_message()
        obj_contact_us.click_on_send_btn()

# Check that message was sent successfully & print if test pass
        error_message = obj_lib.get_data("contact_us_error_message") # have a question why not use key
        assert error_message in browser.page_source
        print("test_3: PASS")


# Take a screenshot when test fails

    except Exception as error :
        obj_lib.save_screenshot(browser)
        pytest.fail(error)
        print("test_3: FAIL")

# Close browser

    finally:
        # time.sleep(10)
        obj_lib.close_browser(browser)