import logging
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

url = "https://moibit.io"


@pytest.fixture(scope="module")
def driver():
    firefox_option = Options()
    firefox_option.add_argument("--headless")
    driver = webdriver.Firefox(options=firefox_option)
    yield driver
    driver.quit()


def test_navigation_links(driver):
    driver.get(url)
    driver.maximize_window()

    links = [
        {"text": "Documentation", "expected_url": "https://docs.moibit.io"},
        {"text": "Pricing", "expected_url": "https://moibit.io/pages/pricing.html"},
        {"text": "Contact us", "expected_url": "#contact"},  # Adjust if necessary
        {"text": "Go to app", "expected_url": "https://dashboard.moibit.io"},
    ]

    for link in links:
        try:
            nav_link = driver.find_element(By.LINK_TEXT, link["text"])
            nav_link.click()
            WebDriverWait(driver, 10).until(EC.url_to_be(link["expected_url"]))
            current_url = driver.current_url
            assert (
                current_url == link["expected_url"]
            ), f"Failed: {link['text']} did not navigate to the expected URL."

            logger.info(f"{link['text']} link is working. Navigated to {current_url}")
            driver.back()
            WebDriverWait(driver, 10).until(EC.url_to_be(url))

        except Exception as e:
            logger.error(f"An error occurred while testing {link['text']}: {e}")


if __name__ == "__main__":
    pytest.main([__file__])
