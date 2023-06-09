import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_html_reporter import attach
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='session')
def login(driver, base_url):
    driver.implicitly_wait(3)
    driver.get(f"{base_url}/")
    #driver.get("http://192.168.6.103:7070/HCM/")
    driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").click()
    driver.find_element(By.XPATH, "//input[@type=\'text\']").send_keys("Admin")
    driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").click()
    driver.find_element(By.XPATH, "//input[@type=\'password\']").send_keys("Newpass2@")
    driver.find_element(By.XPATH, "//input[@role=\'combobox\']").click()
    driver.find_element(By.XPATH, "//span[normalize-space()=\'VS001\']").click()
    driver.find_element(By.XPATH, "//button[@type=\'submit\']").click()
    driver.find_element(By.XPATH, "//span[normalize-space()='Appraisal Masters']").click()



@pytest.mark.usefixtures("driver", "login")
class TestDefaultSuite():

    def test_AppraisalRatingClassification(self, driver):
        #driver.find_element(By.XPATH, "//span[normalize-space()='Appraisal Masters']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Appraisal Rating Classification']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Appraisal Rating Classification\']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_DefiningtheAttributesfortheAppraisalsSystem(self, driver):
        #driver.find_element(By.XPATH, "//span[normalize-space()='Appraisal Masters']").click()
        driver.find_element(By.XPATH,
                            "//span[normalize-space()='Defining the Attributes for the Appraisals System']").click()
        elements = driver.find_elements(By.XPATH,
                                        "//body/app-root/app-full-layout[@class='ng-star-inserted']/div[@class='wrapper']/div[@class='main-panel']/div[@class='main-content']/div[@class='content-wrapper']/app-defining-the-attributes-for-the-appraisals-system[@class='ng-star-inserted']/div[1]/div[1]")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_RulesANDExceptionsforAppraisalOperations(self, driver):
        #driver.find_element(By.XPATH, "//span[normalize-space()='Appraisal Masters']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Rules & Exceptions for Appraisal Operations']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()='Appraisals Rules & Exceptions']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_AssignAcceptingAuthorityPrivilegestoEmployees(self, driver):
        #driver.find_element(By.XPATH, "//span[normalize-space()='Appraisal Masters']").click()
        driver.find_element(By.XPATH,
                            "//span[normalize-space()='Assign Accepting Authority Privileges to Employees']").click()
        elements = driver.find_elements(By.XPATH,
                                        "//div[normalize-space()=\'Assign Accepting Authority Privileges to Employees\']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_Self_Appraisal(self, driver):
        #driver.find_element(By.XPATH, "//span[normalize-space()='Appraisal Masters']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Self-Appraisal (Employee-Facing)']").click()
        elements = driver.find_elements(By.XPATH, "//div[@class='card-header']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_ConductAppraisals(self, driver):
        #driver.find_element(By.XPATH, "//span[normalize-space()='Appraisal Masters']").click()
        driver.find_element(By.XPATH,
                            "//span[contains(text(),'Conduct Appraisals [Operational Screen in Employee')]").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()='Conduct Appraisal']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_ViewAppraisalStage(self, driver):
        #driver.find_element(By.XPATH, "//span[normalize-space()='Appraisal Masters']").click()
        driver.find_element(By.XPATH,
                            "//span[normalize-space()='View Appraisal Stage [Operational Screen]']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()='Conduct Appraisal']"), "No Screen"
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_AppraisalsDashboard(self, driver):
        #driver.find_element(By.XPATH, "//span[normalize-space()='Appraisal Masters']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Appraisals Dashboard (HR-Facing)']").click()
        elements = driver.find_elements(By.XPATH, "//div[@class='card-header']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
