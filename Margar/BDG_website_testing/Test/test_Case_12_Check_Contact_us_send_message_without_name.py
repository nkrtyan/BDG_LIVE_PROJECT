from Lib import LIB
from POM.Contact_Us import CONTACT_US
from POM.BDG_Home import Home

'''

1. Go to URL
2. Click to Contact us
3. Fill email field 
4. Fill phone number field
5. Fill messagge field
6. Click Send button
7. Close browser

'''

def test_1():
    try:
        #open browser
        obj_lib = LIB()
        browser = obj_lib.open_browser()

        #create  objects
        obj_cotact = CONTACT_US(browser)
        obj_home = Home(browser)

        #steps
        obj_lib.page_load(browser)
        obj_lib.wait_for_element(browser, obj_home.contact_us).click()
        obj_cotact.fill_without_email(browser)
        error = browser.find_element(*obj_cotact.fields_error)
        assert error.text == obj_lib.get_data("error_messagge")
        error_1 = browser.find_element(*obj_cotact.field_error_out)
        assert error_1.text == obj_lib.get_data("error_messagge_out")

    except Exception as exp:
        obj_lib.write_to_file(f"In case 12,  error reason is -{exp}")
        obj_lib.save_screenshot(browser, "Case_12")
        raise exp


    finally:
        #Close browser
        obj_lib.close_browser(browser)

