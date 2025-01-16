from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

#https://homeroom6.doe.state.nj.us/directory/pub

# Initialize the WebDriver (Make sure to replace 'PATH_TO_WEBDRIVER' with your actual path)
path = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service= path)


# Function to scrape school information
def scrape_schools():
    try:
        # Target website URL
        url = "https://example.com/north-jersey-schools"  # Replace with the actual URL
        driver.get(url)

        # Wait for the page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "YOUR_TARGET_ELEMENT"))
        )

        # Find school listings and extract data
        schools = []
        school_elements = driver.find_elements(By.CSS_SELECTOR,
                                               "CSS_SELECTOR_FOR_SCHOOL_CARDS")  # Update with actual selector

        for school in school_elements:
            try:
                name = school.find_element(By.CSS_SELECTOR, "CSS_SELECTOR_FOR_NAME").text
                phone = school.find_element(By.CSS_SELECTOR, "CSS_SELECTOR_FOR_PHONE").text
                email = school.find_element(By.CSS_SELECTOR, "CSS_SELECTOR_FOR_EMAIL").text
                schools.append({"name": name, "phone": phone, "email": email})
            except Exception as e:
                print(f"Error extracting data for a school: {e}")

        # Save the data to a CSV file
        with open("north_jersey_schools.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["Name", "Phone", "Email"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(schools)

        print("Data saved to 'north_jersey_schools.csv'")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()


# Run the scraper
scrape_schools()
