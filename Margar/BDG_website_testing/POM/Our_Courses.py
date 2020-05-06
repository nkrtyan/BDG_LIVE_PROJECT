from selenium.webdriver.common.by import By


class OUR_COURSES:

    #---locators---
    courses_parent_div = ('.//div[@class="eltdf-cl-inner eltdf-outer-space "]//article')


    # For check trainings data-name function
    name_atribute  = 'data-name'
    courses_count  = 35
    json_file_name = "dattaa.json"
    json_file_key  = "tr_names"


    # For check_trainings_href function
    href_atribut  = "href"
    json_key_name = "href_list"



    #---methods---
    def __init__(self, browser):
        self.browser = browser




    def check_trainings_data_name(self, browser):
        try:
            listt = [ ]
            for i in range(1, self.courses_count):
                app = browser.find_element(By.XPATH, self.courses_parent_div + f'[{i}]').get_attribute(self.name_atribute)
                listt.append(app)
            return listt
        except:
            print("Locating error")



    def check_trainings_href(self, browser):
        try:
            listt = [ ]
            for i in range(1, self.courses_count):
                app =  browser.find_element(By.XPATH, self.courses_parent_div + f'[{i}]//a').get_attribute(self.href_atribut)
                listt.append(app)
            return listt
        except:
            print("Locating error")


