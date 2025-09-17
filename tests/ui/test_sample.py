import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class GoogleSearchTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.wait = WebDriverWait(self.driver, 15)  # Explicit wait up to 15 seconds

    def test_google_search(self):
        self.driver.get("https://www.google.com")

        # Handle cookie consent popup if present
        try:
            consent_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'I agree')]")))
            consent_button.click()
        except Exception:
            # No consent popup found, continue
            pass

        # Wait for search box and enter query
        search_box = self.wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search_box.send_keys("GitHub Actions")
        search_box.submit()

        # Wait for search results container
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.g')))

        results = self.driver.find_elements(By.CSS_SELECTOR, 'div.g')
        self.assertGreater(len(results), 0, "No search results found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
