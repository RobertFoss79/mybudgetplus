import pytest
import project
import income
import expenses
import utils
import os
from datetime import datetime

@pytest.fixture
def sample_data():
    return {
        'payroll_income': {'amount': 1000.0, 'date': '2024-12-17'},
        'other_income': {'amount': 200.0, 'date': '2024-12-17'},
        'rent': {'amount': 800.0, 'date': '2024-12-17'},
        'power_gas': {'amount': 150.0, 'date': '2024-12-17'},
        'groceries': {'amount': 300.0, 'date': '2024-12-17'}
    }
def test_collect_income(monkeypatch):
    inputs = iter(['1000', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    payroll_income = income.PayrollIncome().input_income()
    expected_date = datetime.now().strftime("%Y-%m-%d")
    assert payroll_income == (1000.0, expected_date)

    inputs = iter(['200', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    other_income = income.OtherIncome().input_income()
    assert other_income == (200.0, expected_date)

def test_collect_expenses(monkeypatch):
    inputs = iter(['850.62', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    rent_expense = expenses.RentExpense().input_expense()
    expected_date = datetime.now().strftime("%Y-%m-%d")
    assert rent_expense == (850.62, expected_date)

    inputs = iter(['63.54', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    phone_expense = expenses.PhoneExpense().input_expense()
    assert phone_expense == (63.54, expected_date)

def test_save_to_file(sample_data):
    filename = 'test_budget_data.csv'
    utils.save_to_file(sample_data, filename)
    
    assert os.path.exists(filename)

    with open(filename, 'r') as file:
        content = file.read()
        assert 'payroll_income,1000.0' in content
        assert 'rent,800.0' in content

    os.remove(filename)

def test_load_from_file(sample_data):
    filename = 'test_budget_data.csv'
    utils.save_to_file(sample_data, filename)
    
    loaded_data = utils.load_from_file(filename)
    
    assert loaded_data == sample_data
    
    os.remove(filename)
