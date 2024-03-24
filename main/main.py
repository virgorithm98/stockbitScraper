from selenium import webdriver
import time
import functions

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import constants

# Setup browser
browser = webdriver.Chrome()
browser.maximize_window()

# <--- STOCKBIT LOGIN --->#
functions.login(browser, constants.LOGIN_URL, constants.USERNAME, constants.PASSWORD)

# <--- ACCESSING STOCK MARKET DATA ---> #
code = "MDLN"
browser.get("https://stockbit.com/symbol/" + code)

# retrieve performance data
functions.retrieve_performance_data(browser)

# retrieve comments
comments_stream = browser.find_elements(By.XPATH, "//div[@class='sc-baf19946-8 gxWIZz']")
for comment in comments_stream:
    print(comment.text)

# retrieve running trade
# click running trade button
browser.find_element(By.XPATH, "//div[@class='sc-gKXOVf sc-a9c7a1f3-0 jqrigJ eXvrMx']/button[@class='sc-a9c7a1f3-6 edPHEx sc-hKpBwk bvvOig'][3]").click()

time.sleep(120)
browser.quit()
