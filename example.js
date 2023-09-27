console.log('hello world')

async function sum_5_2() {
    const response1 = fetch("http://localhost:5000/add?num1=5&num2=2");
    const result1 = await response1
    const sum1 = await result1.json();
    document.body.innerHTML = "<h1>5 + 2 = " + sum1 + "</h1>"
  }

sum_5_2()