import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_input_field_cleared_after_adding_todo(driver):  # AC4 (Corrected)
    driver.get("https://todomvc.com/examples/react/dist/")  # Indented
    wait = WebDriverWait(driver, 120)  # Indented

    todo_input = wait.until(EC.presence_of_element_located((By.ID, "todo-input")))  # Indented
    todo_input.send_keys("Buy groceries")  # Indented
    todo_input.send_keys(Keys.RETURN)  # Indented

    # Check if the input field is cleared  # Indented
    assert todo_input.get_attribute("value") == "", "Input field should be cleared"  # Indented