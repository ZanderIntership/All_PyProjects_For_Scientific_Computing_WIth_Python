class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        # Title
        title = self.name.center(30, "*") + "\n"
        # Items
        items = ""
        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amt = f"{item['amount']:.2f}".rjust(7)
            items += f"{desc}{amt}\n"
        # Total
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    # Calculate spending per category (withdrawals only)
    withdrawals = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += -item["amount"]
        withdrawals.append(spent)

    total_spent = sum(withdrawals)
    percentages = [(w / total_spent) * 100 for w in withdrawals]

    # Title
    chart = "Percentage spent by category\n"

    # Bars (100 down to 0)
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for p in percentages:
            if p >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    # Dashes
    chart += "    -" + "---" * len(categories) + "\n"

    # Category names vertically
    max_len = max(len(c.name) for c in categories)
    for i in range(max_len):
        chart += "     "
        for c in categories:
            if i < len(c.name):
                chart += c.name[i] + "  "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += "\n"

    return chart
