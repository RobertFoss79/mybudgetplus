from django.db import models

# Income Model
class Income(models.Model):
    type = models.CharField(max_length=100)  # Type of income (e.g., 'Payroll', 'Other')
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Income amount
    date = models.DateField()  # Date of income

    def __str__(self):
        # String representation for debugging/admin interface
        return f"{self.type}: ${self.amount} on {self.date}"

# Expense Model
class Expense(models.Model):
    type = models.CharField(max_length=100)  # Type of expense (e.g., 'Rent', 'Phone', 'Groceries')
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Expense amount
    date = models.DateField()  # Date of expense

    def __str__(self):
        # String representation for debugging/admin interface
        return f"{self.type}: ${self.amount} on {self.date}"
