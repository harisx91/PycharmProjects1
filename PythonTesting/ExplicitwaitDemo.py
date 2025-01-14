from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time as t

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

path = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service = path)

#5 seconds is max time out is implicitly waiting
driver.implicitly_wait(2)

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

#Sum Validation
prices= driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)

print(sum)

total_amount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert sum == total_amount

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
#t.sleep(5)
###Explicity wait would be Web Driver Wait with 2 arguements given
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

