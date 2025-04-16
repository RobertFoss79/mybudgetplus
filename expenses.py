from datetime import datetime  # Imports the datetime module for handling date and time
from dateutil import parser  # Imports the parser from dateutil for flexible date parsing

# Defines the base class 'Expense'
class Expense:
    def __init__(self, amount=0.0, date=None):
        # Initializes an Expense object with an amount (default is 0.0)
        # Sets the date to the current date if none is provided
        self.amount = amount
        self.date = date or datetime.now().strftime("%Y-%m-%d")  # Formats today's date as 'YYYY-MM-DD'

    def input_expense(self):
        # Prompts the user to input an expense amount and a date for the expense
        while True:  # Ensures the input process continues until valid data is entered
            try:
                self.amount = float(input(f"Enter {self.__class__.__name__.lower()} expense: "))
                self.amount = round(self.amount, 2)  # Rounds the input amount to two decimal places
                break  # Exits the loop if the input is valid
            except ValueError:
                print("Invalid Input. Please enter a numeric value.")  # Handles invalid numeric input

        while True:  # Ensures the input process continues until a valid date is provided
            user_date = input("Enter the date (YYYY-MM-DD) or leave blank for today: ") or self.date
            try:
                self.date = self.parse_date(user_date)  # Calls the parse_date method to validate and format the date
                break  # Exits the loop if the input date is valid
            except ValueError as e:
                print(e)  # Displays error messages for invalid date input
        return self.amount, self.date  # Returns the expense amount and date

    def parse_date(self, date_string):
        # Validates and parses the date input provided by the user
        try:
            parsed_date = parser.parse(date_string)  # Attempts to parse the provided date string
            return parsed_date.strftime("%Y-%m-%d")  # Formats the parsed date as 'YYYY-MM-DD'
        except ValueError:
            raise ValueError(
                "Invalid date format. Please enter a valid date in the correct format or leave blank for today's date"
            )  # Raises an exception for invalid date formats

# Defines subclasses for various expense types, inheriting from the Expense class
class Rent(Expense):
    pass  # No additional functionality; inherits everything from Expense

class Phone(Expense):
    pass

class Power(Expense):
    pass

class Gas(Expense):
    pass

class Water(Expense):
    pass

class Gasoline(Expense):
    pass

class CarInsurance(Expense):
    pass

class CarPayment(Expense):
    pass

class Internet(Expense):
    pass

class Groceries(Expense):
    pass

class Household(Expense):
    pass

class Hygiene(Expense):
    pass
