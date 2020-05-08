from Lib import Lib
from POM.Home_page import Home_page
from pathlib import Path
import pytest

'''
1. Go to URL
2. Click to Woment tab
3. Open file with 'log' name
4. Write there all found products name with their prices
5. Close browser
'''

def test_4():
    try:
        #open browser
        obj_lib = Lib()
        browser = obj_lib.open_browser()

        # navigate to url
        obj_lib.page_load(browser)

        #Create Home object
        obj_home = Home_page(browser)

        #wait and click on women tab
        obj_lib.wait_for_element(browser, obj_home.women_tab)
        browser.find_element(*obj_home.women_tab).click()

        #Product result
        product_result = obj_home.give_product_name_price(browser)
    
        #open file and write product list there
        obj_lib.write_to_file(product_result)

        print('Test run passed successfully!')
        
    except Exception as e:
        pytest.fail(e)
        print("not write in file")
        obj_lib.save_screenshot(browser)

    
    finally:
        #Close browser
        obj_lib.close_browser(browser)

#---Nel, need to raise exception, you can use also pytest.fail(e), e is a exception       