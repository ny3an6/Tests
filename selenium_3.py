import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class PythonOrgSearch(unittest.TestCase):

    def setUp(self): # зачем отдельно(1)
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver # (1)
        driver.get("http://192.168.5.119/")
        login = driver.find_element_by_name("login")
        password = driver.find_element_by_name("password")
        login.send_keys("5511")
        password.send_keys("5511")
        button = driver.find_element_by_class_name("ant-btn-primary")
        button.submit()
        time.sleep(4)      
        status = driver.find_element_by_class_name("ant-table-row-level-0")      
        action = ActionChains(driver)
        action.move_to_element(status).click().perform()
        



   # def tearDown(self):
   #     self.driver.close()

if __name__ == "__main__":
    unittest.main()
	
# https://habr.com/ru/post/250921/
