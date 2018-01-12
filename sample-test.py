import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class SampleTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/home/tharu/Downloads/chromedriver')

    def test_PypiSite(self):
        self.driver.get("https://pypi.python.org/pypi")
        self.driver.find_element(By.ID, "term").send_keys("selenium")
        self.driver.find_element(By.ID, "submit").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()