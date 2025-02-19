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

def test_todo_count(driver):  # AC3
    driver.get("https://todomvc.com/examples/react/dist/")
    wait = WebDriverWait(driver, 120)

    # Add some todos
    todos = ["Buy milk", "Walk the dog", "Do laundry"]
    for todo in todos:
        todo_input = wait.until(EC.presence_of_element_located((By.ID, "todo-input")))
        todo_input.send_keys(todo)
        todo_input.send_keys(Keys.RETURN)





 # Check the item count (using CLASS_NAME and extracting the number)
    item_count_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "todo-count")))
    expected_count = len(todos)

    # Extract the number from the text (e.g., "3 items left!")
    actual_count_text = item_count_element.text.split(" ")[0]  # Split by space, take first part
    actual_count = int(actual_count_text)

    assert actual_count == expected_count, f"Expected count: {expected_count}, Actual count: {actual_count}"