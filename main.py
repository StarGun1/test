import time
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from flask import Flask
from selenium import webdriver
app = Flask(__name__)
@app.route('/')
def scrape_example():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get('http://www.example.com')
    button = driver.find_element(By.TAG_NAME, 'a')
    button.click()
    text = driver.find_element(By.TAG_NAME, 'p').text
    driver.quit()
    return text
