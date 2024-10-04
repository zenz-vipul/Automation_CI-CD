import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
firefox_options.add_argument('--headless')

class TestSignUp:
    def setup_method(self):
        self.driver = webdriver.Firefox(options=firefox_options)
        self.driver.get('https://iome.ai')
        self.driver.maximize_window()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[span[text()="Go to app"]]'))
        )
        self.driver.find_element(By.XPATH, '//button[span[text()="Go to app"]]').click()

    def teardown_method(self):
        self.driver.quit()

    def test_login(self):
        random_username = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
        random_password = "".join(random.choices(string.ascii_letters + string.digits, k=10))

        if not self.login(random_username, random_password):
            print("Login failed with random credentials.")
            time.sleep(3)
            self.driver.back()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//button[span[text()="Go to app"]]'))
            )
            self.driver.find_element(By.XPATH, '//button[span[text()="Go to app"]]').click()

            actual_username = "test26sep"
            actual_password = "Test@123"
            if self.login(actual_username, actual_password):
                print("Login successful with actual credentials.")
            else:
                print("Login failed with actual credentials.")
                assert False, "Test failed: Unable to login with specified credentials."
        else:
            print("Login successful with random credentials (unexpected).")

    def login(self, username, password):
        try:
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]'))
            )
            username_field.clear()   
            username_field.send_keys(username)

            password_field = self.driver.find_element(By.XPATH, '//input[@placeholder="Password"]')
            password_field.clear()   
            password_field.send_keys(password)

            self.driver.find_element(By.XPATH, '//button[span[text()="Login"]]').click()

            WebDriverWait(self.driver, 10).until(
                EC.url_contains("digitalme")
            )
            assert "digitalme" in self.driver.current_url
            time.sleep(3)
            print(f"Successfully logged in with username: {username}")
            return True
        
        except Exception as e:
            print(f"Login error with username: {username}, Error: {e}")
            return False
