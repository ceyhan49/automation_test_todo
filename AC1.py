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

def test_add_todo(driver):  # AC1
    driver.get("https://todomvc.com/examples/react/dist/")
    wait = WebDriverWait(driver, 10)

    todo_input = wait.until(EC.presence_of_element_located((By.ID, "todo-input")))  # Wait for input field
    todo_text = "Buy groceries"
    todo_input.send_keys(todo_text)
    todo_input.send_keys(Keys.RETURN)

    todo_label = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".todo-list li label")))  # Wait for todo label
    assert todo_label.text.strip() == todo_text, f"Expected: '{todo_text}', Actual: '{todo_label.text.strip()}'"