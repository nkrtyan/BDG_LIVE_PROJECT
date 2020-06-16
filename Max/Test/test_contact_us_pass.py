from Lib import Lib
from POM.Homepage import Homepage
from POM.Contact_us import Contact_us
import pytest
# import time



'''
1. Go to URL
2. Click to Contact US button
3. Fill all fields in Contact Us and click on Send button
4. Validate that success message displays
5. Close browser
'''

def test_2():

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
        obj_contact_us.choose_subject_heading(browser)
        obj_contact_us.input_email()
        obj_contact_us.input_order_reference()
        obj_contact_us.input_message()
        obj_contact_us.click_on_send_btn()

# Check that message was sent successfully & print if test pass
        success_message = obj_lib.get_data("contact_us_success_message") # have a question
        assert success_message in browser.page_source
        print("test_2: PASS")


# Take a screenshot when test fails

    except Exception as error:
        obj_lib.save_screenshot(browser)
        pytest.fail(error)
        # print("test_2: FAIL")

# Close browser
    finally:
        # time.sleep(10)
        obj_lib.close_browser(browser)