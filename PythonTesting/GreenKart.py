###https://rahulshettyacademy.com/seleniumPractise/
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service = path)

driver.get("https://rahulshettyacademy.com/seleniumPractise/")

#//attribute[@type='value']
driver.find_element(By.XPATH, "(//button[type='button'])").click()

#Custom Xpath//tagname[@attribute="value"] -> //input[@type="submit"]
#driver.find_element(By.XPATH, "//input[@type='submit']").click()