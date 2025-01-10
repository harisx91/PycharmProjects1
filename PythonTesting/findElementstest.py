##https://rahulshettyacademy.com/dropdownsPractise/
import time as t
from datetime import datetime, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service = path)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
t.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

print(len(countries))
##CSSlocator #li[class='ui-menu-item'] a

for country in countries:
    if country.text =="India":
        country.click()
    #elif country.text == "Indonesia":
        break

#print(driver.find_element(By.ID, "autosuggest").text)
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"