# Acceptance Criteria for Todo Management

## 1. Adding a Todo

- The user should be able to enter a todo item in the input field.
- Pressing the 'Enter' key should add the todo item to the list.
- The new todo item should appear below any existing todos.
- The input field should be cleared after adding the todo.

## 2. Editing a Todo

- The user should be able to double-click on an existing todo to enter edit mode.
- The todo text should be editable.
- Pressing 'Enter' should save the changes.
- Clicking outside the input field should also save changes.
- The edited todo should reflect the updated text.

## 3. Completing a Todo

- Each todo should have a checkbox to mark it as completed.
- Clicking the checkbox should toggle the completion status.
- Completed todos should have a strikethrough style.
- The completed todos should persist on page reload.

## 4. Deleting a Todo

- Each todo should have a delete (X) button.
- Clicking the delete button should remove the corresponding todo.
- The list should update dynamically, and the deleted todo should not reappear on refresh.

## 5. Filtering Todos

- The user should have filter options: **All, Active, Completed**.
- Clicking 'All' should display all todos.
- Clicking 'Active' should show only incomplete todos.
- Clicking 'Completed' should show only completed todos.
- The filter selection should persist on page reload.
