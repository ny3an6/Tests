import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
<<<<<<< HEAD
# https://www.hostinger.ru/rukovodstva/osnovnie-git-komandy
# http://python-3.ru/page/selenium-python-example


chromedriver = "/home/ny3an6/Документы/chromedriver_linux64/chromedriver"
=======
>>>>>>> 2d2223db72563c8c42da683e6a2367443aef5c95

class PythonOrgSearch(unittest.TestCase):

    def setUp(self): 
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver 
        driver.get("http://192.168.5.118/")
        assert "React App" in driver.title
        login = driver.find_element_by_name("login")
        login.send_keys("5511")
        password = driver.find_element_by_name("password")
<<<<<<< HEAD
        password.send_keys("5511")
=======
<<<<<<< HEAD
        password.send_keys("roma")
        workplace = driver.find_element_by_name("phone")
        workplace.send_keys("2212")
=======
        password.send_keys("xxxx")
        workplace = driver.find_element_by_name("phone")
        workplace.send_keys("xxxx")
>>>>>>> ba90a4de648525c3c3744568ef3d7221ea184590
>>>>>>> 2d2223db72563c8c42da683e6a2367443aef5c95
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
<<<<<<< HEAD
            os.environ["value_of_waiting_call"] = asd[-1]
            try: 
                if asd[-1] or asd[-3] or int(asd[-4]) or int(asd[-5]) <= 0:
                    os.environ["val"] = "Error, value of waiting time is equally 0 or below"
                    #print("Error, value of waiting time is equally 0 or below")
                else:
                    print()
            except:
                print("Error")
=======
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
               
>>>>>>> ba90a4de648525c3c3744568ef3d7221ea184590
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
	
<<<<<<< HEAD
=======
# https://habr.com/ru/post/250921/
# https://www.hostinger.ru/rukovodstva/osnovnie-git-komandy
# http://python-3.ru/page/selenium-python-example
>>>>>>> 2d2223db72563c8c42da683e6a2367443aef5c95
