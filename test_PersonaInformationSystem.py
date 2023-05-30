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

    def test_GradeMaster(self, driver):
        
        driver.find_element(By.XPATH, "//span[normalize-space()='Personal Information Systems']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Grade Master']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Grade Master\']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
        

    def test_DesignationMaster(self, driver):

        driver.find_element(By.XPATH, "//span[normalize-space()='Personal Information Systems']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Designation Master']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Designation Master\']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
        

    def test_DepartmentMaster(self, driver):

        driver.find_element(By.XPATH, "//span[normalize-space()='Personal Information Systems']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Department Master']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Department Master\']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
        

    def test_DepartmentSectionMaster(self, driver):

        driver.find_element(By.XPATH, "//span[normalize-space()='Personal Information Systems']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Department Section Master']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Department Section Master\']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
        

    def test_EmployeeIdDefinition(self, driver):

        driver.find_element(By.XPATH, "//span[normalize-space()='Personal Information Systems']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Employee Id Definition']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Employee Id Definition\']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
        

    def test_Team_Master(self, driver):

        driver.find_element(By.XPATH, "//span[normalize-space()='Personal Information Systems']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Team Master']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Team Master\']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
        

    def test_Team_Master(self, driver):

        driver.find_element(By.XPATH, "//span[normalize-space()='Personal Information Systems']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Team Master']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Team Master\']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())
        

    def test_LeaveTypeMaster(self, driver):

            driver.find_element(By.XPATH, "//span[normalize-space()='Personal Information Systems']").click()
            driver.find_element(By.XPATH, "//span[normalize-space()='Leave Type Master']").click()
            elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Leave Type Master\']")
            assert len(elements) > 0

            attach(data=driver.get_screenshot_as_png())
            

    def test_LeaveRules(self, driver):

                driver.find_element(By.XPATH, "//span[normalize-space()='Personal Information Systems']").click()
                driver.find_element(By.XPATH, "//span[normalize-space()='Leave Rules']").click()
                elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Leave Rules\']")
                assert len(elements) > 0
                attach(data=driver.get_screenshot_as_png())
                




