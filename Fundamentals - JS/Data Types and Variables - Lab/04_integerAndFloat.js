function integerAndFloat(number, number1, number2) {
    const sum = [number, number1, number2].reduce((acc, curr) => acc + curr, 0);
    console.log(`${sum} - ${sum % 1 ? "Float" : "Integer"}`);
}