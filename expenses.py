from datetime import datetime
from dateutil import parser

class Expense:
    def __init__(self, amount=0.0, date=None):
        self.amount = amount
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def input_expense(self):
        while True:
            try:
                self.amount = float(input(f"Enter {self.__class__.__name__.lower()} expense: "))
                self.amount = round(self.amount, 2)
                break
            except ValueError:
                print("Invalid Input. Please enter a numeric value.")
        while True:
            user_date = input("Enter the date (YYYY-MM-DD) or leave blank for today: ") or self.date
            try:
                self.date = self.parse_date(user_date)
                break
            except ValueError as e:
                print(e)
        return self.amount, self.date

    def parse_date(self, date_string):
        try:
            parsed_date = parser.parse(date_string)
            return parsed_date.strftime("%Y-%m-%d")
        except ValueError:
            raise ValueError(
                "Invalid date format. Please enter a valid date in the correct format or leave blank for today's date"
            )

class Rent(Expense):
    pass

class PowerGas(Expense):
    pass

class WaterSewerTrash(Expense):
    pass

class Gasoline(Expense):
    pass

class CarInsurance(Expense):
    pass

class CarPayment(Expense):
    pass

class Phone(Expense):
    pass

class Internet(Expense):
    pass

class Groceries(Expense):
    pass

class Household(Expense):
    pass

class Hygiene(Expense):
    pass
