// Wait until the DOM content is fully loaded before executing scripts
document.addEventListener("DOMContentLoaded", () => {
    // DOM elements for income inputs and buttons
    const incomeForm = document.getElementById("income-form");
    const addIncomeButton = document.getElementById("add-income");

    // DOM elements for expense inputs and buttons
    const expenseForm = document.getElementById("expense-form");
    const addExpenseButton = document.getElementById("add-expense");

    // DOM elements for summary section
    const totalIncomeDisplay = document.getElementById("total-income");
    const totalExpensesDisplay = document.getElementById("total-expenses");
    const netBalanceDisplay = document.getElementById("net-balance");

    // Buttons for viewing summaries by time periods
    const viewWeeklyButton = document.getElementById("view-weekly");
    const viewMonthlyButton = document.getElementById("view-monthly");
    const viewAnnualButton = document.getElementById("view-annual");

    // Function to update totals in the summary section
    function updateSummary(table) {
        fetch(`http://127.0.0.1:5000/get_data?table=${table}`)
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    console.error(data.error);
                    return;
                }

                // Calculate totals
                let total = data.data.reduce((sum, item) => sum + item[1], 0);

                // Update HTML elements
                if (table === 'income') {
                    totalIncomeDisplay.textContent = `$${total.toFixed(2)}`;
                } else if (table === 'expenses') {
                    totalExpensesDisplay.textContent = `$${total.toFixed(2)}`;
                }

                // Calculate and update net balance
                const netBalance = parseFloat(totalIncomeDisplay.textContent.replace('$', '')) -
                                   parseFloat(totalExpensesDisplay.textContent.replace('$', ''));
                netBalanceDisplay.textContent = `$${netBalance.toFixed(2)}`;
            })
            .catch(error => console.error('Error fetching data:', error));
    }

    // Function to send income data to the backend
    function sendIncomeToBackend(type, amount, date) {
        fetch('http://127.0.0.1:5000/save_income', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ type, amount, date }) // Send data as JSON
        })
        .then(response => response.json())
        .then(data => {
            console.log(data.message); // Confirm success
            // alert(data.message);
            updateSummary('income'); // Refresh income totals
        })
        .catch(error => console.error('Error saving income:', error));
    }

    // Function to send expense data to the backend
    function sendExpenseToBackend(type, amount, date) {
        fetch('http://127.0.0.1:5000/save_expense', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ type, amount, date }) // Send data as JSON
        })
        .then(response => response.json())
        .then(data => {
            console.log(data.message); // Confirm success
            alert(data.message);
            updateSummary('expenses'); // Refresh expense totals
        })
        .catch(error => console.error('Error saving expense:', error));
    }

    // Function to navigate to the summary page for a specific time period
    function navigateToSummary(timePeriod) {
        localStorage.setItem("selectedTimePeriod", timePeriod); // Save the selected time period
        window.location.href = "summary.html"; // Redirect to the summary page
    }

    // Event listeners for "Add Income" and "Add Expense" buttons
    addIncomeButton.addEventListener("click", () => {
        const type = document.getElementById("income-type").value;
        const amount = parseFloat(document.getElementById("income-amount").value);
        const date = document.getElementById("income-date").value || new Date().toISOString().split("T")[0];

        if (isNaN(amount) || amount <= 0) {
            alert("Please enter a valid income amount.");
            return;
        }

        sendIncomeToBackend(type, amount, date);
        incomeForm.reset(); // Clear form fields
    });

    addExpenseButton.addEventListener("click", () => {
        const type = document.getElementById("expense-type").value;
        const amount = parseFloat(document.getElementById("expense-amount").value);
        const date = document.getElementById("expense-date").value || new Date().toISOString().split("T")[0];

        if (isNaN(amount) || amount <= 0) {
            alert("Please enter a valid expense amount.");
            return;
        }

        sendExpenseToBackend(type, amount, date);
        expenseForm.reset(); // Clear form fields
    });

    // Event listeners for time period summary buttons
    viewWeeklyButton.addEventListener("click", () => navigateToSummary("weekly"));
    viewMonthlyButton.addEventListener("click", () => navigateToSummary("monthly"));
    viewAnnualButton.addEventListener("click", () => navigateToSummary("annual"));

    // Initial load to display totals
    updateSummary('income');
    updateSummary('expenses');
});
