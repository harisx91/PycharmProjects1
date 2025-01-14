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

driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame('mce_0_ifr')

driver.find_element(By.ID, 'tinymce').clear()
#driver.find_element(By.ID, 'tinymce').send_keys("I am able to automate")

driver.switch_to.default_content()
assert "Your content goes here" == driver.find_element(By.CSS_SELECTOR, "h3").text