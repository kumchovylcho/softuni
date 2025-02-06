function triangleOfNumbers(rows) {
    for (let i = 1; i <= rows; i++) {
        let currRow = [];
        for (let j = 1; j <= i; j++) {
            currRow.push(i);
        }

        console.log(currRow.join(" "));
    }
}