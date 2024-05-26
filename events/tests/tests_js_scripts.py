import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class TestScrollBehavior(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driver_path = r'\LongExam\chromedriver_win32\chromedriver.exe'
        cls.service = Service(driver_path)
        cls.service.start()
        cls.driver = webdriver.Chrome(service=cls.service, options=webdriver.ChromeOptions())
        cls.driver.implicitly_wait(10)
        cls.driver.set_page_load_timeout(10)
        cls.driver.get('file:///D:/LongExam/templates/home.html')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.service.stop()

    def test_scroll_behavior(self):
        # Assertions for scroll behavior
        initial_scroll_position = self.driver.execute_script('return window.pageYOffset;')
        self.assertEqual(initial_scroll_position, 0)

        self.driver.execute_script('window.scrollTo(0, 100);')
        scrolled_scroll_position = self.driver.execute_script('return window.pageYOffset;')
        self.assertEqual(scrolled_scroll_position, 100)

        self.driver.execute_script('window.scrollTo(0, 0);')
        scrolled_scroll_position = self.driver.execute_script('return window.pageYOffset;')
        self.assertEqual(scrolled_scroll_position, 0)

if __name__ == '__main__':
    unittest.main()
