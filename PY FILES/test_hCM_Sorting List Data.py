# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestHCM():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login(self):
    self.driver.get("http://192.168.6.103:7070/HCM/")
    self.driver.set_window_size(1366, 728)
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").click()
    self.driver.find_element(By.XPATH, "//input").send_keys("Admin")
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").send_keys("Newpass2@")
    self.driver.find_element(By.CSS_SELECTOR, ".ng-input > input").click()
    self.driver.find_element(By.XPATH, "//span[contains(.,\'VS001\')]").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
  
  def test_sortingListDatainGradeMaster(self):
    self.driver.get("http://192.168.6.103:7070/HCM/")
    self.driver.set_window_size(1366, 728)
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").click()
    self.driver.find_element(By.XPATH, "//input").send_keys("Admin")
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").send_keys("Newpass2@")
    self.driver.find_element(By.CSS_SELECTOR, ".ng-input > input").click()
    self.driver.find_element(By.XPATH, "//span[contains(.,\'VS001\')]").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.XPATH, "//span[contains(.,\'Personal Information Systems\')]").click()
    self.driver.find_element(By.XPATH, "//span[contains(.,\'Grade Master\')]").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_desc").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
    self.driver.close()
  
  def test_sortingListDatainDesignationMaster(self):
    self.driver.get("http://192.168.6.103:7070/HCM/")
    self.driver.set_window_size(1366, 728)
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").click()
    self.driver.find_element(By.XPATH, "//input").send_keys("Admin")
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").send_keys("Newpass2@")
    self.driver.find_element(By.CSS_SELECTOR, ".ng-input > input").click()
    self.driver.find_element(By.XPATH, "//span[contains(.,\'VS001\')]").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.XPATH, "//span[contains(.,\'Personal Information Systems\')]").click()
    self.driver.find_element(By.LINK_TEXT, "Designation Master").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_desc").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting:nth-child(4)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
  
  def test_sortingListDatainTeamMaster(self):
    self.driver.get("http://192.168.6.103:7070/HCM/")
    self.driver.set_window_size(1366, 728)
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").click()
    self.driver.find_element(By.XPATH, "//input").send_keys("Admin")
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").send_keys("Newpass2@")
    self.driver.find_element(By.CSS_SELECTOR, ".ng-input > input").click()
    self.driver.find_element(By.XPATH, "//span[contains(.,\'VS001\')]").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.XPATH, "//span[contains(.,\'Personal Information Systems\')]").click()
    self.driver.find_element(By.XPATH, "//span[contains(.,\'Team Master\')]").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_desc").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
  
  def test_sortingListDatainLeaveTypeMaster(self):
    self.driver.get("http://192.168.6.103:7070/HCM/")
    self.driver.set_window_size(1366, 728)
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").click()
    self.driver.find_element(By.XPATH, "//input").send_keys("Admin")
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").send_keys("Newpass2@")
    self.driver.find_element(By.CSS_SELECTOR, ".ng-input > input").click()
    self.driver.find_element(By.XPATH, "//span[contains(.,\'VS001\')]").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.XPATH, "//a[contains(.,\'Personal Information Systems\')]").click()
    self.driver.find_element(By.XPATH, "//span[contains(.,\'Leave Type Master\')]").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_desc").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting:nth-child(4)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting:nth-child(5)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting:nth-child(6)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting:nth-child(7)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
  
  def test_sortingListDatainLeaveRules(self):
    self.driver.get("http://192.168.6.103:7070/HCM/")
    self.driver.set_window_size(1366, 728)
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").click()
    self.driver.find_element(By.XPATH, "//input").send_keys("Admin")
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").send_keys("Newpass2@")
    self.driver.find_element(By.CSS_SELECTOR, ".ng-input > input").click()
    self.driver.find_element(By.XPATH, "//span[contains(.,\'VS001\')]").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.XPATH, "//span[contains(.,\'Personal Information Systems\')]").click()
    self.driver.find_element(By.LINK_TEXT, "Leave Rules").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting:nth-child(4)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting:nth-child(5)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting:nth-child(6)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
  
