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

def test_add_todo(driver):
    driver.get("https://todomvc.com/examples/react/dist/")
    wait = WebDriverWait(driver, 10)  # Explicit wait

    todo_input = driver.find_element(By.CLASS_NAME, "new-todo")
    todo_text = "Buy groceries"
    todo_input.send_keys(todo_text)
    todo_input.send_keys(Keys.RETURN)

    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".todo-list li label")))
    except:
        pytest.fail("Todo item did not appear in the list.")

    assert todo_text in driver.page_source, "Todo text not found on the page."
    assert todo_input.get_attribute("value") == "", "Input field not cleared after adding todo."

# Add more test functions here for other ACs (AC2, AC3, etc.)