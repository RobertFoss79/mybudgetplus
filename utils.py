import csv  # Importing csv module for handling CSV file operations
import os  # Importing os module for file and directory management

def save_to_file(data, filename):
    """
    Save the budget data to a CSV file with separated sections for income and expenses,
    including totals and final balance.

    Parameters:
    - data: dictionary containing budget data
    - filename: string path to the file where data will be saved
    """
    # Separate income and expense data for clarity
    income_data = {k: v for k, v in data.items() if 'income' in k}
    expense_data = {k: v for k, v in data.items() if k not in income_data}

    # Calculate totals and final balance
    total_income = sum(v["amount"] for v in income_data.values())
    total_expenses = sum(v["amount"] for v in expense_data.values())
    final_balance = total_income - total_expenses

    # Open the file in write mode and create a CSV writer object
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)

        # Write income data to the file
        writer.writerow(["Income"])  # Income section header
        writer.writerow(["Category", "Amount", "Date"])  # Column headers
        for category, details in income_data.items():  # Iterate through income data
            writer.writerow([category, f"{details['amount']:.2f}", details["date"]])

        # Write total income
        writer.writerow(["Total Income", f"{total_income:.2f}", ""])

        writer.writerow([])  # Blank line for separation

        # Write expense data to the file
        writer.writerow(["Expenses"])  # Expenses section header
        writer.writerow(["Category", "Amount", "Date"])  # Column headers
        for category, details in expense_data.items():  # Iterate through expense data
            writer.writerow([category, f"{details['amount']:.2f}", details["date"]])

        # Write total expenses
        writer.writerow(["Total Expenses", f"{total_expenses:.2f}", ""])

        writer.writerow([])  # Blank line for separation

        # Write final balance
        writer.writerow(["Final Balance", f"{final_balance:.2f}", ""])

    print(f"Budget data saved to {filename}")  # Notify user about file save

def load_from_file(filename):
    """
    Load budget data from a CSV file.

    Parameters:
    - filename: string path to the file from which data will be loaded

    Returns:
    - dictionary containing the loaded budget data
    """
    data = {}  # Initialize an empty dictionary to store budget data

    # Check if the file exists
    if not os.path.exists(filename):
        print(f"File not found: {filename}. A new file will be created.")  # Notify user about missing file
        return data

    try:
        # Open the file in read mode
        with open(filename, mode="r") as file:
            reader = csv.reader(file)  # Create a CSV reader object
            next(reader)  # Skip the section header (e.g., "Income")
            next(reader)  # Skip the column headers

            # Iterate through the rows in the file
            for row in reader:
                # Skip invalid or header rows
                if len(row) < 3 or row[0] in ["Income", "Expenses", "Total Income", "Total Expenses", "Final Balance"]:
                    continue

                # Extract the data from the row
                key = row[0]
                try:
                    amount = float(row[1])  # Convert the amount to a float
                    date = row[2]  # Extract the date
                    data[key] = {"amount": amount, "date": date}  # Store the data in the dictionary
                except ValueError:  # Handle invalid data rows
                    print(f"Skipping invalid row: {row}")
    except Exception as e:  # Handle file read errors
        print(f"An error occurred while loading the file: {e}")
    return data  # Return the loaded data
