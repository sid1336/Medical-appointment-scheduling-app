document.getElementById('uploadForm').addEventListener('submit', async function (e) {
    e.preventDefault();  // Prevent the default form submission

    const fileInput = document.getElementById('file');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    // Send the file to the server
    const response = await fetch('/upload', {
        method: 'POST',
        body: formData,
    });

    const result = await response.json();
    const resultDiv = document.getElementById('result');
    const summaryDiv = document.getElementById('summary');
    const cancelledCountSpan = document.getElementById('cancelledCount');
    const notCancelledCountSpan = document.getElementById('notCancelledCount');

    if (result.error) {
        resultDiv.innerHTML = `<div class="alert alert-danger">${result.error}</div>`;
    } else {
        // Count the cancelled and not cancelled predictions
        let cancelledCount = 0;
        let notCancelledCount = 0;

        result.comparison.forEach(row => {
            if (row.prediction === 'Cancelled') {
                cancelledCount++;
            } else {
                notCancelledCount++;
            }
        });

        // Update the summary section
        cancelledCountSpan.textContent = `Cancelled: ${cancelledCount}`;
        notCancelledCountSpan.textContent = `Not Cancelled: ${notCancelledCount}`;
        summaryDiv.classList.remove('d-none');

        // Display results in a table format
        let tableHTML = `
            <h3 class="text-center mt-4">Comparison Results</h3>
            <table class="table table-bordered table-striped mt-3">
                <thead class="table-dark">
                    <tr>
                        <th>Age</th>
                        <th>No Show</th>
                        <th>Days Between</th>
                        <th>Prediction</th>
                        <th>Recommendation</th>
                    </tr>
                </thead>
                <tbody>
        `;

        result.comparison.forEach(row => {
            const rowColor = row.prediction === 'Cancelled' ? 'table-danger' : 'table-success';
            tableHTML += `
                <tr class="${rowColor}">
                    <td>${row.age}</td>
                    <td>${row.previous_no_show}</td>
                    <td>${row.time_between_scheduling_and_appointment}</td>
                    <td>${row.prediction}</td>
                    <td>${row.recommendation}</td>
                </tr>
            `;
        });

        tableHTML += '</tbody></table>';
        resultDiv.innerHTML = tableHTML;
    }
});
