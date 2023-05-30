
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_html_reporter import attach
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='session')
def base_url():
    return "http://192.168.6.103:3030/HCM/"


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome(service=Service("C:\\Users\\kumar ojja\\Desktop\\HCM_cls\\Drivers\\chromedriver_win32\\chromedriver.exe"))
    driver.maximize_window()
    # driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def login(driver, base_url):
    driver.implicitly_wait(3)
    driver.get(f"{base_url}/")
    #driver.get("http://192.168.6.103:3030/HCM/")
    driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").click()
    driver.find_element(By.XPATH, "//input[@type=\'text\']").send_keys("Admin")
    driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").click()
    driver.find_element(By.XPATH, "//input[@type=\'password\']").send_keys("Newpass2@")
    driver.find_element(By.XPATH, "//input[@role=\'combobox\']").click()
    driver.find_element(By.XPATH, "//span[normalize-space()=\'VS001\']").click()
    driver.find_element(By.XPATH, "//button[@type=\'submit\']").click()



@pytest.mark.usefixtures("driver", "login")

class TestDefaultSuite():

    def test_AttendanceRegisterORLossofPayRegister(self, driver):
        
        driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Processing Engine']").click()
        driver.find_element(By.XPATH, "/html[1]/body[1]/app-root[1]/app-full-layout[1]/div[1]/div[1]/app-sidebar[1]/div[2]/div[1]/ul[1]/li[6]/ul[1]/li[1]/a[1]/span[1]").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()='User Access Management']"), "No Value "
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
        

    def test_Maker_Checker(self, driver):
        
        driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Processing Engine']").click()
        driver.find_element(By.XPATH, "//span[contains(text(),'Maker-Checker for Attendance Register/Loss of Pay ')]").click()
        elements = driver.find_elements(By.XPATH, "//body/app-root/app-full-layout[@class='ng-star-inserted']/div[@class='wrapper']/div[@class='main-panel']/div[@class='main-content']/div[@class='content-wrapper']/app-maker-checker-for-attendance-register-loss-of-pay-register[@class='ng-star-inserted']/div[1]/div[1]")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
        

    def test_Pre_Payroll_Process(self, driver):

        driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Processing Engine']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Pre-Payroll Process']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Pre-Payroll Process\']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
        

    def test_MasterPayScalePayrollProcessing(self, driver):

        driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Processing Engine']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Master Pay Scale Payroll Processing']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Master Pay Scale Payroll Processing\']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
        

    def test_FixedPayScalePayrollProcessing(self, driver):

        driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Processing Engine']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Fixed Pay Scale Payroll Processing']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Fixed Pay Scale Payroll Processing\']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
        

    def test_SupplementaryPayrollProcessing(self, driver):

        driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Processing Engine']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Supplementary Payroll Processing']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()='Supplementary Payroll Processing']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
        

    def test_MakerCheckerModelforPayrollProcessing(self, driver):

        driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Processing Engine']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Maker-Checker Model for Payroll Processing']").click()
        elements = driver.find_elements(By.XPATH, "//div[@class='card-header']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
        

    def test_CBSFileExtractGeneration(self, driver):

            driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Processing Engine']").click()
            driver.find_element(By.XPATH, "//span[normalize-space()='CBS File Extract Generation']").click()
            elements = driver.find_elements(By.XPATH, "//div[@class='card-header']")
            assert len(elements) > 0, " No case found"

            attach(data=driver.get_screenshot_as_png())
            

    def test_DownloadRecordsofPayrollProcessing(self, driver):

                driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Processing Engine']").click()
                actions = ActionChains(driver)
                actions.send_keys(Keys.PAGE_DOWN).perform()
                driver.find_element(By.XPATH, "//span[normalize-space()='Download Records of Payroll Processing']").click()
                elements = driver.find_elements(By.XPATH, "//div[@class='card-header']")
                assert len(elements) > 0
                attach(data=driver.get_screenshot_as_png())
                




