import csv
import os

def save_to_file(data, filename):
    """
    Save the budget data to a CSV file with separated sections for income and expenses,
    including totals and final balance.

    Parameters:
    - data: dictionary containing budget data
    - filename: string path to the file where data will be saved
    """
    income_data = {k: v for k, v in data.items() if 'income' in k}
    expense_data = {k: v for k, v in data.items() if k not in income_data}

    total_income = sum(v["amount"] for v in income_data.values())
    total_expenses = sum(v["amount"] for v in expense_data.values())
    final_balance = total_income - total_expenses

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Income"])
        writer.writerow(["Category", "Amount", "Date"])
        for category, details in income_data.items():
            writer.writerow([category, f"{details['amount']:.2f}", details["date"]])

        writer.writerow(["Total Income", f"{total_income:.2f}", ""])

        writer.writerow([])

        writer.writerow(["Expenses"])
        writer.writerow(["Category", "Amount", "Date"])
        for category, details in expense_data.items():
            writer.writerow([category, f"{details['amount']:.2f}", details["date"]])

        writer.writerow(["Total Expenses", f"{total_expenses:.2f}", ""])

        writer.writerow([])

        writer.writerow(["Final Balance", f"{final_balance:.2f}", ""])

    print(f"Budget data saved to {filename}")

def load_from_file(filename):
    """
    Load budget data from a CSV file.

    Parameters:
    - filename: string path to the file from which data will be loaded

    Returns:
    - dictionary containing the loaded budget data
    """
    data = {}
    if not os.path.exists(filename):
        print(f"File not found: {filename}. A new file will be created.")
        return data

    try:
        with open(filename, mode="r") as file:
            reader = csv.reader(file)
            next(reader)
            next(reader)
            for row in reader:
                if len(row) < 3 or row[0] in ["Income", "Expenses", "Total Income", "Total Expenses", "Final Balance"]:
                    continue
                key = row[0]
                try:
                    amount = float(row[1])
                    date = row[2]
                    data[key] = {"amount": amount, "date": date}
                except ValueError:
                    print(f"Skipping invalid row: {row}")
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
    return data
