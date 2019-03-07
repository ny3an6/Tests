import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.keys import Keys


class Pythonsearchforcallcenter(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_connect(self):
        driver = self.driver
        driver.get("http://192.168.5.119")
        login = driver.find_element_by_name("login")
        login.send_keys("5511")
        password = driver.find_element_by_name("password")
        password.send_keys("5511")
        button = driver.find_element_by_class_name("ant-btn-primary")
        button.submit()
        time.sleep(5)
        print("Status: ")
        status = driver.find_element_by_class_name("ant-table-row-level-0")
        action = ActionChains(driver)
        status.click()

   # #def test_history_calling(self):
   #     driver = self.driver
   #  #   driver.get("http://192.168.5.119/")
   #     status = driver.find_element_by_class_name("ant-table-row-level-0")
   #     status.submit()




if __name__ == "__main__":
    unittest.main()