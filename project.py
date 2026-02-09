import json

# File to store expenses
FILE_NAME = "expenses.json"

def load_expenses():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(expenses):
    item = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Transport/School/Other): ")
    expenses.append({"item": item, "amount": amount, "category": category})
    save_expenses(expenses)
    print("Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['item']} - {exp['amount']} ({exp['category']})")

def summary_report(expenses):
    report = {}
    for exp in expenses:
        category = exp["category"]
        report[category] = report.get(category, 0) + exp["amount"]
    print("\nExpense Summary:")
    for cat, total in report.items():
        print(f"{cat}: {total}")

def main():
    expenses = load_expenses()
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summary Report")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            summary_report(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()