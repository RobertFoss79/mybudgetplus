from datetime import datetime
from dateutil import parser

class Income:
    def __init__(self, amount=0.0, date=None):
        self.amount = amount
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def input_income(self):
        while True:
            try:
                self.amount = float(
                    input(f"Enter {self.__class__.__name__.lower()} income: ")
                )
                self.amount = round(self.amount, 2)
                break
            except ValueError:
                print("Invalid Input. Please enter a numeric value.")
        while True:
            user_date = (
                input("Enter the date (YYYY-MM-DD) or leave blank for today: ")
                or self.date
            )
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


class PayrollIncome(Income):
    pass

class OtherIncome(Income):
    pass