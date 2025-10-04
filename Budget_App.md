💰 Budget App

A Python project that helps you track your spending across different categories like 🍔 Food, 👕 Clothing, and 🎬 Entertainment.
It also generates a neat spending chart 📊 to visualize your expenses.

✨ Features
🗂️ Category Class

Each budget category is an object that supports:

💵 Deposit – deposit(amount, description="")

🏧 Withdraw – withdraw(amount, description="") (fails if insufficient funds)

📊 Balance – get_balance()

🔄 Transfer – transfer(amount, other_category)

✅ Check Funds – check_funds(amount)

📝 Print Ledger – Formatted string with title, transactions, and total

📊 Spending Chart

Function: create_spend_chart(categories)

Shows percentage spent per category (withdrawals only)

Rounded down to the nearest 🔟%

Category names displayed vertically under the chart

Always starts with:
