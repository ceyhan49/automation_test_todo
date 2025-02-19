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


def test_add_multiple_todos(driver):  # AC2
    driver.get("https://todomvc.com/examples/react/dist/")
    wait = WebDriverWait(driver, 10)

    todos = ["Buy milk", "Walk the dog", "Do laundry"]

    for todo in todos:
        todo_input = wait.until(EC.presence_of_element_located((By.ID, "todo-input")))  # Wait for input field
        todo_input.send_keys(todo)
        todo_input.send_keys(Keys.RETURN)

    todo_items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".todo-list li")))  # Wait for all items
    assert len(todo_items) == len(todos), f"Expected {len(todos)} items, Actual: {len(todo_items)}"

    todo_labels = [item.find_element(By.TAG_NAME, "label").text.strip() for item in todo_items]
    assert todo_labels == todos, f"Expected: {todos}, Actual: {todo_labels}"


    wait = WebDriverWait(driver, 10)