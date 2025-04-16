from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import datetime

# Initialize the Flask app
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS)

# Path to the SQLite database file
DB_PATH = "./budget.db"

# Route to save income data
@app.route('/save_income', methods=['POST'])
def save_income():
    data = request.json  # Get JSON data from the request
    type = data.get('type')  # Income type (e.g., salary, freelance)
    amount = data.get('amount')  # Income amount
    date = data.get('date')  # Date of income

    # Connect to the database and insert income data
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO income (type, amount, date)
        VALUES (?, ?, ?);
    """, (type, amount, date))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Income saved successfully!'})

# Route to save expense data
@app.route('/save_expense', methods=['POST'])
def save_expense():
    data = request.json  # Get JSON data from the request
    type = data.get('type')  # Expense type (e.g., rent, groceries)
    amount = data.get('amount')  # Expense amount
    date = data.get('date')  # Date of expense

    # Connect to the database and insert expense data
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO expenses (type, amount, date)
        VALUES (?, ?, ?);
    """, (type, amount, date))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Expense saved successfully!'})

# Route to retrieve all data from a table
@app.route('/get_data', methods=['GET'])
def get_data():
    table = request.args.get('table')  # 'income' or 'expenses'

    if table not in ['income', 'expenses']:
        return jsonify({'error': 'Invalid table name'}), 400

    # Connect to the database and retrieve all data
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"SELECT type, amount, date FROM {table};")
    rows = cursor.fetchall()
    conn.close()

    # Return the data as JSON
    return jsonify({'data': rows})

# Route to retrieve filtered summaries based on time periods
@app.route('/get_summary', methods=['GET'])
def get_summary():
    table = request.args.get('table')  # 'income' or 'expenses'
    time_period = request.args.get('time_period')  # 'weekly', 'monthly', or 'annual'

    if table not in ['income', 'expenses']:
        return jsonify({'error': 'Invalid table name'}), 400

    # Determine the start date based on the time period
    now = datetime.datetime.now()
    if time_period == 'weekly':
        start_date = now - datetime.timedelta(days=7)
    elif time_period == 'monthly':
        start_date = now - datetime.timedelta(days=30)
    elif time_period == 'annual':
        start_date = now - datetime.timedelta(days=365)
    else:
        return jsonify({'error': 'Invalid time period'}), 400

    # Connect to the database and fetch filtered data
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT type, amount, date FROM {table}
        WHERE date >= ?;
    """, (start_date.strftime('%Y-%m-%d'),))
    rows = cursor.fetchall()
    conn.close()

    # Return filtered data as JSON
    return jsonify({'data': rows})

# Main entry point to run the Flask server
if __name__ == '__main__':
    app.run(debug=True)
