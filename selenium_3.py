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
        driver.get("x")
        assert "React App" in driver.title
        login = driver.find_element_by_name("login").send_keys("x")
        password = driver.find_element_by_name("password").send_keys("x")
        workplace = driver.find_element_by_name("phone").send_keys("x")
        button = driver.find_element_by_class_name("ant-btn-primary").submit()
        driver = self.driver 
        action = ActionChains(driver)
        wait = WebDriverWait(driver, 10)

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
            print(len(asd)) 
            q = asd[-1]
            w = asd[-4]
            e = asd[-3]
            r = asd[-5]
            l = [q, w, e, r]
            p = ["NaN", "undefined", "0", "null"] 
            for x in l:
                if x == p[0] or x == p[1] or x == [2] or x == p[3]:
                    print("AGFJSHKDHAVHDF")
            if len(asd) != 17:
                print("Error: length of asd is below 17")
            else:
                print("Nice, all companents appeared and over 0")            
               
        finally:
            button_close = driver.find_element_by_class_name("ant-modal-close")
            button_close.click()
            svg = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "svg")))
            ActionChains(driver).move_to_element(svg).click().perform()
           # driver.close()
   # def tearDown(self):
   #     self.driver.close()

if __name__ == "__main__":
    unittest.main()
	
# https://habr.com/ru/post/250921/
# https://www.hostinger.ru/rukovodstva/osnovnie-git-komandy
# http://python-3.ru/page/selenium-python-example
