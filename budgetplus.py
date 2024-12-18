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

    while True:
        income_type = (
            input("Enter type of income (payroll/other/done): ").strip().lower()
        )
        if income_type == "payroll":
            payroll = income.PayrollIncome()
            amount, date = payroll.input_income()
            income_data["payroll_income"] = {"amount": amount, "date": date}
        elif income_type == "other":
            other = income.OtherIncome()
            amount, date = other.input_income()
            income_data["other_income"] = {"amount": amount, "date": date}
        elif income_type == "done":
            break
        else:
            print("Invalid choice, please enter 'payroll', 'other', or 'done'.")

    return income_data


def collect_expenses():
    expense_data = {}

    while True:
        expense_type = (
            input(
                "Enter type of expense (rent/power_gas/water_sewer_trash/gas_for_car/car_insurance/car_payment/phone/internet/groceries/household/hygiene/done): "
            )
            .strip()
            .lower()
        )
        if expense_type == "rent":
            rent = expenses.Rent()
            amount, date = rent.input_expense()
            expense_data["rent"] = {"amount": amount, "date": date}
        elif expense_type == "power_gas" or expense_type == "power gas":
            power_gas = expenses.PowerGas()
            amount, date = power_gas.input_expense()
            expense_data["power_gas"] = {"amount": amount, "date": date}
        elif expense_type == "water_sewer_trash":
            water_sewer_trash = expenses.WaterSewerTrash()
            amount, date = water_sewer_trash.input_expense()
            expense_data["water_sewer_trash"] = {"amount": amount, "date": date}
        elif expense_type == "gas_for_car":
            gas_for_car = expenses.Gasoline()
            amount, date = gas_for_car.input_expense()
            expense_data["gas_for_car"] = {"amount": amount, "date": date}
        elif expense_type == "car_insurance":
            car_insurance = expenses.CarInsurance()
            amount, date = car_insurance.input_expense()
            expense_data["car_insurance"] = {"amount": amount, "date": date}
        elif expense_type == "car_payment":
            car_payment = expenses.CarPayment()
            amount, date = car_payment.input_expense()
            expense_data["car_payment"] = {"amount": amount, "date": date}
        elif expense_type == "phone":
            phone = expenses.Phone()
            amount, date = phone.input_expense()
            expense_data["phone"] = {"amount": amount, "date": date}
        elif expense_type == "internet":
            internet = expenses.Internet()
            amount, date = internet.input_expense()
            expense_data["internet"] = {"amount": amount, "date": date}
        elif expense_type == "groceries":
            groceries = expenses.Groceries()
            amount, date = groceries.input_expense()
            expense_data["groceries"] = {"amount": amount, "date": date}
        elif expense_type == "household":
            household = expenses.Household()
            amount, date = household.input_expense()
            expense_data["household"] = {"amount": amount, "date": date}
        elif expense_type == "hygiene":
            hygiene = expenses.Hygiene()
            amount, date = hygiene.input_expense()
            expense_data["hygiene"] = {"amount": amount, "date": date}
        elif expense_type == "done":
            break
        else:
            print("Invalid choice, please enter a valid expense type or 'done'.")

    return expense_data


def main():
    budget_data = {}

    load_existing = input("Do you want to load existing budget data? (yes/no): ").strip().lower()
    file_path = ask_for_file_path("Enter the path to the budget data file (e.g., data/budget_data.csv): ")

    if load_existing == "yes":
        budget_data = utils.load_from_file(file_path)
        if budget_data:
            print(f"Budget data loaded from {file_path}")
        else:
            print("No data found. Starting a new budget.")
    else:
        print("Starting a new budget.")

    total_income = sum(value["amount"] for key, value in budget_data.items() if "income" in key)
    total_expenses = sum(value["amount"] for key, value in budget_data.items() if "expense" in key)

    while True:
        entry_type = input("What would you like to enter? (income/expense/done): ").strip().lower()
        if entry_type == "income":
            income_data = collect_income()
            budget_data.update(income_data)
            total_income += sum(value["amount"] for key, value in income_data.items())
        elif entry_type == "expense":
            expense_data = collect_expenses()
            budget_data.update(expense_data)
            total_expenses += sum(value["amount"] for key, value in expense_data.items())
        elif entry_type == "done":
            break
        else:
            print("Invalid choice, please enter 'income', 'expense', or 'done'.")

    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Net Balance: ${total_income - total_expenses:.2f}")

    file_path = ask_for_file_path("Enter the path to save the budget data file (e.g., data/budget_data.csv): ")
    utils.save_to_file(budget_data, file_path)


if __name__ == "__main__":
    main()
