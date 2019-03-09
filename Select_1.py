import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


# driver = webdriver.Chrome("/home/ny3an6/Документы/chromedriver_linux64/chromedriver")

class SearchForSelect(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    
    def test_selectform(self):
        driver = self.driver
        driver.get("http://blog.sedicomm.com/2018/04/06/ispolzovanie-komand-apt-v-linux-polnoe-rukovodstvo/")
        element = driver.find_element_by_xpath("//select[@id='cat']")
        all_options = element.find_element_by_tag_name("option")
        print(all_options.get_attribute("value"))
        for option in all_options:
            print("Options:" % option.get_attribute("value")) 
            option.click()





if __name__ == "__main__":
    unittest.main()


