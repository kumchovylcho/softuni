function addAndSubtract(arr) {
    const sumOriginalArr = arr.reduce((acc, curr) => acc + curr, 0);
    const modifiedArr = arr.map((number, index) => {
        if (number % 2 === 0)
            return number + index;
        return number - index;
    });
    const sumModifiedArr = modifiedArr.reduce((acc, curr) => acc + curr, 0);
    console.log(modifiedArr);
    console.log(sumOriginalArr);
    console.log(sumModifiedArr);
}