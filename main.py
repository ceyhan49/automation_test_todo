from selenium import webdriver
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

# Close the browser window
input("Press Enter to close the browser...")
