fetch('https://google.com')
.then(response => response.json())
.then(json => console.log(json))