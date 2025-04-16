import income  # Imports the income module for income-related classes
import expenses  # Imports the expenses module for expense-related classes
import utils  # Imports a utility module for loading and saving data
import os  # Imports the os module for file and directory management

# Function to prompt user for a file path or default to a pre-defined path
def ask_for_file_path(prompt):
    file_path = input(prompt).strip()  # Prompts user for file path input and removes extra spaces
    if not file_path:  # If user input is empty, use default path in the user's home directory
        home_dir = os.path.expanduser("~")  # Expands the user's home directory path
        file_path = os.path.join(home_dir, "budget_data.csv")  # Constructs the default file path
    return file_path  # Returns the file path

# Function to collect income details from user
def collect_income():
    income_data = {}  # Initializes a dictionary to store income data
    income_classes = {
        "payroll": income.PayrollIncome,  # Maps 'payroll' income to its class
        "other": income.OtherIncome  # Maps 'other' income to its class
    }

    while True:  # Loop to continuously prompt for income types
        income_type = input("Enter type of income (payroll/other/done): ").strip().lower()  # Gets user input
        if income_type in income_classes:  # If valid income type is entered
            income_instance = income_classes[income_type]()  # Creates an instance of the appropriate income class
            amount, date = income_instance.input_income()  # Collects the income amount and date
            income_data[f"{income_type}_income"] = {"amount": amount, "date": date}  # Stores data in dictionary
        elif income_type == "done":  # Ends the loop when 'done' is entered
            break
        else:  # Handles invalid input
            print("Invalid choice, please enter 'payroll', 'other', or 'done'.")
    return income_data  # Returns collected income data

# Function to collect expense details from user
def collect_expenses():
    expense_data = {}  # Initializes a dictionary to store expense data
    expense_classes = {
        "rent": expenses.Rent,  # Maps 'rent' expense to its class
        "power": expenses.Power,  # Maps 'power' expense to its class
        "gas": expenses.Gas,  # Maps 'gas' expense to its class
        "water": expenses.Water,  # Maps 'water' expense to its class
        "gasoline": expenses.Gasoline,  # Maps 'gasoline' expense to its class
        "car_insurance": expenses.CarInsurance,  # Maps 'car insurance' expense to its class
        "car_payment": expenses.CarPayment,  # Maps 'car payment' expense to its class
        "phone": expenses.Phone,  # Maps 'phone' expense to its class
        "internet": expenses.Internet,  # Maps 'internet' expense to its class
        "groceries": expenses.Groceries,  # Maps 'groceries' expense to its class
        "household": expenses.Household,  # Maps 'household' expense to its class
        "hygiene": expenses.Hygiene  # Maps 'hygiene' expense to its class
    }

    while True:  # Loop to continuously prompt for expense types
        options = ", ".join(expense_classes.keys())  # Combines available expense types into a string
        expense_type = input(f"Enter type of expense ({options}) or 'done' to finish: ").strip().lower()  # Gets user input
        if expense_type in expense_classes:  # If valid expense type is entered
            expense_instance = expense_classes[expense_type]()  # Creates an instance of the appropriate expense class
            amount, date = expense_instance.input_expense()  # Collects the expense amount and date
            expense_data[expense_type] = {"amount": amount, "date": date}  # Stores data in dictionary
        elif expense_type == "done":  # Ends the loop when 'done' is entered
            break
        else:  # Handles invalid input
            print(f"Invalid choice. Please choose from ({options}) or enter 'done' to finish.")
    return expense_data  # Returns collected expense data

# Main function to orchestrate the program's flow
def main():
    budget_data = {}  # Initializes a dictionary to store budget data
    load_existing = input("Do you want to load existing budget data? (yes/no): ").strip().lower()  # Prompts user for choice
    file_path = ask_for_file_path("Enter the path to the budget data file (e.g., data/budget_data.csv): ")  # Gets file path

    if load_existing == "yes":  # If user chooses to load existing data
        try:
            budget_data = utils.load_from_file(file_path)  # Attempts to load data from the file
            if budget_data:  # If data is found
                print(f"Budget data loaded from {file_path}")
            else:  # If file is empty
                print("No data found. Starting a new budget.")
        except Exception as e:  # Handles errors during file loading
            print(f"Error loading file: {e}")
            print("Starting a new budget.")
    else:  # If user chooses not to load existing data
        print("Starting a new budget.")

    total_income = sum(value["amount"] for key, value in budget_data.items() if "income" in key)  # Calculates total income
    total_expenses = sum(value["amount"] for key, value in budget_data.items() if "expense" in key)  # Calculates total expenses

    while True:  # Loop to prompt user for entries
        entry_type = input("What would you like to enter? (income/expense/done): ").strip().lower()  # Gets user input
        if entry_type == "income":  # If user chooses 'income'
            income_data = collect_income()  # Collects income data
            budget_data.update(income_data)  # Updates budget data
            total_income += sum(value["amount"] for value in income_data.values())  # Updates total income
        elif entry_type == "expense":  # If user chooses 'expense'
            expense_data = collect_expenses()  # Collects expense data
            budget_data.update(expense_data)  # Updates budget data
            total_expenses += sum(value["amount"] for value in expense_data.values())  # Updates total expenses
        elif entry_type == "done":  # Ends loop when 'done' is entered
            break
        else:  # Handles invalid input
            print("Invalid choice, please enter 'income', 'expense', or 'done'.")

    # Displays summary of total income, expenses, and net balance
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Net Balance: ${total_income - total_expenses:.2f}")

    try:  # Attempts to save budget data to file
        file_path = ask_for_file_path("Enter the path to save the budget data file (e.g., data/budget_data.csv): ")
        utils.save_to_file(budget_data, file_path)
        print(f"Budget data saved to {file_path}")
    except Exception as e:  # Handles errors during file saving
        print(f"Error saving file: {e}")

# Entry point for program execution
if __name__ == "__main__":
    main()  # Calls the main function
