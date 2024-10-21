import time
from selenium import webdriver
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
        self.driver.get("https://dev.iome.ai")
        self.driver.find_element(By.XPATH, '//a[contains(@href,/docs/devportal/]')').click()
        time.sleep(2)
        self.driver.back()

    def test_developer(self):
        self.driver.get("https://dev.iome.ai")
        self.driver.find_element(By.XPATH, '//a[contains(@href,/docs/applications/]')
        time.sleep(2)
        self.driver.back()

    def test_community(self):
        self.driver.get("https://dev.iome.ai")
        self.driver.find_element(By.XPATH, '//a[contains(@href,/docs/authentication/]')
        time.sleep(2)
        self.driver.back()

    def test_go_to_app(self):
        self.driver.get("https://dev.iome.ai")
        self.driver.find_element(By.XPATH, '//a[contains(@href,/docs/widget/]')
        go_to_app_link.click()
        time.sleep(2) 
        self.driver.back()
        
    def test_go_to_app(self):
        self.driver.get("https://dev.iome.ai")
        self.driver.find_element(By.XPATH, '//a[contains(@href,/docs/api/]')
        go_to_app_link.click()
        time.sleep(2) 
        self.driver.back()