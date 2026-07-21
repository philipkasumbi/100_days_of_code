from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org/")

search = driver.find_element(By.NAME,"search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

driver.get("https://secure-retreat-92358.herokuapp.com/")
first_name=driver.find_element(By.NAME,"fName")
last_name=driver.find_element(By.NAME,"lName")
email=driver.find_element(By.NAME,"email")
button = driver.find_element(By.TAG_NAME,"button")

first_name.send_keys("philip")
last_name.send_keys("peter")
email.send_keys("philip@gmail.com")
button.send_keys(Keys.ENTER)

time.sleep(10)
driver.quit()



