import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select

import test_data


@pytest.mark.usefixtures("setup_Chrome")
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

    def test_dropdown_admin(self):
        self.driver.find_element_by_xpath(".//a[@class='firstLevelMenu']").click()
        drop_down = Select(self.driver.find_element_by_id("searchSystemUser_userType"))
        drop_down.select_by_value("2")
        self.driver.find_element_by_xpath(".//input[@value='Search']").click()
        assert self.driver.find_element_by_xpath(".//*[text()='Aaliyah.Haq']")

    def test_input_text(self):
        self.driver.find_element_by_xpath(".//*[text()='Directory']").click()
        self.driver.find_element_by_xpath(".//input[@name='searchDirectory[emp_name][empName]']")\
            .send_keys(test_data.it_manager_name)
        self.driver.find_element_by_xpath(".//input[@name='_search']").click()
        assert self.driver.find_element_by_xpath(".//*[text()='Cassidy Hope']").is_displayed()

