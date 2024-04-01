function searchActor() {
    const actorName = document.getElementById('actorName').value;

    fetch(`/search?actor=${encodeURIComponent(actorName)}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            displayResults(data);
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error.message);
        });
}

function displayResults(data) {
    const resultsTable = document.getElementById('resultsTable').getElementsByTagName('tbody')[0];
    resultsTable.innerHTML = '';  // Clear previous results

    const invalidString = document.getElementById('invalidString');
    invalidString.innerHTML = '';

    if (Object.keys(data).length === 0 && data.constructor === Object) {
        console.log("JSON object is empty.");
        invalidString.innerHTML = "No results found!";
    } else {
        for (const [movie, roles] of Object.entries(data)) {
            const row = resultsTable.insertRow();
            const cell1 = row.insertCell(0);
            const cell2 = row.insertCell(1);

            cell1.textContent = movie;
            cell2.textContent = roles.join(', ');
        }
    }
}
