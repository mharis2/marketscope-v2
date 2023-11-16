from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time

def scrape_edmonton_journal():
    # Update this driver path to your own path, for Windows install chromedriver and place it in a folder and run this command in terminal
    # setx CHROMEDRIVER_PATH "your_path\chromedriver.exe"
    driver_path = os.environ.get('CHROMEDRIVER_PATH') 
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("https://edmontonjournal.com/")

    # Example: Extract news headlines
    headlines = driver.find_elements(By.TAG_NAME, "h2")
    for headline in headlines:
        print(headline.text)

    time.sleep(5)  # Sleep for 5 seconds
    driver.quit()

if __name__ == "__main__":
    scrape_edmonton_journal()
