from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time as t

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

path = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service = path)
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
open_windows = driver.window_handles

driver.switch_to.window(open_windows[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()

driver.switch_to.window(open_windows[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text

