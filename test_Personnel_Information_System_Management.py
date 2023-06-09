import pytest

from selenium.webdriver.common.by import By
from pytest_html_reporter import attach





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
    driver.find_element(By.XPATH,
                        "/html[1]/body[1]/app-root[1]/app-full-layout[1]/div[1]/div[1]/app-sidebar[1]/div[2]/div[1]/ul[1]/li[3]/a[1]/span[1]").click()


@pytest.mark.usefixtures("driver", "login")
class TestDefaultSuite():
   
    def test_ModifiedDetails (self, driver):

        #driver.find_element(By.XPATH, "//span[normalize-space()='Personnel Information System Management']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='ModifiedDetails']").click()
        elements = driver.find_elements(By.XPATH, "//h6[normalize-space()='New:Personal Details']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
        

    def test_Provisional_Employee_Draft (self, driver):

        #driver.find_element(By.XPATH, "//span[normalize-space()='Personnel Information System Management']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Provisional Employee Draft']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Provisional Employee Draft\']"),"Page not found"
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
        driver.close()
        

    def test_NewEmployeeDraft (self, driver):

        #driver.find_element(By.XPATH, "/html[1]/body[1]/app-root[1]/app-full-layout[1]/div[1]/div[1]/app-sidebar[1]/div[2]/div[1]/ul[1]/li[3]/a[1]/span[1]").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='New Employee Draft']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'New Employee Draft\']"),"Page not found"
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
        driver.close()
        

    def test_AcceptORReject_Provisional_Employee_Draft (self, driver):

        #driver.find_element(By.XPATH, "//span[normalize-space()='Personnel Information System Management']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Accept/Reject Provisional Employee Draft']").click()
        elements = driver.find_elements(By.XPATH, "//div[@class='card-header']"),"Page not found"

        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
        driver.close()
        

    def test_Modifying_Approved_Information (self, driver):

        #driver.find_element(By.XPATH, "//span[normalize-space()='Personnel Information System Management']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Modifying Approved Information']").click()
        elements = driver.find_elements(By.XPATH, "//form//div[@class='card-header mt-3'][normalize-space()='Update Approved Regular Employee Profiles']"),"Page not found"
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
        driver.close()
        

    def test_Updating_Approved_Information (self, driver):

        #driver.find_element(By.XPATH, "//span[normalize-space()='Personnel Information System Management']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Updating Approved Information']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Updating Approved Information\']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
        driver.close()
        

    def test_AcceptingORRejectingModifiedInformation_in_Approv (self, driver):

        #driver.find_element(By.XPATH, "//span[normalize-space()='Personnel Information System Management']").click()
        driver.find_element(By.XPATH, "//span[contains(text(),'Accepting/Rejecting Modified Information in Approv')]").click()
        elements = driver.find_elements(By.XPATH, "//div[@class='card-header']"),"error"
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
        driver.close()
        

    def test_AcceptORRejectUpdatedInformation_in_ApprovedProf (self, driver):

            #driver.find_element(By.XPATH, "//span[normalize-space()='Personnel Information System Management']").click()
            driver.find_element(By.XPATH, "//span[contains(text(),'Accept/Reject Updated Information in Approved Prof')]").click()
            elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Accept/Reject Updated Information in Approved Prof\']"),"No PAAGE"
            assert len(elements) > 0

            attach(data=driver.get_screenshot_as_png())

            driver.close()
            

    def test_EmployeeBasicPayEntry_FixedPayScale (self, driver):

                #driver.find_element(By.XPATH, "//span[normalize-space()='Personnel Information System Management']").click()
                driver.find_element(By.XPATH, "//span[normalize-space()='Employee Basic Pay Entry - Fixed Pay Scale']").click()
                elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Employee Basic Pay Entry - Fixed Pay Scale\']")
                assert len(elements) > 0

                attach(data=driver.get_screenshot_as_png())
                driver.close()
                

    def test_Maker_CheckerModelforBasicPayEntry (self, driver):

        driver.find_element(By.XPATH, "//span[normalize-space()='Personnel Information System Management']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Maker-Checker Model for Basic Pay Entry']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Maker-Checker Model for Basic Pay Entry\']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
        




