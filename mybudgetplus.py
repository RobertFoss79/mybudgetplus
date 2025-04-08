import income
import expenses
import utils
import os

def ask_for_file_path(prompt):
    file_path = input(prompt).strip()
    if not file_path:
        home_dir = os.path.expanduser("~")
        file_path = os.path.join(home_dir, "budget_data.csv")
    return file_path

def collect_income():
    income_data = {}
    income_classes = {
        "payroll": income.PayrollIncome,
        "other": income.OtherIncome
    }

    while True:
        income_type = input("Enter type of income (payroll/other/done): ").strip().lower()
        if income_type in income_classes:
            income_instance = income_classes[income_type]()
            amount, date = income_instance.input_income()
            income_data[f"{income_type}_income"] = {"amount": amount, "date": date}
        elif income_type == "done":
            break
        else:
            print("Invalid choice, please enter 'payroll', 'other', or 'done'.")
    return income_data

def collect_expenses():
    expense_data = {}
    expense_classes = {
        "rent": expenses.Rent,
        "power": expenses.Power,
        "gas": expenses.Gas,
        "water": expenses.Water,
        "gasoline": expenses.Gasoline,
        "car_insurance": expenses.CarInsurance,
        "car_payment": expenses.CarPayment,
        "phone": expenses.Phone,
        "internet": expenses.Internet,
        "groceries": expenses.Groceries,
        "household": expenses.Household,
        "hygiene": expenses.Hygiene
    }

    while True:
        # Display available expense options
        options = ", ".join(expense_classes.keys())
        expense_type = input(f"Enter type of expense ({options}) or 'done' to finish: ").strip().lower()
        
        if expense_type in expense_classes:
            expense_instance = expense_classes[expense_type]()
            amount, date = expense_instance.input_expense()
            expense_data[expense_type] = {"amount": amount, "date": date}
        elif expense_type == "done":
            break
        else:
            print(f"Invalid choice. Please choose from ({options}) or enter 'done' to finish.")

    return expense_data


def main():
    budget_data = {}
    load_existing = input("Do you want to load existing budget data? (yes/no): ").strip().lower()
    file_path = ask_for_file_path("Enter the path to the budget data file (e.g., data/budget_data.csv): ")

    if load_existing == "yes":
        try:
            budget_data = utils.load_from_file(file_path)
            if budget_data:
                print(f"Budget data loaded from {file_path}")
            else:
                print("No data found. Starting a new budget.")
        except Exception as e:
            print(f"Error loading file: {e}")
            print("Starting a new budget.")
    else:
        print("Starting a new budget.")

    total_income = sum(value["amount"] for key, value in budget_data.items() if "income" in key)
    total_expenses = sum(value["amount"] for key, value in budget_data.items() if "expense" in key)

    while True:
        entry_type = input("What would you like to enter? (income/expense/done): ").strip().lower()
        if entry_type == "income":
            income_data = collect_income()
            budget_data.update(income_data)
            total_income += sum(value["amount"] for value in income_data.values())
        elif entry_type == "expense":
            expense_data = collect_expenses()
            budget_data.update(expense_data)
            total_expenses += sum(value["amount"] for value in expense_data.values())
        elif entry_type == "done":
            break
        else:
            print("Invalid choice, please enter 'income', 'expense', or 'done'.")

    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Net Balance: ${total_income - total_expenses:.2f}")

    try:
        file_path = ask_for_file_path("Enter the path to save the budget data file (e.g., data/budget_data.csv): ")
        utils.save_to_file(budget_data, file_path)
        print(f"Budget data saved to {file_path}")
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    main()
