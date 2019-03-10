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
class PythonOrgSearch(unittest.TestCase):

    def setUp(self): # зачем отдельно(1)
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver # (1)
        driver.get("http://192.168.5.118/")
        login = driver.find_element_by_name("login")
        login.send_keys("roma")
        password = driver.find_element_by_name("password")
        password.send_keys("roma")
        button = driver.find_element_by_class_name("ant-btn-primary")
        button.submit()

        driver.wait = WebDriverWait(driver, 10)
        inf_call = driver.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ant-table-row-level-0")))     
        action = ActionChains(driver)
        action.move_to_element(inf_call).click().perform()

        try:
            hold_time_all = driver.wait.untill(EC.presence_of_element_located((
                By.CLASS_NAME, "p-font")))
            asd = hold_time_all.text.split()
            print(asd[-1])
        except:
            print("Error") 


   # def tearDown(self):
   #     self.driver.close()

if __name__ == "__main__":
    unittest.main()
	
# https://habr.com/ru/post/250921/
