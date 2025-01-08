from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("/Users/harisx91/Documents/geckodriver")
driver = webdriver.Firefox(service=service_obj)

driver.get("http://speechtherapyhubnj.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
##https://speechtherapyhubnj.com/meet-the-team/
driver.get("https://speechtherapyhubnj.com/meet-the-team/")

driver.back()
driver.refresh()

driver.minimize_window()

driver.close()

