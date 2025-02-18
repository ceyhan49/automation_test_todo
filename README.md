# automation_test_todo

This project contains Selenium-based automation tests for the TodoMVC application.

## Acceptance Criteria

*   **Adding Todos:**
    *   AC1: A user can add a new todo item by typing text in the input field and pressing Enter.
    *   AC2: A user can add multiple todo items.
    *   AC3: Added todo items are displayed in the list.
    *   AC4: The input field should be cleared after adding a todo.
    *   AC5: Empty todo items (including whitespace) should not be added.
*   **Completing Todos:**
    *   AC6: A user can mark a todo item as complete by clicking the checkbox next to it.
    *   AC7: Completed todo items are visually distinct (e.g., strikethrough).
    *   AC8: Completing a todo does not remove it from the list.
*   **Deleting Todos:**
    *   AC9: A user can delete a todo item by clicking the "x" button next to it.
    *   AC10: Deleting a todo removes it from the list.
*   **Editing Todos:**
    *   AC11: A user can edit a todo by double-clicking on it.
    *   AC12: The todo item becomes editable.
    *   AC13: Changes are saved by pressing Enter or clicking outside the edit field.
    *   AC14: Editing a todo item updates the displayed text.
*   **Filtering Todos:**
    *   AC15: Users can filter todos to show "All," "Active," or "Completed" items.
    *   AC16: The correct number of items is shown in each filter view.
*   **Clearing Completed Todos:**
    *   AC17: Users can clear all completed todos at once using the "Clear completed" button.
*   **Item Count:**
    *   AC18: The number of active (incomplete) items is correctly displayed.

## Prerequisites

*   Python 3.x
*   Selenium WebDriver (`pip install selenium`)
*   ChromeDriver (or appropriate driver for your browser - download from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads) and place in a suitable location, and add it to your system PATH)
*   HtmlTestRunner (`pip install html-testRunner`)

## Setup

1.  Clone the repository: `git clone <your_repo_url>`
2.  Navigate to the project directory: `cd TodoMVC-Test`

## Running the Tests

1.  Ensure ChromeDriver is in your system's PATH or provide the path to the executable in your script.
2.  Execute the tests: `python todo_test.py`

## Test Report

An HTML test report will be generated in the `test_reports` directory after each test run.  The report file will be named `TodoAppTest_*.html` (where * is the date and time of the run).

## Implementation Strategy Overview

The tests were developed using Python and Selenium. The approach was to create separate test methods for each acceptance criterion, ensuring thorough coverage of the user story.  The tests cover adding, completing, deleting, and editing todos, as well as filtering and clearing completed items.  Explicit waits (`WebDriverWait`) were used to handle dynamic content loading, making the tests more robust. The `HtmlTestRunner` library was used to generate an HTML test report, providing a clear overview of the test results.  The Page Object Model (POM) was considered, but due to the simplicity of the application, a straightforward approach was used.  For larger projects, POM is highly recommended.
