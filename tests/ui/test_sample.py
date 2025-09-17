import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class GoogleSearchTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument('--headless')  # Run in headless mode on CI
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        # Use webdriver-manager to install and manage chromedriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def test_google_search(self):
        self.driver.get("https://www.google.com")

        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("GitHub Actions")
        search_box.submit()

        self.driver.implicitly_wait(5)

        self.assertIn("GitHub Actions", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
