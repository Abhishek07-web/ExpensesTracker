import json
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_expense(expenses):
    print("\n--- Adding expenses---")

    date = input("Enter a date (DD-MM-YYYY): ")
    category = input("Enter category (Food, Travel, etc): ")

    try:
        amount = float(input("Enter Amount: "))
    except ValueError:
        print("Value Error. please Enter a valid number.")
        return

    note = input("Enter a Note(optional): ")

    expense = {
        "date" : date,
        "category" : category,
        "amount" : amount,
        "note" : note
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense Added Successfully!")

def view_expense(expenses):
    print("\n___View Expense___")

    if not expenses:
        print("No expenses Found!")
        return
    
    for index, expense in enumerate(expenses, start=1):
        print(f"\n Expense {index}")
        print(f"Date       :{expense['date']}")
        print(f"Category   :{expense['category']}")
        print(f"Amount     :${expense['amount']}")
        print(f"Note       :{expense['note']}")

def summary_expense(expenses):
    print("\n____Expense Summary____")      

    if not expenses:
        print("No expenses to summerize ") 
        return

    total = 0
    category_total = {}

    for expense in expenses:
        amount = expense['amount']
        category = expense['category']
        total += amount

        if category in category_total:
            category_total[category] += amount
        else:
            category_total[category] = amount
    print(f"\n Total expense ${total}")   

    print("\nCategory-wise Summary") 
    for category, amount in category_total.items():
        print(f"{category} : ${amount}")
        
    
expenses = load_expenses()
while True:
    print("\n----Personal Expense Tracker----")
    print("\n1. Add Expense: ")
    print("2. View Expense: ")
    print("3. Exit")
    print("4. Expense Summary: ")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense(expenses)
    elif choice == '2':
        view_expense(expenses)
    elif choice == '3':
        print("Exit")
        break
    elif choice == "4":
        summary_expense(expenses)
    else:
        print("Invalid choice, try agian !!!")