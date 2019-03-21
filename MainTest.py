import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PythonOrgSearch(unittest.TestCase):

    def setUp(self): 
        self.driver = webdriver.Chrome('/home/ny3an6/Загрузки/chromedriver_linux64/chromedriver')

    def test_Case_1(self):
        driver = self.driver 
        driver.get("http://192.168.5.118/")
        assert "React App" in driver.title
        login = driver.find_element_by_name("login").send_keys("roma")
        password = driver.find_element_by_name("password").send_keys("roma")
        workplace = driver.find_element_by_name("phone").send_keys("2214")
        button = driver.find_element_by_class_name("ant-btn-primary").submit()
        
        action = ActionChains(driver)
        wait = WebDriverWait(driver, 10)
         #
         #  svg = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "svg")))
         #  #ActionChains(driver).move_to_element(svg).click().perform()
         #  if svg:
         #      print("Success")
         #  else:
         #      print("Error")
        
        history = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "anticon-bars")))
        action.move_to_element(history).click().perform()
        
        date_1 = wait.until(EC.visibility_of_element_located((By.ID, "DateFrom"))).find_element_by_tag_name("input")
        print(date_1)
        action.move_to_element(date_1).click().send_keys("2019-03-03").perform()

        action.move_to_element(history).click().perform()
       
        
        date_2 = wait.until(EC.visibility_of_element_located((By.ID, "DateTo"))).find_element_by_tag_name("input")
        action.move_to_element(date_2).click().send_keys("2019-03-21").perform()
        
        action.move_to_element(history).click().perform()
        
        history_button = driver.find_element_by_class_name("ant-btn").click()

        table_vision = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ant-table-row-level-0")))
        if table_vision:
            print("Success")
        elif not table_vision:
            print("Error, no table elements")


        graphics = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "anticon-bar-chart")))
        action.move_to_element(graphics).click().perform()
        
        time.sleep(2)
        # date_3 = wait.until(EC.visibility_of_element_located((By.ID, "DateFrom"))).find_element_by_tag_name("input")
        date_3 = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@id='DateFrom']/div/input[1]")))
        print(date_3)

        action.move_to_element(date_3).click().send_keys("2019-03-21").perform()

        



        time.sleep(10)
       
if __name__ == "__main__":
    unittest.main()