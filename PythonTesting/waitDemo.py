from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time as t

path = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service = path)

#5 seconds is max time out is implicitly waiting
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

t.sleep(2)

##driver.find_element(By.CLASS_NAME, "//div[@class = 'product']/div")
##div{@class='product'
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
#t.sleep(5)

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
