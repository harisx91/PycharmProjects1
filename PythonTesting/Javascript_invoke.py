from selenium import webdriver
from selenium.webdriver.chrome.service import Service

##chrome driver  is intermediate drive to invoke the chrome browser
##service_obj = Service("/opt/homebrew/bin/chromedriver")
##driver = webdriver.Chrome(service= service_obj)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service= service_obj, options=chrome_options)
driver.implicitly_wait(2)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

driver.execute_script('window.scroll(0,document.body.scrollHeight);')
driver.get_screenshot_as_file("screenshot.png")
