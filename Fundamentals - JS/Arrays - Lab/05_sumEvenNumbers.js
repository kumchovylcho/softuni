function sumEvenNumbers(arr) {
    console.log(arr
                .map(number => Number(number))
                .filter(number => number % 2 === 0)
                .reduce((acc, number) => acc + number, 0)
    )
}