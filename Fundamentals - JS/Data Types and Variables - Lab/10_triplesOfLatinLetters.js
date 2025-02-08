function triplesOfLatinLetters(numberAsString) {
    const from = 97;
    const to = from + Number(numberAsString);

    for (let i = from; i < to; i++) {
        for (let j = from; j < to; j++) {
            for (let k = from; k < to; k++) {
                console.log(`${String.fromCharCode(i)}${String.fromCharCode(j)}${String.fromCharCode(k)}`);
            }
        }
    }
}