
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_html_reporter import attach
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='session')
def base_url():
    return "http://192.168.6.103:7070/HCM"
@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome(service=Service("C:\\Users\\kumar ojja\\Desktop\\HCM_cls\\Drivers\\chromedriver_win32\\chromedriver.exe"))
    driver.maximize_window()
    # driver.implicitly_wait(5)
    yield driver
    driver.quit()
