def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Travel, etc.): ")
    amount = input("Enter the amount spent: ")

    with open("expense.txt", "a") as file:
        file.write(f"{date},{category},{amount}\n")


def view_expense():
    try:
        with open("expense.txt", "r") as file:
            content = file.read()
            return content if content.strip() else "No expenses recorded yet."
    except FileNotFoundError:
        return "No expense file found yet."


def total_spend_by_category():
    try:
        with open("expense.txt", "r") as file:
            lines = file.readlines()
        totals = {}
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) != 3:
                continue
            date, category, amount = parts
            category = category.strip().capitalize()
            try:
                amount = float(amount.strip())
            except ValueError:
                continue
            if category in totals:
                totals[category] += amount
            else:
                totals[category] = amount
        if not totals:
            print("No valid expenses found.")
            return
        print("\nTotal Spent by Category:")
        for cat, total in totals.items():
            print(f"{cat}: ₹{total:.2f}")
    except FileNotFoundError: 
        print(" No expense file found.")


def show_menu():
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total by Category")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            print("\nExpense History:")
            print(view_expense())
        elif choice == "3":
            total_spend_by_category()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu
show_menu()