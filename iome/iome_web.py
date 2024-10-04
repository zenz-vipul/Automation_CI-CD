import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

firefox_options=Options()
firefox_options.add_argument('--headless')

class Test_landing_page:
    def setup_method(self):
        self.driver = webdriver.Firefox(options=firefox_options)

    def teardown_method(self):
        self.driver.quit()

    def test_digital_you(self):
        self.driver.get("https://iome.ai")
        self.driver.find_element(By.XPATH, '//a[@href="/#the-digital-you"]').click()
        time.sleep(2)
        self.driver.back()

    def test_developer(self):
        self.driver.get("https://iome.ai")
        self.driver.find_element(By.XPATH, '//a[@href="https://dev.iome.ai"]').click()
        time.sleep(2)
        self.driver.back()

    def test_community(self):
        self.driver.get("https://iome.ai")
        self.driver.find_element(By.XPATH, '//a[@href="https://join.slack.com/t/iomeai/shared_invite/zt-20s1w9jxg-unzBomKqMBrrq~DlYNpQHQ"]').click()
        time.sleep(2)
        self.driver.back()

    def test_go_to_app(self):
        self.driver.get("https://iome.ai")
        go_to_app_link = self.driver.find_element(By.XPATH, '//button//span[contains(text(), "Go to app")]/..')
        go_to_app_link.click()
        time.sleep(2) 
        self.driver.back()