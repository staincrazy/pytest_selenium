import pytest
from selenium import webdriver
import test_data


@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome("/Users/reonoldpetrenko/PycharmProjects/Selenium-Pytest-1/chromedriver")
    driver.get(test_data.url)
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.close()
