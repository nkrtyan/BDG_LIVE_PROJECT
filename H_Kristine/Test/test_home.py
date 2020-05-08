from POM.LP_Home import Home
from Lib import LIB


# Go to home page
# Click on women button
# Get all infolrmation about price and product and write it some file   

def test_3():
    try:
        #Create drivere and open browser
        obj = LIB()
        browser = obj.open_browser()

        #load automationpractice.com page 
        obj.page_load(browser)

        #Create Home object
        obj_home = Home(browser)

        #Wait to some element visible on page
        obj.wait_for_element(browser, obj_home.menu_women)

        #Find intrerested element on menu and click it
        browser.find_element(*obj_home.menu_women).click()

        #Wait to product element visible on page
        obj.wait_for_elements(browser, obj_home.product_name)

        #Get some information about product name and product price
        product_name_ls = []
        product_price_ls = []
        product_name = browser.find_elements(*obj_home.product_name)
        for i in product_name:
            product_name_ls.append(i.text)
        product_price = browser.find_elements(*obj_home.product_price)
        for i in product_price:
            product_price_ls.append(i.text)
        my_dict = dict(zip(product_name_ls, product_price_ls))
        obj.write_to_file(my_dict)
        print("Test is pass!")

    except Exception as e:
        print(e)
        obj.save_screenshot(browser)        
        print("Test is fail!")
        raise
    finally:
        obj.close_browser(browser)

#Nel, good, part with product would be better to keep as function in POM, as you can use this in future        