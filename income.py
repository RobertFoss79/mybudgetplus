from datetime import datetime  # Importing the datetime module to handle dates and times
from dateutil import parser  # Importing the parser from the dateutil library for flexible date parsing

# Defining the base class 'Income'
class Income:
    def __init__(self, amount=0.0, date=None):
        # Initializes an Income object with a default amount of 0.0 and an optional date
        self.amount = amount
        self.date = date or datetime.now().strftime("%Y-%m-%d")  # Sets date to today if no date is provided

    def input_income(self):
        # Prompts user for an income amount and a date
        while True:  # Loop to ensure valid input for the income amount
            try:
                self.amount = float(
                    input(f"Enter {self.__class__.__name__.lower()} income: ")
                )  # Converts input to a floating-point number
                self.amount = round(self.amount, 2)  # Rounds the income to two decimal places
                break  # Exits loop when valid input is received
            except ValueError:
                print("Invalid Input. Please enter a numeric value.")  # Error message for non-numeric input

        while True:  # Loop to ensure valid input for the date
            user_date = (
                input("Enter the date (YYYY-MM-DD) or leave blank for today: ")
                or self.date  # Uses today's date if no input is provided
            )
            try:
                self.date = self.parse_date(user_date)  # Parses and validates the entered date
                break  # Exits loop when valid date is received
            except ValueError as e:
                print(e)  # Displays error message for invalid date input
        return self.amount, self.date  # Returns the income amount and date

    def parse_date(self, date_string):
        # Validates and parses the user-provided date string
        try:
            parsed_date = parser.parse(date_string)  # Attempts to parse the date using dateutil
            return parsed_date.strftime("%Y-%m-%d")  # Formats the parsed date as 'YYYY-MM-DD'
        except ValueError:
            raise ValueError(
                "Invalid date format. Please enter a valid date in the correct format or leave blank for today's date"
            )  # Raises an error for invalid date format

# Subclasses for specific income categories, inheriting from the Income base class
class PayrollIncome(Income):
    pass  # No additional functionality; inherits everything from Income

class OtherIncome(Income):
    pass
