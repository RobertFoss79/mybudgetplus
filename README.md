# Everyday Household Budget
#### Video Demo:  https://youtu.be/QWyWaeve0UI
#### Description:
I have never been happy with any app that I have tried for keeping track of my personal budgeting needs. They either don’t have the diversity of categories for income and expenses, or they are just so complicated that it is more of a headache than it is worth using. This project is a basic budgeting application with the categories that I want to see with the ease of use that anyone can figure out with very little explanation. This application allows users to enter their income and expenses, save this data to a file, and load it when needed. The application is implemented in Python and is designed to be user-friendly with interactive prompts from the command line. 
It will be a continual work in progress. I intend to add more categories and functionality to it. Eventually you will be able to see charts and graphs showing your income and expenses. I will learn the Tkinter library to create a gui to make it truly user friendly. And eventually I plan to learn Flask and Django and turn it into a web application. It will be a true friendly budgeting app for the everyday person.


## Files
- `project.py`: Main program file containing the main function and additional required functions.
- `income.py`: Contains functions for inputting income.
- `expenses.py`: Contains functions for inputting expenses.
- `utils.py`: Utility functions for saving and loading data.
- `test_project.py`: Contains tests for the functions in `project.py`.
- `requirements.txt`: Lists the required pip-installable libraries for the project.

## Usage
1. Run `project.py` to start the budgeting application.
2. Follow the prompts to enter income and expenses.
3. Save the data to a specified file.
4. Load existing data by providing the file path.

## Design Choices
- The application uses a simple command-line interface for ease of use.
- Data is saved in CSV format for compatibility with spreadsheet applications like Microsoft Excel.
- The project includes basic tests using `pytest` to ensure functionality.
