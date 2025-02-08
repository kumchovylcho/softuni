function evenAndOddSubtraction(arr) {
    const sumOfEven = arr
        .filter(number => number % 2 === 0)
        .reduce((acc, curr) => acc + curr, 0);

    const sumOfOdd = arr
        .filter(number => number % 2 !== 0)
        .reduce((acc, curr) => acc + curr, 0);

    console.log(sumOfEven - sumOfOdd);
}