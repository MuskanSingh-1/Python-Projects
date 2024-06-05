
#Importing all the needed extentions
import csv
import os
from datetime import datetime

#Creating a class that can store all the funtions for expense tracker
class Expense_Tracker:
    #using init function to initialize object attributes
    def __init__(self):
        self.expenses = []
        self.categories = ["food", "transportation", "entertainment", "utilities", "others"]
        self.filepath = 'expenses.csv'
        self.loadExpenses()
    
    #Funtion to read data from the csv file
    def loadExpenses(self):
        if not os.path.exists(self.filepath):
            self.expenses = []
            return

        with open(self.filepath, 'r', newline='') as file:
            reader = csv.reader(file)
            self.expenses = [row for row in reader]

    #Funtion to add a new expense in the existing csv file of expenses along with date and time of input
    def AddExpense(self, amount, description, category):
        if category not in self.categories:
            print("Invalid category. Available categories are:", ", ".join(self.categories))
            return
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            return

        expense = [amount, description, category, datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
        self.expenses.append(expense)
        self.SaveExpenses()
        print("Expense added successfully.")

    #Funtion to get the Category wise expense summary
    def CategoryExpenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return

        category_summary = {category: 0 for category in self.categories}
        for expense in self.expenses:
            category_summary[expense[2]] += float(expense[0])

        print("Category-wise Expense Summary:")
        for category, total in category_summary.items():
            print(f"{category}: ₹{total:.2f}")

    #Function to view the expense list including all the previos expense
    def ViewExpenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        for expense in self.expenses:
            print(f"Amount: ₹{expense[0]}, Description: {expense[1]}, Category: {expense[2]}, Date: {expense[3]}")

    #Funtion to save the expenses in the csv file ie expenses.csv
    def SaveExpenses(self):
        with open(self.filepath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.expenses)

    #Funtion to calculate the monthly summary of expenses
    def SummarizeExpenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return

        summary = {}
        for expense in self.expenses:
            month = expense[3][:7]
            if month not in summary:
                summary[month] = 0
            summary[month] += float(expense[0])

        print("Monthly Expense Summary:")
        for month, total in summary.items():
            print(f"{month}: ₹{total:.2f}")

    #Funtion for the user interface so that user can choose different options accordingly
    def user_interface(self):
        while True:
            print("\nExpense Tracker Menu:")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Monthly Summary")
            print("4. Category-wise Summary")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                amount = input("Enter amount: ")
                description = input("Enter description: ")
                category = input("Enter category: ")
                self.AddExpense(amount,description,category)
            elif choice == '2':
                self.ViewExpenses()
            elif choice == '3':
                self.SummarizeExpenses()
            elif choice == '4':
                self.CategoryExpenses()
            elif choice == '5':
                print("Exiting Expense Tracker.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tracker = Expense_Tracker()
    tracker.user_interface()
