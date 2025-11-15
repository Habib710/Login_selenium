from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.maximize_window()

username = "standard_user"
password = "secret_sauce"
url_link = "https://www.saucedemo.com/"

driver.get(url_link)
driver.find_element(By.ID, "user-name").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.ID, "login-button").click()


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "app_logo"))
)
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
driver.find_element(By.ID, "continue-shopping").click()
driver.find_element(By.ID, "react-burger-menu-btn").click()

logout_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
)
logout_btn.click()

login_page_logo = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "login_logo"))
)

assert login_page_logo.text == "Swag Labs"
print("successfuly done the test")

