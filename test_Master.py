
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_html_reporter import attach
from selenium.webdriver.chrome.service import Service





@pytest.fixture(scope='session')
def login(driver, base_url):
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get(f"{base_url}/")
    #driver.get("http://192.168.6.103:7070/HCM/")
    driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").click()
    driver.find_element(By.XPATH, "//input[@type=\'text\']").send_keys("Admin")
    driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").click()
    driver.find_element(By.XPATH, "//input[@type=\'password\']").send_keys("Newpass2@")
    driver.find_element(By.XPATH, "//input[@role=\'combobox\']").click()
    driver.find_element(By.XPATH, "//span[normalize-space()=\'VS001\']").click()
    driver.find_element(By.XPATH, "//button[@type=\'submit\']").click()
    driver.find_element(By.XPATH,"//body/app-root/app-full-layout[@class=\'ng-star-inserted\']/div[@class=\'wrapper\']/div[@class=\'app-sidebar main-menu menu-fixed menu-native-scroll expanded ng-star-inserted\']/app-sidebar[@class=\'ng-tns-c154-3 ng-star-inserted\']/div[@class=\'sidebar-content main-menu-content ng-tns-c154-3 ps\']/div[@class=\'nav-container ng-tns-c154-3\']/ul[@class=\'navigation ng-tns-c154-3\']/li[1]/a[1]").click()


@pytest.mark.usefixtures("driver", "login")
class TestDefaultSuite():

    def test_login(self,driver):

        elements = driver.find_elements(By.XPATH, "//h6[normalize-space()=\'VSOFT BANK\']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())


    def test_branchmaster(self,driver):

        driver.maximize_window()
        #driver.find_element(By.XPATH,"//body/app-root/app-full-layout[@class=\'ng-star-inserted\']/div[@class=\'wrapper\']/div[@class=\'app-sidebar main-menu menu-fixed menu-native-scroll expanded ng-star-inserted\']/app-sidebar[@class=\'ng-tns-c154-3 ng-star-inserted\']/div[@class=\'sidebar-content main-menu-content ng-tns-c154-3 ps\']/div[@class=\'nav-container ng-tns-c154-3\']/ul[@class=\'navigation ng-tns-c154-3\']/li[1]/a[1]").click()
        driver.find_element(By.XPATH, "//span[normalize-space()=\'Branch Master\']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Branch Master\']")
        assert len(elements) > 0
        attach(data= driver.get_screenshot_as_png())


    def test_cadreemaster(self,driver):
       # self.login()
        driver.maximize_window()

        #driver.find_element(By.XPATH, "//body/app-root/app-full-layout[@class=\'ng-star-inserted\']/div[@class=\'wrapper\']/div[@class=\'app-sidebar main-menu menu-fixed menu-native-scroll expanded ng-star-inserted\']/app-sidebar[@class=\'ng-tns-c154-3 ng-star-inserted\']/div[@class=\'sidebar-content main-menu-content ng-tns-c154-3 ps\']/div[@class=\'nav-container ng-tns-c154-3\']/ul[@class=\'navigation ng-tns-c154-3\']/li[1]/a[1]").click()
        driver.find_element(By.XPATH, "//span[normalize-space()=\'Cadre Master\']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Cadre Master\']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())


    def test_calendermaster(self,driver):

        driver.maximize_window()

        #driver.find_element(By.XPATH,"/html[1]/body[1]/app-root[1]/app-full-layout[1]/div[1]/div[1]/app-sidebar[1]/div[2]/div[1]/ul[1]/li[1]/a[1]").click()
        driver.find_element(By.XPATH, "//span[normalize-space()=\'Calendar Master\']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Calendar Master\']")
        assert len(elements) > 0
        attach(data=driver.get_screenshot_as_png())


    def test_institutemaster(self,driver):

        driver.implicitly_wait(5)
        driver.maximize_window()
        #driver.find_element(By.XPATH,"//body/app-root/app-full-layout[@class=\'ng-star-inserted\']/div[@class=\'wrapper\']/div[@class=\'app-sidebar main-menu menu-fixed menu-native-scroll expanded ng-star-inserted\']/app-sidebar[@class=\'ng-tns-c154-3 ng-star-inserted\']/div[@class=\'sidebar-content main-menu-content ng-tns-c154-3 ps\']/div[@class=\'nav-container ng-tns-c154-3\']/ul[@class=\'navigation ng-tns-c154-3\']/li[1]/a[1]").click()
        driver.find_element(By.XPATH, "//span[normalize-space()=\'Institution Master\']").click()
        elements = driver.find_elements(By.XPATH, "//div[normalize-space()=\'Institution Master List\']")
        assert len(elements) > 0
        attach(data= driver.get_screenshot_as_png())


    def test_usermanagement(self,driver):
        #self.login()
        driver.implicitly_wait(20)
        driver.maximize_window()
        #driver.find_element(By.XPATH, "//body/app-root/app-full-layout[@class=\'ng-star-inserted\']/div[@class=\'wrapper\']/div[@class=\'app-sidebar main-menu menu-fixed menu-native-scroll expanded ng-star-inserted\']/app-sidebar[@class=\'ng-tns-c154-3 ng-star-inserted\']/div[@class=\'sidebar-content main-menu-content ng-tns-c154-3 ps\']/div[@class=\'nav-container ng-tns-c154-3\']/ul[@class=\'navigation ng-tns-c154-3\']/li[1]/a[1]").click()
        driver.find_element(By.XPATH, "//span[normalize-space()=\'User Management\']").click()
        attach(data= driver.get_screenshot_as_png())

