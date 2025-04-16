import pytest  # Importing pytest for testing
import mybudgetplus  # Importing the main module for the budget application
import income  # Importing the income module
import expenses  # Importing the expenses module
import utils  # Importing the utility module for data saving/loading
import os  # Importing os module for file system interactions
from datetime import datetime  # Importing datetime to handle date and time operations

# Pytest fixture to provide sample data for testing
@pytest.fixture
def sample_data():
    # Returns a sample dictionary with income and expense data for testing
    return {
        'payroll_income': {'amount': 1000.0, 'date': '2024-12-17'},
        'other_income': {'amount': 200.0, 'date': '2024-12-17'},
        'rent': {'amount': 800.0, 'date': '2024-12-17'},
        'power': {'amount': 150.0, 'date': '2024-12-17'},
        'groceries': {'amount': 300.0, 'date': '2024-12-17'}
    }

# Test for collecting income inputs
def test_collect_income(monkeypatch):
    # First test case for payroll income
    inputs = iter(['1000', ''])  # Simulates user input for amount and default date
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))  # Overrides input calls
    payroll_income = income.PayrollIncome().input_income()  # Captures income data
    expected_date = datetime.now().strftime("%Y-%m-%d")  # Gets today's date in 'YYYY-MM-DD' format
    assert payroll_income == (1000.0, expected_date)  # Validates the input data

    # Second test case for other income
    inputs = iter(['200', ''])  # Simulates user input for amount and default date
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))  # Overrides input calls
    other_income = income.OtherIncome().input_income()  # Captures income data
    assert other_income == (200.0, expected_date)  # Validates the input data

# Test for collecting expense inputs
def test_collect_expenses(monkeypatch):
    # Test case for rent expense
    inputs = iter(['850.62', ''])  # Simulates user input for amount and default date
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))  # Overrides input calls
    rent_expense = expenses.Rent().input_expense()  # Captures expense data
    expected_date = datetime.now().strftime("%Y-%m-%d")  # Gets today's date in 'YYYY-MM-DD' format
    assert rent_expense == (850.62, expected_date)  # Validates the input data

    # Test case for phone expense
    inputs = iter(['63.54', ''])  # Simulates user input for amount and default date
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))  # Overrides input calls
    phone_expense = expenses.Phone().input_expense()  # Captures expense data
    assert phone_expense == (63.54, expected_date)  # Validates the input data

# Test for saving data to a file
def test_save_to_file(sample_data):
    filename = 'test_budget_data.csv'  # Specifies the test file name
    utils.save_to_file(sample_data, filename)  # Saves sample data to file
    
    assert os.path.exists(filename)  # Asserts that the file was created

    with open(filename, 'r') as file:  # Opens the file for reading
        content = file.read()  # Reads file content
        assert 'payroll_income,1000.0' in content  # Checks for specific data in the file
        assert 'rent,800.0' in content  # Checks for specific data in the file

    os.remove(filename)  # Deletes the test file after the test

# Test for loading data from a file
def test_load_from_file(sample_data):
    filename = 'test_budget_data.csv'  # Specifies the test file name
    utils.save_to_file(sample_data, filename)  # Saves sample data to file
    
    loaded_data = utils.load_from_file(filename)  # Loads data back from the file
    
    assert loaded_data == sample_data  # Asserts that loaded data matches the sample data
    
    os.remove(filename)  # Deletes the test file after the test
