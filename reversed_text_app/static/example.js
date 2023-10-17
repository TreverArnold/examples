document.getElementById('textForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var inputText = document.getElementById('inputText').value;

    fetch('/reverse', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: inputText })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('output').innerText = 'Reversed Text: ' + data.reversed_text;
    });
});
