from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time as t

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
browserSortedVeggies = []

path = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service = path)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

#click on column header
driver.find_element(By.XPATH,"//span[text()= 'Veg/fruit name']").click()
#collect all veggie names -> veggiesList
veggieList = driver.find_elements(By.XPATH,'//tr/td[1]')
for veggy in veggieList:
    browserSortedVeggies.append(veggy.text)

originalBrowserSortedList = browserSortedVeggies.copy()

#Sort this veggieList == newSortedList
browserSortedVeggies.sort()

assert browserSortedVeggies == originalBrowserSortedList

#veggieList == newSortedList




