function magicSum(arr, targetSum) {
    for (let i = 0; i < arr.length; i++) {
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[i] + arr[j] !== targetSum) continue;

            console.log(`${arr[i]} ${arr[j]}`);
        }
    }
}