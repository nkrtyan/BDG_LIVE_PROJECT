from Lib import LIB
from POM.BDG_Home import Home

'''

1. Go to URL
2. Click to Contact us
3. Check  BDG address
3. Check  BDG phone number
3. Check  BDG @mail
4. Close browser

'''

def test_1():
    try:
        #open browser
        obj_lib = LIB()
        browser = obj_lib.open_browser()

        #create  objects
        obj_home = Home(browser)

        #steps
        obj_lib.page_load(browser)
        obj_lib.wait_for_element(browser, obj_home.contact_us).click()
        assert obj_lib.get_data("contact_us_address") in browser.page_source
        assert obj_lib.get_data("contact_us_phone") in browser.page_source
        assert obj_lib.get_data("contact_us_@mail") in browser.page_source


    except Exception as exp:
        obj_lib.write_to_file(f"In case 9,  error reason is -{exp}")
        obj_lib.save_screenshot(browser, "Case_9")
        raise exp


    finally:
        #Close browser
        obj_lib.close_browser(browser)

