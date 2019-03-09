import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# https://www.hostinger.ru/rukovodstva/osnovnie-git-komandy
# http://python-3.ru/page/selenium-python-example
class PythonOrgSearch(unittest.TestCase):

    def setUp(self): # зачем отдельно(1)
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver # (1)
        driver.get("http://192.168.5.119/")
        login = driver.find_element_by_name("login")
        login.send_keys("roma")
        password = driver.find_element_by_name("password")
        password.send_keys("roma")
        button = driver.find_element_by_class_name("ant-btn-primary")
        button.submit()
        time.sleep(4)      
        #status = driver.find_element_by_class_name("ant-table-row-level-0")      
        #action = ActionChains(driver)
        #action.move_to_element(status).click().perform()
        #time.sleep(3)
        #hold_time = driver.find_elements_by_class_name("ant-col-12")
        #for times in hold_time:
        #    print("<p>: " % times.get_attribute("p"))



   # def tearDown(self):
   #     self.driver.close()

if __name__ == "__main__":
    unittest.main()
	
# https://habr.com/ru/post/250921/
