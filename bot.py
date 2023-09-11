from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

data = []
with open("data_current.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)


def create_account(name, email, day, month, year, password):
    driver.get("https://order.gailsbread.co.uk/account/auth/register")

    name_input = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="firstName"]')))
    email_input = driver.find_element(By.XPATH, '//*[@id="email"]')
    password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
    day_select = Select(driver.find_element(
        By.XPATH, '//*[@id="auth"]/ul/li/div[3]/div/div[1]/select'))
    month_select = Select(driver.find_element(
        By.XPATH, '//*[@id="auth"]/ul/li/div[3]/div/div[2]/select'))
    year_select = Select(driver.find_element(
        By.XPATH, '//*[@id="auth"]/ul/li/div[3]/div/div[3]/select'))
    opt_in = driver.find_element(By.CSS_SELECTOR, '.css-h9oi1u.e379e0i4')
    submit_button = driver.find_element(
        By.XPATH, '//*[@id="auth"]/ul/li/button')

    name_input.send_keys(name)
    email_input.send_keys(email)
    day_select.select_by_value(str(day))
    month_select.select_by_value(str(month))
    year_select.select_by_value(str(year))
    password_input.send_keys(password)
    opt_in.click()
    submit_button.click()


for row in data:
    create_account(*row)
    wait.until(EC.url_contains("order.gailsbread.co.uk/store"))
