import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class GoogleSearchTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument('--headless')  # Run Chrome in headless mode
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        # Use webdriver-manager to manage ChromeDriver automatically
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def test_google_search(self):
        self.driver.get("https://www.google.com")

        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("GitHub Actions")
        search_box.submit()

        self.driver.implicitly_wait(5)

        # Verify that some search results are present on the page
        results = self.driver.find_elements(By.CSS_SELECTOR, 'div.g')
        self.assertGreater(len(results), 0, "No search results found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
