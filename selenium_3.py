import unittest
import os
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

    def setUp(self): 
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver 
        driver.get("http://192.168.5.118/")
        assert "React App" in driver.title
        login = driver.find_element_by_name("login")
        login.send_keys("roma")
        password = driver.find_element_by_name("password")
        password.send_keys("roma")
        workplace = driver.find_element_by_name("phone")
        workplace.send_keys("2212")
        button = driver.find_element_by_class_name("ant-btn-primary")
        button.submit()

        wait = WebDriverWait(driver, 10)
        inf_call = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ant-table-row-level-0")))     
        action = ActionChains(driver)
        action.move_to_element(inf_call).click().perform()
     
        try:
             wait_2 = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "p-font"))) 
             #wait_2 = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[contains(text(), 'YourTextHere')]")));     
        except:
            print("Error") 
        else:  
            asd = wait_2[-1].text.split()
            print(asd)
            os.environ["value_of_waiting_call"] = asd[-1]
            try: 
                if asd[-1] or asd[-3] or int(asd[-4]) or int(asd[-5]) <= 0:
                    os.environ["val"] = "Error, value of waiting time is equally 0 or below"
                    #print("Error, value of waiting time is equally 0 or below")
                else:
                    print()
            except:
                print("Error")
        finally:
            driver.close()
   # def tearDown(self):
   #     self.driver.close()

if __name__ == "__main__":
    unittest.main()
	
# https://habr.com/ru/post/250921/
