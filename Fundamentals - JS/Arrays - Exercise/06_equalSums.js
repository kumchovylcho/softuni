function equalSums(arr) {
    const getSum = (from, to) => arr.slice(from, to).reduce((acc, curr) => acc + curr, 0);

    let output = "no";
    for (let i = 0; i < arr.length; i++) {
        let leftSum = getSum(0, i + 1);
        let rightSum = getSum(i, arr.length);

        if (leftSum === rightSum) {
            output = i;
            break;
        }
    }

    console.log(output);
}