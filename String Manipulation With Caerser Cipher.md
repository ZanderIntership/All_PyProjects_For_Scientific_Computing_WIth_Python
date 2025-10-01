Expense Tracker (Python)

This is a simple command-line based Expense Tracker written in Python.
It allows users to add, view, and filter expenses, as well as calculate the total amount spent.

Features

Add Expense: Enter an amount and category to record a new expense.

List Expenses: View all expenses that have been added.

Total Expenses: Calculate and display the total sum of all expenses.

Filter by Category: View expenses belonging to a specific category.

Exit Option: Safely exit the program.

Code Overview

The program is divided into several functions:

add_expense(expenses, amount, category)
Adds a new expense (with amount and category) to the list.

print_expenses(expenses)
Prints all expenses in a formatted way.

total_expenses(expenses)
Calculates and returns the sum of all expenses.

filter_expenses_by_category(expenses, category)
Filters expenses by category and returns a filtered list.

main()
Runs the interactive menu loop for the user to interact with the tracker.
