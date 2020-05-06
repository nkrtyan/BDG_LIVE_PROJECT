from Lib import LIB
from POM.BDG_Home import Home
from  POM.Our_Trainers import OUR_TRAINERS
import time
'''
1. Go to URL
2. Click to Our Trainers
3. Click to trainer Nelli's name
4. Check Nelli's page titile
5. Check Nelli's page  url
6. Check Nelli's info
7. Close browser
'''

def test_1():
    try:

        #open browser
        obj_lib = LIB()
        browser = obj_lib.open_browser()

        #create  objects
        obj_train = OUR_TRAINERS(browser)
        obj_home = Home(browser)

        #steps
        obj_lib.page_load(browser)
        obj_lib.wait_for_element(browser, obj_home.our_trainers).click()
        time.sleep(10) # Here I have a problem with my internet, for it here i use time sleep
        obj_lib.wait_for_element(browser, obj_train.trainer_Nelli).click()
        assert  browser.title == obj_lib.get_data("Nelli's_page_titile")
        assert  browser.current_url == obj_lib.get_data( "Nelli's_page_url")
        assert  obj_lib.get_data("Nelli's_page_info_1") in browser.page_source
        assert  obj_lib.get_data("Nelli's_page_info_2") in browser.page_source
        assert  obj_lib.get_data("Nelli's_page_info_3") in browser.page_source
        assert  obj_lib.get_data("Nelli's_page_info_4") in browser.page_source


    except Exception as exp:
        obj_lib.write_to_file(f"In case 4,  error reason is -{exp}")
        obj_lib.save_screenshot(browser, "Case_4")
        raise exp



    finally:
        # Close browser
        obj_lib.close_browser(browser)


