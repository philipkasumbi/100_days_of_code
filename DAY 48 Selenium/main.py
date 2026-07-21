from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_drive_path = "C:/Users/kasum/Desktop/selenium/chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://www.python.org/")

events = driver.find_elements(By.CSS_SELECTOR,".event-widget li")
upcoming_events={}
for event in events:
    date = event.find_element(By.TAG_NAME,"time").text
    title = event.find_element(By.TAG_NAME, "a").text
    upcoming_events[date]= title

print(upcoming_events)

driver.quit()
