from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


def login(browser, url, username, password):
    browser.get(url)
    # email input
    email_or_username_field_input = browser.find_element(By.ID, "username")
    email_or_username_field_input.send_keys(username)
    # password input
    password_field_input = browser.find_element(By.ID, "password")
    password_field_input.send_keys(password)
    # login
    password_field_input.send_keys(Keys.ENTER)


def retrieve_performance_data(browser):
    index = browser.find_element(By.XPATH, "//h3[@class='sc-crXcEl sc-f3f6e11e-4 jDdNzm qCunt']")
    volatility = browser.find_element(By.XPATH, "//h3[@class='sc-crXcEl sc-f3f6e11e-4 ciNPAK qCunt']")
    volatility_percentage = browser.find_element(By.XPATH, "//h3[@class='sc-crXcEl sc-f3f6e11e-4 dEfCjO qCunt']")
    volume = browser.find_element(By.XPATH, "//div[@class='sc-f3f6e11e-12 hcfnCg'][1]/h3[@class='sc-crXcEl eZcWln']")
    average_volume = browser.find_element(By.XPATH,
                                          "//div[@class='sc-f3f6e11e-12 hcfnCg'][2]/h3[@class='sc-crXcEl eZcWln']")

    print(index.text)
    print(volatility.text)
    print(volatility_percentage.text.replace('(', '').replace(')', ''))
    print(volume.text)
    print(average_volume.text)