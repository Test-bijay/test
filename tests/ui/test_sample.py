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
        self.wait = WebDriverWait(self.driver, 20)  # Increase wait time to 20s

    def test_google_search(self):
        self.driver.get("https://www.google.com")

        # Try to accept cookie consent (multiple button text variants)
        consent_buttons_texts = ["I agree", "Accept all", "Agree", "Accept"]

        for text in consent_buttons_texts:
            try:
                consent_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(),'{text}')]")))
                consent_button.click()
                break
            except Exception:
                pass  # Try next button text

        # Wait for search box and search
        search_box = self.wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search_box.send_keys("GitHub Actions")
        search_box.submit()

        # Wait for one of the possible results selectors:
        try:
            # Try old results container
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.g')))
        except:
            try:
                # Try new possible selector (sometimes Google changes this)
                self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="search-result"]')))
            except:
                # Try to find the "About X results" text instead
                self.wait.until(EC.presence_of_element_located((By.ID, 'result-stats')))

        # Try to collect results from any of the selectors
        results = self.driver.find_elements(By.CSS_SELECTOR, 'div.g')
        if not results:
            results = self.driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="search-result"]')

        self.assertTrue(len(results) > 0, "No search results found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
