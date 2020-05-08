from Lib import Lib
from POM.Homepage import Homepage
from POM.Contact_us import Contact_us
import pytest
# import time

'''
1. Go to URL
2. Click to Dresses tab
3. Open file with 'log' name
4. Write there all found products name with their prices
5. Close browser
'''

def test_4():

    try:

# Open browser, maximazie window, get URL
        obj_lib = Lib()
        browser = obj_lib.open_browser()
        obj_lib.page_load(browser)

# Creating homepage & contact us page objects
        obj_homepage = Homepage(browser)

# Wait for dresses tab and click on it
        obj_lib.wait_for_element(browser, obj_homepage.dresses_menu_xpath)
        browser.find_element(*obj_homepage.dresses_menu_xpath).click()
        
# Get products result 
        prod_result = obj_homepage.get_product_name_price(browser)

# Open txt file write result
        obj_lib.write_to_file(prod_result)

        print("TEST_4: PASS")
    
    except Exception as error:
        obj_lib.save_screenshot(browser)
        pytest.fail(error)

# Close browser
    finally:
        obj_lib.close_browser(browser)
#Nel, correct        