import time
import json

expenses = []

try:
    file = open("expense.json", "r")
    expenses = json.load(file)
    file.close()
except:
    expenses = []


def save_expenses():
    file = open("expense.json", "w")
    json.dump(expenses, file, indent=4)
    file.close()


while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Total Spending")
    print("5. Spending by Category")
    print("6. Exit")

    # Choose menu option
    while True:
        try:
            option = int(input("Choose an option: "))

            if option < 1 or option > 6:
                print("Invalid option. Please choose between 1 and 6.")
                continue

        except ValueError:
            print("Invalid option. Please enter a number.")
            continue

        break

    # ADD EXPENSE
    if option == 1:
        print("\nAdd Expense")

        try:
            amount = float(input("Enter expense amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

        except ValueError:
            print("Invalid amount.")
            continue

        category = input("Enter expense category: ").strip()

        if category == "":
            print("Category cannot be empty.")
            continue

        if " " in category:
            print("Category cannot contain spaces.")
            continue

        description = input("Enter expense description: ").strip()

        if description == "":
            print("Description cannot be empty.")
            continue

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)
        save_expenses()

        print("Expense added successfully.")
        time.sleep(4)

    # VIEW EXPENSES
    elif option == 2:
        print("\nView Expenses")

        if len(expenses) == 0:
            print("No expenses available.")
            continue

        print("=" * 75)
        print(
            f"{'Index':<8}"
            f"{'Amount':<15}"
            f"{'Category':<20}"
            f"{'Description':<25}"
        )
        print("=" * 75)

        for i, expense in enumerate(expenses, start=1):
            print(
                f"{i:<8}"
                f"{expense['amount']:<15}"
                f"{expense['category']:<20}"
                f"{expense['description']:<25}"
            )

        print("=" * 75)
        time.sleep(4)

    # DELETE EXPENSE
    elif option == 3:
        print("\nDelete Expense")

        if len(expenses) == 0:
            print("No expenses available to delete.")
            continue

        print("=" * 75)
        print(
            f"{'Index':<8}"
            f"{'Amount':<15}"
            f"{'Category':<20}"
            f"{'Description':<25}"
        )
        print("=" * 75)

        for i, expense in enumerate(expenses, start=1):
            print(
                f"{i:<8}"
                f"{expense['amount']:<15}"
                f"{expense['category']:<20}"
                f"{expense['description']:<25}"
            )

        print("=" * 75)

        try:
            index_delete = int(input("Enter the number of the expense to delete (e.g. 1, 2, 3, 4): "))
        except ValueError:
            print("Invalid expense number.")
            continue

        if index_delete < 1 or index_delete > len(expenses):
            print("Invalid expense number.")
            continue

        index_delete = index_delete - 1

        expenses.pop(index_delete)
        save_expenses()

        print("Expense deleted successfully.")
        time.sleep(4)

    # TOTAL SPENDING
    elif option == 4:
        print("\nTotal Spending")

        total = 0

        for expense in expenses:
            total += expense["amount"]

        print(f"Total: {total}")
        time.sleep(4)

    # SPENDING BY CATEGORY
    elif option == 5:
        print("\nSpending by Category")

        if len(expenses) == 0:
            print("No expenses available.")
            continue

        categories = []

        for expense in expenses:
            if expense["category"] not in categories:
                categories.append(expense["category"])

        print("\nAvailable Categories:")

        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")

        try:
            category_number = int(input("Choose a category: "))
        except ValueError:
            print("Invalid category number.")
            continue

        if category_number < 1 or category_number > len(categories):
            print("Invalid category number.")
            continue

        category = categories[category_number - 1]

        print(f"\nSelected Category: {category}")

        total = 0

        print("=" * 75)
        print(
            f"{'Amount':<15}"
            f"{'Category':<20}"
            f"{'Description':<25}"
        )
        print("=" * 75)

        for expense in expenses:
            if expense["category"] == category:
                print(
                    f"{expense['amount']:<15}"
                    f"{expense['category']:<20}"
                    f"{expense['description']:<25}"
                )

                total += expense["amount"]

        print("=" * 75)
        print(f"{category} Total: {total}")
        time.sleep(4)

    # EXIT
    elif option == 6:
        print("Exit")
        break
