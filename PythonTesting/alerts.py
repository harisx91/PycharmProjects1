from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service = path)

name = "Haris"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()

alert = driver.switch_to.alert
alerttext = alert.text
print(alerttext)
assert name in alerttext

alert.accept()
#alert.dismiss()
