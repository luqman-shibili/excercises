function fibonacciOutput() {
    const n = parseInt(document.getElementById('numInput').value);
    let a = 0, b = 1, fibonacciSequence = [];

    for (let i = 0; i < n; i++) {
        fibonacciSequence.push(a);
        let temp = a;
        a = b;
        b = temp + b;
    }

    document.getElementById('output').textContent = fibonacciSequence.join(', ');
}


function generateTable() {
    const n = document.getElementById('numberInput').value;
    const tableBody = document.querySelector('#numbersTable tbody');
    tableBody.innerHTML = ''; // Clear any existing rows

    for (let i = 1; i <= n; i++) {
        const row = document.createElement('tr');
        const numberCell = document.createElement('td');
        const squareCell = document.createElement('td');

        numberCell.textContent = i;
        squareCell.textContent = i * i;

        row.appendChild(numberCell);
        row.appendChild(squareCell);

        tableBody.appendChild(row);
    }
}

window.onload = generateTable;