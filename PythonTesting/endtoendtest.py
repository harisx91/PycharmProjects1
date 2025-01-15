from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time as t

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('start-maximized')
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--ignore-certificate-errors')

path = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service = path)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/angularpractice/")

#We need to click on shop
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

product_list = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for product in product_list:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == 'BlackBerry':
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, 'a[class*="btn-primary"]').click()
driver.find_element(By.XPATH, '//button[@class="btn btn-success"]').click()


driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India')))
driver.find_element(By.LINK_TEXT, 'India').click()

driver.find_element(By.XPATH, "//div[@class = 'checkbox checkbox-primary']").click()

driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

success_text = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success! Thank you!" in success_text

driver.close()

