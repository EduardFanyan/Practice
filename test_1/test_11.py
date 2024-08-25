import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.page_1 import RandomTest


def test_random():
    service = Service(executable_path=r'C:\Users\Edward\Desktop\driver\chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=service, options=options)

    test_1_random = RandomTest(driver)
    test_1_random.random_test_1()
    test_1_random.random_test_2()
    test_1_random.random_test_3()
