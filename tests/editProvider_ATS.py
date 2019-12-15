import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class login_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/sanchitverma/PycharmProjects/a4venv/bin/chromedriver')

    def test_blog(self):
        user = "admin"
        pwd = "test12345"
        name = "Dr Alexis"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/clinic-supervisor")
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        time.sleep(2)
        elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[1]/li[3]/a').click()
        time.sleep(2)
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[2]/table/tbody/tr[1]/td[4]/a').click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_provider_name")
        elem.send_keys(name)
        elem = driver.find_element_by_xpath('/html/body/form/button').click()
        elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[1]/li[3]/a').click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
