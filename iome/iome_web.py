import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-software-rasterizer")  # Useful for headless Chrome
    options.add_argument("--remote-debugging-port=9222")  # Required for DevTools
    driver = webdriver.Chrome(options=options)
    url = os.environ.get('URL') or 'https://iome.ai'
    driver.get(url)
    yield driver
    driver.quit()

def test_nav_links(driver):
    try:
        print("Waiting for page to be fully loaded...")
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        print("Page is fully loaded!")
        
        print("Waiting for navbar to be visible...")
        navbar = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.ant-col.flex.justify-end'))
        )
        print("Navbar is visible!")
        nav_links = navbar.find_elements(By.TAG_NAME, 'a')

        for link in nav_links:
            link_name = link.text.strip()
            link_url = link.get_attribute("href")

            if not link_name or "mailto:" in link_url:
                print(f"Skipping link: {link_name or 'empty'}")
                continue
            
            print(f"Testing navbar link: {link_name} -> {link_url}")
            driver.get(link_url)

            expected_url = {
                "Digital You": "https://iome.ai/#the-digital-you",
                "Developer": "https://dev.iome.ai/",
            }
            
            if link_name in expected_url:
                assert driver.current_url == expected_url[link_name], f"Navigation Link '{link_name}' did not redirect correctly or is broken."
            else:
                print(f"Skipping validation for link: {link_name}")

            driver.back()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.ant-col.flex.justify-end'))
            ) 

    except TimeoutException:
        pytest.fail("Timeout: Navbar could not be located.")
    except Exception as e:
        pytest.fail(f"Error locating links: {e}")
