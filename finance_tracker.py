# step 2 - add expense
expenses = {}
def add_expense():
    try:
        description = input("Enter expense description: ").strip()
        category = input("Enter category: ").strip()
        amount = float(input("Enter amount: ").strip())

        if description == "" or category == "" or amount <= 0:
            print("Invalid input. Please enter valid details.")
            return

        if category not in expenses:
            expenses[category] = []

        expenses[category].append((description, amount))
        print("Expense added successfully.")

    except ValueError:
        print("Invalid amount. Please enter a number.")

# step 3 - view expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    for category, items in expenses.items():
        print("Category:", category)
        for desc, amt in items:
            print(" -", desc + ": $" + str(amt))

# step 4 - view summary
def view_summary():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nExpense Summary:")
    for category, items in expenses.items():
        total = sum(amount for _, amount in items)
        print(category + ": $" + str(total))


# step 7 - menu
def menu():

    # step 1 - intro statement
    print("Welcome to the Personal Finance Tracker!")
    print("What would you like to do?")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary")
    print("4. Exit")
    choice = int(input("Choose an option: "))

    while choice != 4:
        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            view_summary()
        else:
            print("Invalid option. Please choose again.")

        print("What would you like to do?")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")
        choice = int(input("Choose an option: "))
    print("Goodbye!")

menu()