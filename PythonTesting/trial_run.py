from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time as t

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


path = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service = path)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
actual_List = []

driver.implicitly_wait(5)
#Search for ca in dynamic dropdown
driver.find_element(By.CSS_SELECTOR, '.search-keyword').send_keys("ca")


#Add to cart for each one
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0

#for result in results:
    #actual_List.append(result.find_element(By.XPATH, 'h4').text)
    #result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CLASS_NAME, 'cart-icon').click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()


#Click on the cart

#Click on proceed to checkout

#Apply code