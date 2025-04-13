// const readline = require('readline');

// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });

// // Function to perform arithmetic operations
// function calculateOperations(num1, num2) {
//     // Check if inputs are valid numbers
//     if (isNaN(num1) || isNaN(num2)) {
//         console.log("Please enter valid numbers");
//         rl.close();
//         return;
//     }
    
//     // Perform calculations
//     let addition = num1 + num2;
//     let multiplication = num1 * num2;
//     let division = num2 !== 0 ? (num1 / num2).toFixed(2) : "Cannot divide by zero";
//     let remainder = num2 !== 0 ? num1 % num2 : "Cannot divide by zero";
    
//     // Display results
//     console.log("Addition:", addition);
//     console.log("Multiplication:", multiplication);
//     console.log("Division:", division);
//     console.log("Remainder:", remainder);
    
//     rl.close();
// }

// // Get user input
// rl.question("Enter first number: ", (input1) => {
//     rl.question("Enter second number: ", (input2) => {
//         let num1 = parseFloat(input1);
//         let num2 = parseFloat(input2);
//         calculateOperations(num1, num2);
//     });
// });






// Function to generate number sequence from 100 to 150
function generateSequence(start, end) {
    let sequence = "";
    for (let i = start; i <= end; i++) {
        sequence += i + (i < end ? " " : "");
    }
    return sequence;
}

// Display the sequence
console.log(generateSequence(100, 150));
