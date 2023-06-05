from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_html_reporter import attach
from selenium.webdriver.chrome.service import Service




@pytest.fixture(scope='session')
def login(driver, base_url):
    driver.implicitly_wait(3)
    driver.get(f"{base_url}/")
    # driver.get("http://192.168.6.103:7070/HCM/")
    driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").click()
    driver.find_element(By.XPATH, "//input[@type=\'text\']").send_keys("Admin")
    driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").click()
    driver.find_element(By.XPATH, "//input[@type=\'password\']").send_keys("Newpass2@")
    driver.find_element(By.XPATH, "//input[@role=\'combobox\']").click()
    driver.find_element(By.XPATH, "//span[normalize-space()=\'VS001\']").click()
    driver.find_element(By.XPATH, "//button[@type=\'submit\']").click()
    driver.find_element(By.XPATH, "//span[normalize-space()='EmployeePortal']").click()


@pytest.mark.usefixtures("driver", "login")
class TestDefaultSuite():

    def test_ActivateORDeactivateEmployeeCredentials(self, driver):
        # #driver.find_element(By.XPATH, "//span[normalize-space()='EmployeePortal']").click()
        driver.find_element(By.XPATH,
                            "//span[contains(text(),'Activate/Deactivate Employee Credentials for the Employee Portal – HR Facing')]").click()
        elements = driver.find_elements(By.XPATH,
                                        "//body/app-root/app-full-layout[@class='ng-star-inserted']/div[@class='wrapper']/div[@class='main-panel']/div[@class='main-content']/div[@class='content-wrapper']/app-activate-deactivate[@class='ng-star-inserted']/div[@class='col-lg-12 col-md-12 col-sm-12']/div[@class='card']/div[1]")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_LoginPage(self, driver):
        # #driver.find_element(By.XPATH, "//span[normalize-space()='EmployeePortal']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Login Page']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Login Page\']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_DashboardEmployeePortal(self, driver):
        # #driver.find_element(By.XPATH, "//span[normalize-space()='EmployeePortal']").click()
        driver.find_element(By.XPATH, "//span[contains(text(),'Dashboard – Employee Portal')]").click()
        elements = driver.find_elements(By.XPATH, "//div[@class='card-header']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_ServiceRegister(self, driver):
        # #driver.find_element(By.XPATH, "//span[normalize-space()='EmployeePortal']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Service Register']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Service Register\']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_LeavePosting(self, driver):
        # #driver.find_element(By.XPATH, "//span[normalize-space()='EmployeePortal']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Leave Posting (HR-Facing)']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()='Leaves Posting (HR-Facing)']"), "No_screen"
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    @pytest.mark.skip
    def test_LeavesManagement(self, driver):
        # #driver.find_element(By.XPATH, "//span[normalize-space()='EmployeePortal']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Leaves Management (Employee-Facing)']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()='Leaves Management']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_Leave_Applications_Reviewal(self, driver):
        # #driver.find_element(By.XPATH, "//span[normalize-space()='EmployeePortal']").click()

        # driver.execute_script(windows.ScrollBy(0,500))
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()

        driver.find_element(By.XPATH,
                            "//span[contains(text(),'Leave Applications Reviewal (HR-Facing/Reporting M')]").click()
        elements = driver.find_elements(By.XPATH, "//div[@class='card-header']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_PaySlipEmployeeFacing(self, driver):
        # #driver.find_element(By.XPATH, "//span[normalize-space()='EmployeePortal']").click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH, "//span[normalize-space()='Pay Slip (Employee-Facing)']").click()
        elements = driver.find_elements(By.XPATH, "//div[@class='card-header']")
        assert len(elements) > 0

        attach(data=driver.get_screenshot_as_png())

    def test_UploadEmployeeDocuments(self, driver):
        # #driver.find_element(By.XPATH, "//span[normalize-space()='EmployeePortal']").click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH, "//span[normalize-space()='Upload Employee Documents (HR-Facing)']").click()
        elements = driver.find_elements(By.XPATH, "//span[normalize-space()='Upload Employee Documents (HR-Facing)']")
        assert len(elements) > 0

        attach(data=driver.get_screenshot_as_png())

    def test_AccessEmployee(self, driver):
        ##driver.find_element(By.XPATH, "//span[normalize-space()='EmployeePortal']").click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH, "//span[normalize-space()='Access Employee Documents (Employee Facing)']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()='Download Employee Document']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_IncomeTaxDeclaration(self, driver):
        ##driver.find_element(By.XPATH, "//span[normalize-space()='EmployeePortal']").click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH, "//span[normalize-space()='Income Tax Declarations (Employee Facing)']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()='Income Tax Declaration']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_ReviewIncomeTaxDeclarations(self, driver):
        ##driver.find_element(By.XPATH, "//span[normalize-space()='EmployeePortal']").click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH, "//div[normalize-space()='Income Tax Declaration']").click()
        elements = driver.find_elements(By.XPATH, "//div[@class='card-header']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_ApplyforAdvances(self, driver):
        ##driver.find_element(By.XPATH, "//span[normalize-space()='EmployeePortal']").click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH,
                            "//span[normalize-space()='Apply for Advances & Loans (Employee-Facing)']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()='Apply for Advances & Loans']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_ReviewEmployeeAdvanceLoan(self, driver):
        ##driver.find_element(By.XPATH, "//span[normalize-space()='EmployeePortal']").click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH,
                            "//span[contains(text(),'Review Employee Advance & Loan Applications (HR-Facing)]").click(), "Error"
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Staff Benefits Operational Screen\']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_EnterAdvancesforEmployees(self, driver):
        ##driver.find_element(By.XPATH, "//span[normalize-space()='EmployeePortal']").click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH, "//span[normalize-space()='Enter Advances for Employees (HR-Facing)']").click()
        elements = driver.find_elements(By.XPATH,
                                        "//form[@class='ng-untouched ng-pristine ng-valid']//div[@class='card-header'][normalize-space()='Advances (HR-Facing)']"), "No Screen"
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_ViewAdvances(self, driver):
        #driver.find_element(By.XPATH, "//span[normalize-space()='EmployeePortal']").click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH, "//span[normalize-space()='View Advances (Employee-Facing)']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()='Advances (Employee-Facing)']"), " No Screen"
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_ViewDeductionDetails(self, driver):
        #driver.find_element(By.XPATH, "//span[normalize-space()='EmployeePortal']").click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH, "//span[normalize-space()='View Deduction Details (Employee-Facing)']").click()
        elements = driver.find_elements(By.XPATH, "//div[@class='card-header']"), "No Screen"
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_Reimbursements(self, driver):
        #driver.find_element(By.XPATH, "//span[normalize-space()='EmployeePortal']").click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH, "//span[normalize-space()='Reimbursements Management (Employee-Facing)']").click()
        elements = driver.find_elements(By.XPATH,
                                        "//body/app-root/app-full-layout[@class='ng-star-inserted']/div[@class='wrapper']/div[@class='main-panel']/div[@class='main-content']/div[@class='content-wrapper']/app-reimbursements-management[@class='ng-star-inserted']/form[@class='ng-untouched ng-pristine ng-invalid']/div[1]/div[1]")
        assert len(elements) > 0

        attach(data=driver.get_screenshot_as_png())

    def test_ReviewReimbursement(self, driver):
        #driver.find_element(By.XPATH, "//span[normalize-space()='EmployeePortal']").click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH,
                            "//span[normalize-space()='Review Reimbursement Applications (HR-Facing)']").click()
        elements = driver.find_elements(By.XPATH,
                                        "//body/app-root/app-full-layout[@class='ng-star-inserted']/div[@class='wrapper']/div[@class='main-panel']/div[@class='main-content']/div[@class='content-wrapper']/app-reporting-manager-review-of-reimbursement-application[@class='ng-star-inserted']/form[@class='ng-untouched ng-pristine ng-invalid']/div[1]/div[1]"), "No Screen"
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
