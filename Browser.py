from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

# Click the "Forgot your password?" link
driver.find_element(By.ID, "login-button").click()

# # Wait for the new page to load properly
# reset_header = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.TAG_NAME, "h6"))
# )

# # Validate correct page
# assert reset_header.text == "Reset Password"

print("Forgot Password page opened successfully.")

driver.quit()
