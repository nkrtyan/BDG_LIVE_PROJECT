from Lib import LIB
from POM.About_Us import ABOUT_US
from POM.BDG_Home import Home

'''

1. Go to URL
2. Click to About us
3. Check info about BDG
4. Close browser

'''

def test_1():
    try:
        #open browser
        obj_lib = LIB()
        browser = obj_lib.open_browser()

        #create  objects
        obj_about = ABOUT_US(browser)
        obj_home = Home(browser)

        #steps
        obj_lib.page_load(browser)
        obj_lib.wait_for_element(browser, obj_home.about_us).click()
        assert obj_about.return_text(browser, obj_about.founders_title) == obj_lib.get_data("founders_title")
        assert obj_about.return_text(browser, obj_about.founder_1) == obj_lib.get_data("founder_1")
        assert obj_about.return_text(browser, obj_about.founder_2) == obj_lib.get_data("founder_2")


    except Exception as exp:
        obj_lib.write_to_file(f"In case 8,  error reason is -{exp}")
        obj_lib.save_screenshot(browser, "Case_8")
        raise exp


    finally:
        #Close browser
        obj_lib.close_browser(browser)

