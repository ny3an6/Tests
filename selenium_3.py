import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self): # зачем отдельно(1)
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver # (1)
        driver.get("http://192.168.5.119/")
       # self.assertIn("Python", driver.title)
        elem = driver.find_element_by_class_name("ant-table-row-level-0")
        elem.submit()
        assert "No results found." not in driver.page_source
       # elem.send_keys(Keys.RETURN)





   # def tearDown(self):
   #     self.driver.close()

if __name__ == "__main__":
    unittest.main()
	
# https://habr.com/ru/post/250921/