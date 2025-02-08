function condenseArrayToNumber(numbers) {
    while (numbers.length > 1) {
        let condensed = [];
        for (let i = 0; i < numbers.length - 1; i++) {
            condensed[i] = numbers[i] + numbers[i + 1];
        }

        numbers = condensed;
    }

    console.log(numbers[0]);
}