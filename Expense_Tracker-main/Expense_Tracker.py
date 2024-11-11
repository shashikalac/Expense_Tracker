import csv
from datetime import datetime
import os

# Define the file to store expenses
file_name = "expenses.csv"

# Initialize categories for expenses
categories = ["Food", "Transportation", "Entertainment", "Utilities", "Other"]

# Function to initialize the expense file
def initialize_file():
    if not os.path.exists(file_name):
        with open(file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Description", "Category"])

# Function to add an expense
def add_expense(amount, description, category):
    date = datetime.now().strftime("%Y-%m-%d")
    if category not in categories:
        print("Invalid category. Please choose from:", ", ".join(categories))
        return
    with open(file_name, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, description, category])
    print("Expense added successfully.")

# Function to view all expenses
def view_expenses():
    with open(file_name, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            print(f"Date: {row[0]}, Amount: {row[1]}, Description: {row[2]}, Category: {row[3]}")

# Function to view monthly summary
def monthly_summary(month):
    total = 0.0
    with open(file_name, mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            expense_date = datetime.strptime(row[0], "%Y-%m-%d")
            if expense_date.strftime("%Y-%m") == month:
                total += float(row[1])
                print(f"Date: {row[0]}, Amount: {row[1]}, Description: {row[2]}, Category: {row[3]}")
    print(f"Total expenses for {month}: {total}")

# Function to get category-wise expenditure
def category_summary():
    category_totals = {category: 0.0 for category in categories}
    with open(file_name, mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            category_totals[row[3]] += float(row[1])
    for category, total in category_totals.items():
        print(f"Category: {category}, Total Expenditure: {total}")

# Main function
def main():
    initialize_file()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Monthly Summary")
        print("4. Category-wise Summary")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            category = input(f"Enter category ({', '.join(categories)}): ")
            add_expense(amount, description, category)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            month = input("Enter month (YYYY-MM): ")
            monthly_summary(month)
        elif choice == "4":
            category_summary()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
main()