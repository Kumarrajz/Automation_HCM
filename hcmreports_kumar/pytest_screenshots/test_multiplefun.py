import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='session')
def base_url():
    return "https://agile.vsoft.co.in:8443"


@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Chrome(service = Service("C:\\Users\\kumar ojja\\Desktop\\HCM_cls\\Drivers\\chromedriver_win32\\chromedriver.exe"))
    driver.set_window_size(1280, 672)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def login(driver, base_url):
    driver.get("https://agile.vsoft.co.in:8443/secure/Dashboard.jspa")
    driver.find_element(By.XPATH, "//a[@class='aui-nav-link login-link']").click()
    driver.find_element(By.ID, "login-form-username").send_keys("kumar ojja")
    driver.find_element(By.ID, "login-form-password").send_keys("Newpass@111")
    driver.find_element(By.ID, "login-form-submit").click()


@pytest.mark.usefixtures("login")
class TestJIRA:
    def test_jIRA(self, driver):
        driver.find_element(By.ID, "quickSearchInput").click()
        driver.find_element(By.ID, "quickSearchInput").send_keys("OWB-2686")
        driver.find_element(By.ID, "quickSearchInput").send_keys(Keys.ENTER)
        driver.find_element(By.ID, "header-details-user-fullname").click()

    def test_jira2(self, driver):
        driver.find_element(By.ID, "quickSearchInput").click()
        driver.find_element(By.ID, "quickSearchInput").send_keys("OWB-2686")
        driver.find_element(By.ID, "quickSearchInput").click()
        driver.find_element(By.ID, "quickSearchInput").send_keys("OWB-2687")
        driver.find_element(By.ID, "quickSearchInput").send_keys(Keys.ENTER)
        driver.find_element(By.ID, "header-details-user-fullname").click()
        driver.find_element(By.CSS_SELECTOR, ".ops-cont").click()