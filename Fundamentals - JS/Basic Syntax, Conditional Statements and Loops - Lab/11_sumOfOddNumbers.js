function sumOfOddNumbers(oddNumbersAmount) {
    let total = 0;
    let iterations = 0;
    let startOddNumber = 1;
    while (iterations < oddNumbersAmount) {
        console.log(startOddNumber);
        total += startOddNumber;
        startOddNumber += 2;
        iterations++;
    }

    console.log(`Sum: ${total}`);
}