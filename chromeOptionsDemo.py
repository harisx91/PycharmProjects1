from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time as t

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('start-maximized')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--ignore-certificate-errors')

path = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service = path, options=chrome_options)

driver.get("https://speechtherapyhubnj.com/")

print(driver.title)

driver.implicitly_wait(5)
