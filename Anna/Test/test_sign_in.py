from lib import Lib
from POM.Home_page import Home_page
from POM.Sign_in_page import Sign_in
import json

'''
Scenario steps
1. Go to URL
2. Click to Sign In in Home Page
3. Fill email address and password
4. Click Sign In button
5. Verify that you signed in successfully
'''

def test_1():
    try:
        # get email and pass from config
        with open('config.json') as f:
            data = json.load(f)
        email_address = data['eMail'] 
        password      = data['password']       

        #open browser,#navigate to url
        obj_lib = Lib()
        browser = obj_lib.open_browser()
        obj_lib.page_load(browser)

        #Create Home page objcet
        obj_home = Home_page(browser)

        #click on Sign in
        browser.find_element(*obj_home.sign_in).click()

        #Create Sign In object
        obj_signin = Sign_in(browser)

        #submit with email and pass
        obj_lib.wait_for_element(browser, obj_signin.email_address)
        browser.find_element(*obj_signin.email_address).send_keys(email_address)
        browser.find_element(*obj_signin.password).send_keys(password)

         #Check that you are in My accout page
        browser.find_element(*obj_signin.my_account_title)

        #click on Sign In button
        browser.find_element(*obj_signin.sign_in_btn).click()

        #Check that you are in My accout page
        browser.find_element(*obj_signin.my_account_title)

        print('Test run pass!')

    except Exception as e:
        print (e)
        obj_lib.save_screenshot(browser)
        print('Test run failed!')

    finally:
        #Close browser
        obj_lib.close_browser(browser)