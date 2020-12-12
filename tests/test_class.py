from telnetlib import EC

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import test_data


@pytest.mark.usefixtures("setup")
class TestClass:
    def test_navigation(self):
        print(self.driver.title)
        assert "OrangeHRM" in self.driver.title

    def test_login(self):
        self.driver.find_element_by_xpath(".//input[@name='txtUsername']").send_keys(test_data.login)
        self.driver.find_element_by_xpath(".//input[@name='txtPassword']").send_keys(test_data.password)
        self.driver.find_element_by_xpath(".//input[@type='submit']").click()

        try:
            assert self.driver.find_element_by_xpath("//div[@class='head']/h1[text()='Dashboard']").is_displayed()
        except NoSuchElementException as error:
            print("Test failed", error)

        self.driver.find_element_by_xpath(".//a[@class='firstLevelMenu']").click()

    def test_back_and_forth(self):
        self.driver.back()
        self.driver.forward()
        self.driver.refresh()

        