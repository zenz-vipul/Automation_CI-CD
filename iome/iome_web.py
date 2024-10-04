import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_links(driver):
    driver.get("https://iome.ai")  # Replace with the actual URL

    # Check "Digital You" link
    digital_you_link = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Digital You')]"))
    )
    digital_you_link.click()
    assert driver.current_url == "https://iome.ai/#the-digital-you"

    # Check "Developer" link
    driver.get("https://iome.ai")  # Go back to the main page
    developer_link = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Developer')]"))
    )
    developer_link.click()
    assert driver.current_url == "https://dev.iome.ai"

    # Check "Community" link
    driver.get("https://iome.ai")  # Go back to the main page
    community_link = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Community')]"))
    )
    community_link.click()
    assert driver.current_url == "https://join.slack.com/t/iomeai/shared_invite/zt-20s1w9jxg-unzBomKqMBrrq~DlYNpQHQ"

    # Check "Go to app" link
    driver.get("https://iome.ai")  # Go back to the main page
    go_to_app_link = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Go to app')]"))
    )
    go_to_app_link.click()
    assert driver.current_url == "https://iome.ai/login/"

def test_links_integration(driver):  # Corrected function signature
    test_links(driver)