import spacy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    doc = nlp(text)
    # Extracting nouns and proper nouns as keywords, for example
    keywords = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]
    return keywords

def scrape_edmonton_journal(user_input):
    keywords = extract_keywords(user_input)
    # Update this driver path to your own path, for Windows install chromedriver and place it in a folder and run this command in terminal
    # setx CHROMEDRIVER_PATH "your_path\chromedriver.exe"
    driver_path = os.environ.get('CHROMEDRIVER_PATH')
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("https://edmontonjournal.com/")

    headlines = driver.find_elements(By.TAG_NAME, "h2")
    for headline in headlines:
        if any(keyword.lower() in headline.text.lower() for keyword in keywords):
            print(headline.text)

    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    user_query = "Gas prices"  # Example user input
    scrape_edmonton_journal(user_query)
