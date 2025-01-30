from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

#NJ School Directory
#https://homeroom6.doe.state.nj.us/directory/pub

# Initialize the WebDriver (Make sure to replace 'PATH_TO_WEBDRIVER' with your actual path)
path = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service= path)

driver.get("https://homeroom6.doe.state.nj.us/directory/pub")

print(driver.title)
driver.find_element(By.ID, "county").send_keys(Keys.ARROW_RIGHT)