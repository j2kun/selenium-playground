import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.binary_location = "/usr/bin/google-chrome"
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(
    options=chrome_options,
)

driver.get("http://www.python.org")
time.sleep(2)
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
time.sleep(2)
elem.send_keys(Keys.RETURN)
time.sleep(2)
assert "No results found." not in driver.page_source
driver.close()
