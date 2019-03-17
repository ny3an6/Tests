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

    def test_Case_1(self):
        driver = self.driver 
        driver.get("http://192.168.5.118/")
        assert "React App" in driver.title
        login = driver.find_element_by_name("login").send_keys("xxxx")
        password = driver.find_element_by_name("password").send_keys("xxxx")
        workplace = driver.find_element_by_name("phone")
        workplace.send_keys("xxxx")
        button = driver.find_element_by_class_name("ant-btn-primary").submit()
        
        action = ActionChains(driver)
        wait = WebDriverWait(driver, 10)
         #
         #  svg = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "svg")))
#  проверка логина         #  #ActionChains(driver).move_to_element(svg).click().perform()
         #  if svg:
         #      print("Success")
         #  else:
         #      print("Error")

        history = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "anticon-bars")))
        action.move_to_element(history).click().perform()
        date_1 = wait.until(EC.visibility_of_element_located((By.ID, "dateFrom")))
        action.move_to_element(date_1).click().send_keys("12").perform()
       # date_2 = wait.until(EC.visibility_of_element_located((By.ID, "dateTo")))
      #  date_2.send_keys("12032019")
if __name__ == "__main__":
    unittest.main()
        