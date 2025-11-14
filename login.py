from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

username = "standard_user"
password = "secret_sauce"
url_link = "https://www.saucedemo.com/"

driver.get(url_link)

driver.find_element(By.ID, "user-name").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)

driver.find_element(By.ID, "login-button").click()


login_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "app_logo"))
)

assert login_element.text == "Swag Labs"
print("Login successful and element found!")

driver.quit()
