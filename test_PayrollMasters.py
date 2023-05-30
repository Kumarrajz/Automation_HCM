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

    def test_PayScaleMaster(self, driver):
        driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Masters']").click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH, "//span[normalize-space()='Pay Scale Master']").click()
        elements = driver.find_elements(By.XPATH, "//div[@class='card-header']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_Allowances_Master(self, driver):
        driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Masters']").click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH, "//span[normalize-space()='Allowances Master']").click()
        elements = driver.find_elements(By.XPATH,
                                        "//body/app-root/app-full-layout[@class='ng-star-inserted']/div[@class='wrapper']/div[@class='main-panel']/div[@class='main-content']/div[@class='content-wrapper']/app-allowances-master[@class='ng-star-inserted']/form[@class='ng-untouched ng-pristine ng-invalid']/div[1]/div[1]/div[1]")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_AllowancesManagement(self, driver):
        driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Masters']").click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH, "//span[normalize-space()='Allowances Management']").click()
        elements = driver.find_elements(By.XPATH, "//div[@class='card-header']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_ProvidentFundORGovernmentProvidentFundNomination(self, driver):
        driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Masters']").click()
        # actions = ActionChains(driver)
        # actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH,
                            "//span[contains(text(),'Provident Fund/Government Provident Fund Nomination')]").click()
        # elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Provident Fund/Government Provident Fund Nomination\']")
        # assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_EmployeesStateInsuranceNomination(self, driver):
        driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Masters']").click()
        # actions = ActionChains(driver)
        # actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH,
                            "//span[normalize-space()='Employees State Insurance Nomination']").click(), "404 Error no page"
        # elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Employees State Insurance Nomination\']")
        # assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_GratuityNominationForm(self, driver):
        driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Masters']").click()
        # actions = ActionChains(driver)
        # actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH, "//span[normalize-space()='Gratuity Nomination Form']").click()
        elements = driver.find_elements(By.XPATH, "//div[@class='card-header']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_DeductionsMaster(self, driver):
        driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Masters']").click()
        # actions = ActionChains(driver)
        # actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH, "//span[normalize-space()='Deductions Master']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()='Deductions Master']")
        assert len(elements) > 0

        attach(data=driver.get_screenshot_as_png())

    def test_Deductions_Management(self, driver):
        driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Masters']").click()
        # actions = ActionChains(driver)
        # actions.send_keys(Keys.PAGE_UP).perform()
        # driver.find_element(By.XPATH, "//html[1]/body[1]/app-root[1]/app-full-layout[1]/div[1]/div[1]/app-sidebar[1]/div[2]/div[1]/ul[1]/li[4]/ul[1]/li[8]/a[1]/span[1]").click()
        # elements = driver.find_elements(By.XPATH, "//div[normalize-space()='Deductions Management']")
        # assert len(elements) > 0

        attach(data=driver.get_screenshot_as_png())

    def test_TaxDeductedatSourceMaster(self, driver):
        driver.find_element(By.XPATH,
                            "//span[normalize-space()='Payroll Masters']").click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH,
                            "//span[normalize-space()='Tax Deducted at Source Master']").click()
        elements = driver.find_elements(By.XPATH,
                                        "//div[normalize-space()=\'Tax Deducted at Source Master\']")
        assert len(elements) > 0, "No Case"
        attach(data=driver.get_screenshot_as_png())

    def test_Remuneration_Package_Template(self, driver):
        driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Masters']").click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH, "//span[normalize-space()='Remuneration Package Template']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Remuneration Package Template\']")
        assert len(elements) > 0, "No Case"
        attach(data=driver.get_screenshot_as_png())

    def test_RemunerationPackageOperationScreen(self, driver):
        driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Masters']").click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH, "//span[normalize-space()='Remuneration Package Operation Screen']").click()
        elements = driver.find_elements(By.XPATH,
                                        "//div[normalize-space()='Remuneration Package Operation Screen']"), "No click found"
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_StaffBenefitsMaster(self, driver):
        driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Masters']").click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH, "//span[normalize-space()='Staff Benefits Master']").click()
        elements = driver.find_elements(By.XPATH, "//div[@class='card-header']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_StaffBenefitsOperationalScreen(self, driver):
        driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Masters']").click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH, "//span[normalize-space()='Staff Benefits Operational Screen']").click()
        elements = driver.find_elements(By.XPATH,
                                        "//body/app-root/app-full-layout[@class='ng-star-inserted']/div[@class='wrapper']/div[@class='main-panel']/div[@class='main-content']/div[@class='content-wrapper']/app-staff-benefits-operational-screen[@class='ng-star-inserted']/div[1]/div[1]")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_CBSFileExtractTemplate(self, driver):
        driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Masters']").click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH, "//span[normalize-space()='CBS File Extract Template']").click()
        elements = driver.find_elements(By.XPATH, "//div[@class='card-header']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_PaySlipTemplate(self, driver):
        driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Masters']").click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH, "//span[normalize-space()='Pay Slip Template']").click()
        elements = driver.find_elements(By.XPATH, "//div[@class='card-header']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_AdvancesANDLoansMaster(self, driver):
        driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Masters']").click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH, "//span[normalize-space()='Advances & Loans Master']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()='Advances & Loans Master']"), "NO SCREEN"
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_Tax_Declarations_Master(self, driver):
        driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Masters']").click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH, "//span[normalize-space()='Tax Declarations Master (Employee Portal)']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()='Tax Declarations Master']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())

    def test_ReimbursementTemplateDefinition(self, driver):
        driver.find_element(By.XPATH, "//span[normalize-space()='Payroll Masters']").click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        driver.find_element(By.XPATH, "//span[normalize-space()='Reimbursement Template Definition']").click()
        elements = driver.find_elements(By.XPATH,
                                        "//body/app-root/app-full-layout[@class='ng-star-inserted']/div[@class='wrapper']/div[@class='main-panel']/div[@class='main-content']/div[@class='content-wrapper']/app-reimbursement-template-definition[@class='ng-star-inserted']/div[1]/div[1]")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
