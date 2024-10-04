import random
import string
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
        """Sets up the browser with the provided URL."""
        self.driver.get(url)
        self.driver.maximize_window()

    def wait_for_element(self, by, value, timeout=20):
        """Waits for an element to be present and visible."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
        except TimeoutException:
            print(f"Element with {by}='{value}' not found after {timeout} seconds.")
            return None

    def click_go_to_app(self):
        """Clicks on the 'Go to app' button if available."""
        go_to_app_button = self.wait_for_element(By.XPATH, "//button[span[text()='Go to app']]", timeout=30)
        if go_to_app_button:
            go_to_app_button.click()
            return True
        return False

    def login(self, username, password):
        """Performs the login with the provided username and password."""
        username_field = self.wait_for_element(By.XPATH, '//input[@placeholder="Username"]', timeout=20)
        if not username_field:
            return False
        username_field.send_keys(username)

        password_field = self.driver.find_element(By.XPATH, '//input[@placeholder="Password"]')
        password_field.send_keys(password)

        login_button = self.driver.find_element(By.XPATH, '//button[span[text()="Login"]]')
        login_button.click()

        try:
            WebDriverWait(self.driver, 20).until(EC.url_contains("digitalme"))
            print(f"Login successful with Username: {username} and Password: {password}")
            return True
        except TimeoutException:
            print(f"Login failed or timed out for Username: {username} and Password: {password}")
            return False

    def generate_random_credentials(self):
        """Generates random credentials for testing."""
        username = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
        password = "".join(random.choices(string.ascii_letters + string.digits, k=10))
        return username, password

    def login_to_account(self, username, password):
        """Performs login by first clicking the 'Go to app' button and then logging in."""
        if not self.click_go_to_app():
            return False
        return self.login(username, password)

@pytest.fixture(scope="module")
def driver():
    firefox_options = Options()
    firefox_options.add_argument('--headless')
    firefox_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Firefox(options=firefox_options)
    yield driver
    driver.quit()

def test_random_login(driver):
    """Tests logging in with random credentials and ensures it fails."""
    account = LoginAutomation(driver)
    account.setup("https://iome.ai")

    random_username, random_password = account.generate_random_credentials()
    assert account.login_to_account(random_username, random_password) == False  # Invalid credentials test

def test_specific_login(driver):
    """Logs in with specific valid credentials and quits after success."""
    account = LoginAutomation(driver)
    account.setup("https://iome.ai")

    specific_username = "test26sep"
    specific_password = "Test@123"
    print(f"\nTesting with specific credentials: {specific_username}, {specific_password}")
    
    assert account.login(specific_username, specific_password) == True  # Valid credentials test
