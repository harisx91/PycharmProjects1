from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

path = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service = path)

driver.get("https://rahulshettyacademy.com/angularpractice/")

#ID, Xpath, CSSSelector, Classname, name, linktext
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

#Custome Xpath//tagname[@attribute="value"] -> //input[@type="submit"]
driver.find_element(By.XPATH, "//input[@type='submit']").click()

message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
#Custom CSSSelector//tagname[@attribute="value"] -> //input[@type="submit"], #id, .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Haris")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()

##Static Dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(1)
#dropdown.select_by_value()


#Xpath for Teo-way Data Binding Xpath: attribute[@value:" " ] input[class='ng-pristine'].send_keys("")
assert "Success" in message
##XPath tagname[@attribute="value"] input[@id="inlinRadio1"] //input[@value='option1']
###driver.find_element(By.XPATH


#Xpath for Teo-way Data Binding Xpath: attribute[@value:" " ] input[class='ng-pristine'].send_keys("")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("hello again")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()