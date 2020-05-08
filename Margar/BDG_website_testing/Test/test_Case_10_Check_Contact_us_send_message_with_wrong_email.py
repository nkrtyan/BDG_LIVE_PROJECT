from Lib import LIB
from POM.Contact_Us import CONTACT_US
from POM.BDG_Home import Home

'''

1. Go to URL
2. Click to Contact us
3. Fill name field 
4. Fill email field with wrong email
5. Fill phone number field
6. Fill messagge field
7. Click Send button
8. Close browser

'''

def test_1():
    try:
        #open browser
        obj_lib = LIB()
        browser = obj_lib.open_browser()

        #create  objects
        obj_contact = CONTACT_US(browser)
        obj_home = Home(browser)

        #steps
        obj_lib.page_load(browser)
        obj_lib.wait_for_element(browser, obj_home.contact_us).click()
        obj_contact.fill_wrong_email(browser)
        error = browser.find_element(*obj_contact.fields_error)
        assert error.text == obj_lib.get_data("error_messagge")



    except Exception as exp:
        obj_lib.write_to_file(f"In case 10,  error reason is -{exp}")
        obj_lib.save_screenshot(browser, "Case_10")
        raise exp


    finally:
        #Close browser
        obj_lib.close_browser(browser)

