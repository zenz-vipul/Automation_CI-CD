import random
import string
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options

class LoginAutomation:
    def __init__(self, driver):
        self.driver = driver

    def setup(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def click_go_to_app(self):
        try:
            go_to_app_button = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//button[span[text()='Go to app']]")
                )
            )
            go_to_app_button.click()
        except TimeoutException:
            print("Timed out waiting for the 'Go to app' button to load.")
        print(self.driver.page_source)

    def login(self, username, password):
        try:
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//input[@placeholder="Username"]')
                )
            )
            username_field.send_keys(username)

            password_field = self.driver.find_element(
                By.XPATH, '//input[@placeholder="Password"]'
            )
            password_field.send_keys(password)

            self.driver.find_element(By.XPATH, '//button[span[text()="Login"]]').click()

            WebDriverWait(self.driver, 20).until(EC.url_contains("digitalme"))
            print(f"Login successful with Username: {username} and Password: {password}")
            return True
        except TimeoutException:
            print(f"Login timed out for Username: {username} and Password: {password}")
            return False

    def generate_random_credentials(self):
        username = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
        password = "".join(random.choices(string.ascii_letters + string.digits, k=10))
        return username, password

    def login_to_account(self, username, password):
        print(f"Logging in with Username: {username}")
        print(f"Logging in with Password: {password}")

        self.click_go_to_app()
        return self.login(username, password)

@pytest.fixture(scope="module")
def driver():
    firefox_options = Options()
    firefox_options.add_argument('--headless') 
    firefox_options.add_argument('--window-size=1920,1080')  # Set the window size to 1920x1080
    driver = webdriver.Firefox(options=firefox_options)
    yield driver   
    driver.quit()  

def test_random_login(driver):
    account = LoginAutomation(driver)
    account.setup("https://iome.ai")

    for _ in range(1):  
        random_username, random_password = account.generate_random_credentials()
        print(f"Testing random Username: {random_username}, Password: {random_password}")
        assert account.login_to_account(random_username, random_password) == False  
        driver.back()
        
def test_specific_login(driver):
    account = LoginAutomation(driver)
    account.setup("https://iome.ai")

    specific_username = "test26sep"
    specific_password = "Test@123"
    print(f"\nNow testing with specific credentials...")
    assert account.login_to_account(specific_username, specific_password) == True  
    time.sleep(3)
    driver.quit()
