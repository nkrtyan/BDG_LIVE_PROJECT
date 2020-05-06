from POM.LP_Sign_In import Sign_in
from POM.LP_Home import Home
from Lib import LIB
import json

# Go to home page
# Click on sign in button
# Go to sign in page
# Fill in some input neeeded information and click on send button 

#test_1 sign_in page
def test_1():
    try:
        #Create drivere and open browser
        br = LIB()
        browser = br.open_browser()

        #load automationpractice.com page 
        br.page_load(browser)

        #Create Home object
        page_home = Home(browser)

        #Find some element and click
        browser.find_element(*page_home.sing_in).click()

        #Create Sign_in object
        page_sing_in = Sign_in(browser)

        #Get some data from config file
        with open('config.json') as f:
            data = json.load(f)
        email_add = data['eMail']
        password = data['password']  

        #Wait for element visible                  
        br.wait_for_element(browser, page_sing_in.email_address)

        #Fill in nessesary information
        browser.find_element(*page_sing_in.email_address).send_keys(email_add)
        browser.find_element(*page_sing_in.password).send_keys(password)

        #Click on send button
        browser.find_element(*page_sing_in.sign_in_btn).click()
        browser.find_element(*page_sing_in.my_account_title)
        print('Test is pass!')
        
    except Exception as e:
        print(e)
        br.save_screenshot(browser)
        print('Test is fail!')
    finally:
        br.close_browser(browser)

