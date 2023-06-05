import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_html_reporter import attach
from selenium.webdriver.chrome.service import Service





@pytest.fixture(scope='session')
def login(driver, base_url):
    driver.implicitly_wait(5)
    driver.get(f"{base_url}/")
    #driver.get("http://192.168.6.103:7070/HCM/")
    driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").click()
    driver.find_element(By.XPATH, "//input[@type=\'text\']").send_keys("Admin")
    driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").click()
    driver.find_element(By.XPATH, "//input[@type=\'password\']").send_keys("Newpass2@")
    driver.find_element(By.XPATH, "//input[@role=\'combobox\']").click()
    driver.find_element(By.XPATH, "//span[normalize-space()=\'VS001\']").click()
    driver.find_element(By.XPATH, "//button[@type=\'submit\']").click()
    driver.find_element(By.XPATH, "//span[normalize-space()='Reports']").click()

@pytest.mark.usefixtures("driver", "login")
class TestDefaultSuite():
    def test_PaySlipGeneration(self, driver):

        #driver.find_element(By.XPATH, "//span[normalize-space()='Reports']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Pay Slip Generation']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()='Pay Slip Generation']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
        

    def test_Remittances(self, driver):

        #driver.find_element(By.XPATH, "//span[normalize-space()='Reports']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Remittances']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()='Remittances']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
        


    def test_GeneralReports(self, driver):

        #driver.find_element(By.XPATH, "//span[normalize-space()='Reports']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='General Reports']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'General Reports\']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
        


