from selenium import webdriver
from selenium.webdriver.chrome.service import Service

##chrome driver  is intermediate drive to invoke the chrome browser
##service_obj = Service("/opt/homebrew/bin/chromedriver")
##driver = webdriver.Chrome(service= service_obj)

service_obj = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service= service_obj)

driver.maximize_window()
driver.get("https://google.com")
print(driver.title)
print(driver.current_url)
driver.get("https://google.com")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()

