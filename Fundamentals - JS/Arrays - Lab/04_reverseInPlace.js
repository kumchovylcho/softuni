function reverseInPlace(arr) {
    const swapElements = (arr, i, j) => {
        [arr[j], arr[i]] = [arr[i], arr[j]];
    }

    const arrLength = arr.length;
    for (let i = 0; i < arrLength / 2; i++) {
        swapElements(arr, i, arrLength - 1 - i);
    }

    console.log(arr.join(" "));
}