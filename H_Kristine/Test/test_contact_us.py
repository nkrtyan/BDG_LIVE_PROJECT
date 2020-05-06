from POM.LP_Home import Home
from POM.LP_Contact_Us import Contact_Us
from Lib import LIB
from selenium.webdriver.support.ui import Select

# Go to home page
# Click on contact us button
# Go to contact us page
# Fill in some input neeeded information and click on send button   


#test_2 contact_us_page
def test_2():
    try:
        #Create driver
        obj = LIB()
        browser = obj.open_browser()

        #Get web page
        obj.page_load(browser)

        #Create Home page object  
        obj_home = Home(browser)

        #Find contact us element and click
        browser.find_element(*obj_home.contact_us).click()

        #Create Contact_us obj
        obj_contact_us = Contact_Us(browser)

        #Wait for visible nessasery element 
        obj.wait_for_element(browser, obj_contact_us.subject_heading)

        #Fill in nessesary formation in input fields 
        select = Select(browser.find_element(*obj_contact_us.subject_heading))
        select.select_by_visible_text(obj.get_data('subject_heading'))
        browser.find_element(*obj_contact_us.email).send_keys(obj.get_data('valid_email'))
        browser.find_element(*obj_contact_us.message).send_keys(obj.get_data('contact_us_input_message'))

        #Click send button 
        browser.find_element(*obj_contact_us.submit_message).click()

        #Compare get information and information in page 
        success_message = obj.get_data('contact_us_success_message')
        assert success_message in browser.page_source
        print('Test is pass!')

    except Exception as e:
        print(e)
        obj.save_screenshot(browser)
        print('Test is fail!')
        raise

    finally:
        obj.close_browser(browser)