from Lib import Lib
from POM.Homepage import Homepage
from POM.Sign_in import Sing_in
import json
import time
'''
Scenario steps
1. Go to URL
2. Click to Sign In in Home Page
3. Sing in with valid data
5. Verify that you are sign in successfully

'''

def test_4():
    try:
    
    # Get data for sing in form config.json 
        with open("config.json") as file:
            data = json.load(file)
        email_address = data["email"]
        password      = data["password"]

    # Open browser, maximazie window, get URL
        obj_lib = Lib()
        browser = obj_lib.open_browser()
        obj_lib.page_load(browser)

    # Go Home page & click on Sing in btn
        obj_homepage = Homepage(browser)
        browser.find_element(*obj_homepage.sing_in_xpath).click()

    # Go sing in page
        obj_sing_in = Sing_in(browser)

    # Sing in with valid data
        obj_lib.wait_for_element(browser, obj_sing_in.email_id)
        browser.find_element(*obj_sing_in.email_id).send_keys(email_address)
        browser.find_element(*obj_sing_in.password_id).send_keys(password)
        browser.find_element(*obj_sing_in.submit_btn_id).click()

    # Verify that i sign in successfully
        obj_lib.wait_for_element(browser, obj_sing_in.my_account_title_xpath)
        browser.find_element(*obj_sing_in.my_account_title_xpath)

        print("TEST_1: PASS")

    except Exception as e:
        obj_lib.save_screenshot(browser)
        print(e)
        raise

    finally:
    # Close the browser
        obj_lib.close_browser(browser)

#Nel, dont use time.sleep    
# use raise part in exception block as descied yesterday    