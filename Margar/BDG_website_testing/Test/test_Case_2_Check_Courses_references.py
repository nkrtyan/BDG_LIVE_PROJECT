from Lib import LIB
from POM.Our_Courses import OUR_COURSES
from POM.BDG_Home import Home
from selenium import webdriver

'''
1. Go to URL
2. Click to Our Courses
3. Check courses references 
4. Close browser
'''
def test_1():
    try:
        #open browser
        obj_lib = LIB()
        browser = obj_lib.open_browser()

        # navigate to url
        obj_lib.page_load(browser)

        #create  objects
        obj_our = OUR_COURSES(browser)
        obj_home = Home(browser)

        #steps
        browser.find_element(*obj_home.our_courses).click()
        assert obj_our.check_trainings_href(browser)  == obj_lib.get_data("href_list")

    except Exception as exp:
        obj_lib.write_to_file(f"In case 2,  error reason is -{exp}")
        obj_lib.save_screenshot(browser, "Case_2")
        raise exp

    finally:
        #Close browser
        obj_lib.close_browser(browser)


