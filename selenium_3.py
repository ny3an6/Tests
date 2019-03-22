import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# https://www.hostinger.ru/rukovodstva/osnovnie-git-komandy
# http://python-3.ru/page/selenium-python-example


chromedriver = "/home/ny3an6/Документы/chromedriver_linux64/chromedriver"

class PythonOrgSearch(unittest.TestCase):

    def setUp(self): 
        self.driver = webdriver.Chrome(chromedriver)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://192.168.5.119/")
        assert "React App" in driver.title
        login = driver.find_element_by_name("login")
        login.send_keys("5511")
        password = driver.find_element_by_name("password")
        password.send_keys("5511")
        button = driver.find_element_by_class_name("ant-btn-primary")
        button.submit()

        wait = WebDriverWait(driver, 10)
        inf_call = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ant-table-row-level-0")))     
        action = ActionChains(driver)
        action.move_to_element(inf_call).click().perform()
     
        try:
             wait_2 = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "p-font")))      
        except:
            print("Error") 
        else:
           # hold_time_all = wait.until(EC.presence_of_element_located((
           #     By.CLASS_NAME, "p-font")))
            asd = wait_2[-1].text.split()
            print(asd[-1])
            if int(asd[-1]) <= 0:
                print("Error, value of waiting time is equally 0 or below")
        finally:
            driver.close()
   # def tearDown(self):
   #     self.driver.close()

if __name__ == "__main__":
    unittest.main()
	
