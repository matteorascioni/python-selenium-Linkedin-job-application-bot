import time
import os 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Selenium Driver setup
chrome_driver_path = "/Users/matteorascioni/Development/chromedriver"
service = Service(executable_path=chrome_driver_path)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
driver = webdriver.Chrome(service=service, options=chrome_options)

# User info
email = os.environ.get("EMAIL")
password = os.environ.get("PW")
phone = os.environ.get("PHONE_NUM")

# Get the endpoint to scrape
url = '' # <-- Your LinkedIn query
driver.get(url)

#Signing in
first_sign_in = driver.find_element(by="css selector", value=".btn-secondary-emphasis")
first_sign_in.click()
# Wait for page to load
time.sleep(3)
email_field = driver.find_element(by="id", value="username")
email_field.send_keys(email)
password_field = driver.find_element(by="id", value="password")
password_field.send_keys(password)
sign_in_button = driver.find_element(by="xpath", value="//*[@id='organic-div']/form/div[3]/button")
sign_in_button.click()

#Wait for page to load and solve captcha
time.sleep(20)

#Define a method to apply for a job
def apply():
    easy_apply = driver.find_element(by="css selector", value=".jobs-apply-button--top-card")
    easy_apply.click()
    time.sleep(5)
    #Fill in application fields
    phone_field = driver.find_element(by="css selector", value='.artdeco-text-input--input')
    if phone_field.get_attribute("value") == "":
        phone_field.send_keys(phone)
    check_button = driver.find_element(by="css selector", value=".artdeco-button--primary span")
    #Check if button is submit or next
    if check_button.text != "Next":
        submit = driver.find_element(by="css selector", value=".artdeco-button--primary")
        submit.click()
        time.sleep(5)
    else:
        close = driver.find_element(by="css selector", value=".artdeco-modal__dismiss")
        close.click()
        time.sleep(2)
        discard = driver.find_element(by="css selector", value=".artdeco-modal__confirm-dialog-btn")
        discard.click()
        time.sleep(2)

# Store job listings on page to click on for applying
job_listings = driver.find_elements(by="css selector", value=".jobs-search-results__list-item")

for job_listing in job_listings:
    time.sleep(3)
    job_listing.click()
    time.sleep(3)
    apply()

driver.quit()