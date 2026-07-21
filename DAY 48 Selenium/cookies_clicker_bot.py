from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

helpers = driver.find_element(By.ID, "store")
cookie = driver.find_element(By.ID, "cookie")

start_time = time.time()
timeout = 5

while True:
    cookie.click()

    # Check upgrades every 5 seconds
    if time.time() - start_time >= timeout:

        cookies_money = int(
            driver.find_element(By.ID, "money").text.replace(",", "")
        )

        booster = helpers.find_elements(By.CSS_SELECTOR, "b")

        items = []

        for i, boost in enumerate(booster):
            if " - " not in boost.text:
                continue

            name, price = boost.text.split(" - ")
            price = int(price.replace(",", ""))

            items.append((price, booster[i]))

        best_item = None

        for price, element in items:
            if cookies_money >= price:
                best_item = element

        if best_item:
            best_item.click()

        start_time = time.time()