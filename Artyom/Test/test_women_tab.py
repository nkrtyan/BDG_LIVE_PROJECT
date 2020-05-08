from lib import LIB
from POM.home import Home
from pathlib import Path

"""
1. Go to URL
2. Click to Woment tab
3. Open file with 'log' name
4. Write there all found products name with their prices
5. Close browser
"""

def test_4():

    try:
        # open browser
        obj_lib = LIB()
        browser = obj_lib.browser()

        # navigate to url
        obj_lib.page_load(browser)

        # wait for woman tab and click
        obj_home = Home()
        obj_lib.wait_for_element(browser, obj_home.women)
        browser.find_element(*obj_home.women).click()

        """ I didn't fully understand part of locating list of elements yet, so I decided 
        don't just copy your code, I will view the lesson one more time, 
        and maybe will add this part"""