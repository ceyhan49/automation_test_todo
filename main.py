from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# This automatically downloads and sets up the ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# Open the desired URL
driver.get("https://treasuryprism.dbs.com")

# Maximize the browser window (optional)
driver.maximize_window()

# Print the title of the opened webpage
print(driver.title)

email_field = driver.find_element(By.ID, "register_email")

# Enter text into the email field
email_field.send_keys("example@example.com")

# Optional: Pause to view
input("Press Enter to close the browser...")

# Close the browser
driver.quit()

# Close the browser window

