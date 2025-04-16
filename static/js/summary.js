// Wait until the DOM content is fully loaded
document.addEventListener("DOMContentLoaded", () => {
    // Retrieve the selected time period from localStorage
    const selectedTimePeriod = localStorage.getItem("selectedTimePeriod");
    const summarySection = document.getElementById("filtered-summary");

    // If no time period is selected, show an error message
    if (!selectedTimePeriod) {
        summarySection.innerHTML = "<p>No time period selected. Please return to the main page and choose one.</p>";
        return; // Stop further execution if no time period is selected
    }

    // Fetch and display the summary data for the selected time period
    fetchSummary(selectedTimePeriod);

    /**
     * Function to fetch and display summary data from the backend.
     * @param {string} timePeriod - The selected time period (e.g., 'weekly', 'monthly', 'annual').
     */
    function fetchSummary(timePeriod) {
        // Fetch income data for the selected time period
        fetch(`http://127.0.0.1:5000/get_summary?table=income&time_period=${timePeriod}`)
            .then(response => response.json()) // Parse JSON response from the server
            .then(data => {
                if (data.error) {
                    console.error(data.error); // Log any errors returned by the backend
                    summarySection.innerHTML = `<p>Error: ${data.error}</p>`;
                    return; // Stop execution if an error occurs
                }

                // Add an income summary heading
                summarySection.innerHTML = `<h2>${capitalizeFirstLetter(timePeriod)} Income Summary</h2>`;

                // Check if there's any income data
                if (data.data.length === 0) {
                    summarySection.innerHTML += "<p>No income data for this time period.</p>";
                } else {
                    // Iterate through income data and display each entry
                    data.data.forEach(row => {
                        const item = document.createElement("p");
                        item.textContent = `${row[0]}: $${row[1].toFixed(2)} on ${row[2]}`;
                        summarySection.appendChild(item);
                    });
                }

                // Fetch expense data for the same time period
                return fetch(`http://127.0.0.1:5000/get_summary?table=expenses&time_period=${timePeriod}`);
            })
            .then(response => response.json()) // Parse JSON response for expenses
            .then(data => {
                if (data.error) {
                    console.error(data.error); // Log any errors returned by the backend
                    summarySection.innerHTML += `<p>Error: ${data.error}</p>`;
                    return; // Stop execution if an error occurs
                }

                // Add an expense summary heading
                summarySection.innerHTML += `<h2>${capitalizeFirstLetter(timePeriod)} Expenses Summary</h2>`;

                // Check if there's any expense data
                if (data.data.length === 0) {
                    summarySection.innerHTML += "<p>No expenses data for this time period.</p>";
                } else {
                    // Iterate through expense data and display each entry
                    data.data.forEach(row => {
                        const item = document.createElement("p");
                        item.textContent = `${row[0]}: $${row[1].toFixed(2)} on ${row[2]}`;
                        summarySection.appendChild(item);
                    });
                }
            })
            .catch(error => {
                console.error('Error fetching summary data:', error); // Log any fetch errors
                summarySection.innerHTML = `<p>Error fetching data. Please try again later.</p>`;
            });
    }

    /**
     * Helper function to capitalize the first letter of a string.
     * @param {string} string - The string to be capitalized.
     * @returns {string} - The string with the first letter capitalized.
     */
    function capitalizeFirstLetter(string) {
        return string.charAt(0).toUpperCase() + string.slice(1); // Capitalize the first letter
    }
});
