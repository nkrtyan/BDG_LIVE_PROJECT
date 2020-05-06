from Lib import Lib
from POM.Home_page import Home_Page
import time
import pytest

# Go to url
# Click to Wommen tab
# Open file with "log" name
# Write where all found products name and their prices

def test_4():
    try:
        obj_lib=Lib()
        #open browser
        browser=obj_lib.open_browser()
        #load page
        obj_lib.page_load(browser)
        obj_home=Home_Page(browser)
        #wait and find element Women and click
        browser.find_element(*obj_home.li_women).click()
        obj_lib.wait_for_elements(browser,obj_home.pict_names)
        #find products 
        products_names=browser.find_elements(*obj_home.pict_names)
        #find prices
        products_price=browser.find_elements(*obj_home.price)
        # get products names and prices
        p_name=[]
        p_price=[]
        for i in products_names:
            p_name.append(i.text)
        
        for j in products_price:
            p_price.append(j.text)
            list_of_price=p_price[1::2]
        # create dictionary for geting data and write to log file
        res = dict(zip(p_name, list_of_price)) 
        obj_lib.write_to_file(res)
    except Exception as e:
        pytest.fail(e)
        print("not write in file")
        obj_lib.save_screenshot(browser)
    finally:
        #close browsers
        obj_lib.close_browser(browser)



    
    
    obj_lib.close_browser(browser)
    #obj_lib.move_to_elements(browser,elements)




