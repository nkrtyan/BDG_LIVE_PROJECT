from Lib import LIB
from POM.BDG_Home import Home

'''
1. Go to URL
2. Click to Blog
4. Check Blog page titile
5. Check Blog page  url
6. Check Blog info
7. Close browser
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
        obj_lib.wait_for_element(browser, obj_home.blog).click()
        assert  browser.title == obj_lib.get_data("blog_title")
        assert  browser.current_url == obj_lib.get_data( "blog_url")
        assert  obj_lib.get_data("blog_letter") in browser.page_source

    except Exception as exp:
        obj_lib.write_to_file(f"In case 6,  error reason is -{exp}")
        obj_lib.save_screenshot(browser, "Case_6")
        raise exp

    finally:
        # Close browser
        obj_lib.close_browser(browser)


