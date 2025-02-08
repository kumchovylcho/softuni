function equalArrays(arr, arr2) {
    const isSameArray = () => {
        for (let i = 0; i < arr.length; i++) {
            if (arr[i] !== arr2[i]) return [false, i];
        }

        return [true, 0];
    }

    const [isSame, index] = isSameArray();
    if (isSame) {
        const sum = arr.map(Number).reduce((acc, curr) => acc + curr, 0);
        console.log(`Arrays are identical. Sum: ${sum}`)
    } else {
        console.log(`Arrays are not identical. Found difference at ${index} index`)
    }
}