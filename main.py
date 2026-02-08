import json
import os
import csv

def export_to_csv(expenses):
    if not expenses:
        

FILE_NAME = "expense.json"
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent = 4)

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
    
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['date']} | {expense['category']} | ${expense['amount']} | {expense['note']}")

def total_expense(expenses):
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses {total}")        

def category_summary(expenses):
    summary = {}

    for exp in expenses:
        category = exp["category"]
        summary[category] = summary.get(category, 0) + exp["amount"]

    print("\n Category-wise Summary")
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt}")
  
expenses = load_expenses()
while True:
    print("\n----Personal Expense Tracker----")
    print("\n1. Add Expense: ")
    print("2. View Expense: ")
    print("3. Total Expense: ")
    print("4. Category Summary: ")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense(expenses)
    elif choice == '2':
        view_expense(expenses)
    elif choice == '3':
        total_expense(expenses)
    elif choice == "4":
        category_summary(expenses)
    elif choice == "5":
        print("GoodBye, Have A Nice Day !")
        break
    else:
        print("Invalid choice, try again")