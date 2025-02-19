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

def test_empty_todo_not_added(driver):  # AC5
    driver.get("https://todomvc.com/examples/react/dist/")
    wait = WebDriverWait(driver, 10)

    todo_input = wait.until(EC.presence_of_element_located((By.ID, "todo-input")))

    # Initial checks (before any input)
    initial_todo_count = get_todo_count(driver)  # Helper function (see below)
    initial_todo_items = driver.find_elements(By.CSS_SELECTOR, ".todo-list li")

    # Try adding an empty todo
    todo_input.send_keys("")
    todo_input.send_keys(Keys.RETURN)

    # Try adding a todo with only whitespace
    todo_input = wait.until(EC.presence_of_element_located((By.ID, "todo-input")))  # Re-find the input
    todo_input.send_keys("   ")  # Only spaces
    todo_input.send_keys(Keys.RETURN)

    # Check that no NEW todo items were added
    current_todo_items = driver.find_elements(By.CSS_SELECTOR, ".todo-list li")
    assert len(current_todo_items) == len(initial_todo_items), "No new todos should be added"  # Compare lengths

    # Check that the item count remains the same (0 or whatever it was initially)
    current_todo_count = get_todo_count(driver)
    assert current_todo_count == initial_todo_count, "Todo count should not change"

def get_todo_count(driver):  # Helper function to get the todo count
    try:
        item_count_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "todo-count"))
        )
        item_count_text = item_count_element.text.split(" ")[0]  # Extract the number
        return int(item_count_text)
    except: # handle the case where todo-count is not found.
        return 0