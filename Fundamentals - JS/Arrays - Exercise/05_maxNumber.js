function maxNumber(arr) {
    const topIntegers = [];
    for (let i = 0; i < arr.length; i++) {
        const number = arr[i];
        const restNumbers = arr.slice(i + 1, arr.length);
        const isNumberTheBiggest = number > Math.max(...restNumbers);
        if (!isNumberTheBiggest) continue;

        topIntegers.push(number);
    }

    console.log(topIntegers.join(" "));
}