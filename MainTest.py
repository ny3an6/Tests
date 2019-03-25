import unittest
import time
import os
import logging
from logging import log
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(
    filename="logi.log", 
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s")
    

class PythonOrgSearch(unittest.TestCase):

    def setUp(self): 
        self.driver = webdriver.Chrome('/home/ny3an6/chromedriver_linux64/chromedriver')

    def test_Case_1(self):
        driver = self.driver 
        driver.get("x")
        assert "React App" in driver.title
        login = driver.find_element_by_name("login").send_keys("x")
        password = driver.find_element_by_name("password").send_keys("x")
        workplace = driver.find_element_by_name("phone").send_keys("x")
        button = driver.find_element_by_class_name("ant-btn-primary").submit()
        driver = self.driver 
        action = ActionChains(driver)
        wait = WebDriverWait(driver, 10)
    
    
        
        history = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "anticon-bars")))
        action.move_to_element(history).click().perform()
        
        date_1 = wait.until(EC.visibility_of_element_located((By.ID, "DateFrom"))).find_element_by_tag_name("input")
        action.move_to_element(date_1).click().send_keys("2019-03-03").perform()

        action.move_to_element(history).click().perform()
        
        date_2 = wait.until(EC.visibility_of_element_located((By.ID, "DateTo"))).find_element_by_tag_name("input")
        action.move_to_element(date_2).click().send_keys("2019-03-21").perform()
        
        action.move_to_element(history).click().perform()
        
        history_button = driver.find_element_by_class_name("ant-btn").click()

        table_vision = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ant-table-row-level-0")))
        if table_vision:
            logging.debug("Success, history of calling is visible")
        elif not table_vision:
            logging.debug("Error, history of calling is invisible")

        driver.close()
        
    def test_Case_2(self):
        driver = self.driver 
        driver.get("x")
        assert "React App" in driver.title
        login = driver.find_element_by_name("login").send_keys("x")
        password = driver.find_element_by_name("password").send_keys("x")
        workplace = driver.find_element_by_name("phone").send_keys("x")
        button = driver.find_element_by_class_name("ant-btn-primary").submit()
        driver = self.driver 
        action = ActionChains(driver)
        wait = WebDriverWait(driver, 10)


        graphics = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "anticon-bar-chart")))
        action.move_to_element(graphics).click().perform()
        
        
        date_3 = wait.until(EC.visibility_of_element_located((By.ID, "DateFrom"))).find_element_by_tag_name("input")
        #date_3 = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@id='DateFrom']/div/input[1]")))
        action.move_to_element(date_3).click().send_keys("2019-03-03").perform()
        
        action.move_to_element(graphics).click().perform()

        date_4 = wait.until(EC.visibility_of_element_located((By.ID, "DateTo"))).find_element_by_tag_name("input")
        action.move_to_element(date_4).click().send_keys("2019-03-21").perform()

        action.move_to_element(graphics).click().perform()

        graphics_button = driver.find_element_by_class_name("ant-btn")
        action.move_to_element(graphics_button).click().perform()

        #first_data_graphic = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@id='DateFrom']/div/input[1]")))
        first_data_graphic = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "recharts-cartesian-axis-tick")))
        if first_data_graphic:
            logging.debug("Success, graphics is visible")
        elif not first_data_graphic:
            logging.debug("Error, graphics is invisible")
        

        
       
if __name__ == "__main__":
    unittest.main()