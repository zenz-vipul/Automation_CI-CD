import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PAGE_URL = os.getenv('PAGE_URL', 'https://iome.ai/')

@pytest.fixture(scope="session")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_digital_you_link(driver):
    driver.get(PAGE_URL)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/#the-digital-you"]')))
    digital_you = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/#the-digital-you"]'))
    )
    digital_you.click()
    WebDriverWait(driver, 20).until(EC.url_contains('/#the-digital-you'))
    assert driver.current_url.endswith('/#the-digital-you')

def test_developer_link(driver):
    driver.get(PAGE_URL)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="https://dev.iome.ai"]')))
    
    developer_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="https://dev.iome.ai"]'))
    )
    assert developer_link.get_attribute('target') == '_blank'
    developer_link.click()
    driver.switch_to.window(driver.window_handles[-1])
    WebDriverWait(driver, 20).until(EC.url_contains('dev.iome.ai'))
    assert 'dev.iome.ai' in driver.current_url
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

def test_community_link(driver):
    driver.get(PAGE_URL)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="https://join.slack.com/t/iomeai/shared_invite/zt-20s1w9jxg-unzBomKqMBrrq~DlYNpQHQ"]')))
    
    community_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="https://join.slack.com/t/iomeai/shared_invite/zt-20s1w9jxg-unzBomKqMBrrq~DlYNpQHQ"]'))
    )
    assert community_link.get_attribute('target') == '_blank'
    community_link.click()
    driver.switch_to.window(driver.window_handles[-1])
    WebDriverWait(driver, 20).until(EC.url_contains('slack.com'))
    assert 'slack.com' in driver.current_url
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

def test_go_to_app_button(driver):
    driver.get(PAGE_URL)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/login/"] button')))
    
    go_to_app_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/login/"] button'))
    )
    go_to_app_button.click()
    WebDriverWait(driver, 20).until(EC.url_contains('/login/'))
    assert driver.current_url.endswith('/login/')
