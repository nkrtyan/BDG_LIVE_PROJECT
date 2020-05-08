from Lib import LIB
from POM.Our_Courses import OUR_COURSES
from POM.BDG_Home import Home

'''
1. Go to URL
2. Click to Our Courses
3. Click to Our Programming 
4. Checking current url
5. Checking current title
6. Close browser
'''

def test_1():
    try:


        #open browser
        obj_lib = LIB()
        browser = obj_lib.open_browser()

        # navigate to url
        obj_lib.page_load(browser)

        #create  objects
        obj_home = Home(browser)

        #steps
        obj_lib.wait_for_element(browser, obj_home.our_courses).click()
        obj_lib.wait_for_element(browser, obj_home.programming).click()
        assert browser.current_url == obj_lib.get_data("current_url_all_courses")
        assert browser.title == obj_lib.get_data("title_courses")


    except Exception as exp:
        obj_lib.write_to_file(f"In case 3,  error reason is -{exp}")
        obj_lib.save_screenshot(browser, "Case_3")
        raise exp




    finally:
        #Close browser
        obj_lib.close_browser(browser)




