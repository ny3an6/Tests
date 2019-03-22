import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PythonOrgSearch(unittest.TestCase):

    def setUp(self): 
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver 
        driver.get("http://192.168.5.118/")
        assert "React App" in driver.title
        login = driver.find_element_by_name("login")
        login.send_keys("xxxx")
        password = driver.find_element_by_name("password")
        password.send_keys("xxxx")
        workplace = driver.find_element_by_name("phone")
        workplace.send_keys("xxxx")
        button = driver.find_element_by_class_name("ant-btn-primary")
        button.submit()

        wait = WebDriverWait(driver, 10)
        calling = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ant-table-wrapper")))
       # print(calling.text)
        svg = driver.find_element_by_tag_name("svg")
        action = ActionChains(driver)
        print(driver.find_elements_by_class_name("ant-spin-container")[1].text)
        # action.move_to_element(svg).click().perform()
        # driver.close()
if __name__ == "__main__":
    unittest.main()