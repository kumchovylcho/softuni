function maxSequenceOfEqualElements(arr) {
    let output = [];
    for (let i = 0; i < arr.length; i++) {

        const currentNumbers = [arr[i]];
        for (let j = i + 1; j < arr.length; j++) {
            if (!currentNumbers.every(number => number === arr[j])) {
                if (output.length < currentNumbers.length) {
                    output = currentNumbers;
                }
                break;
            }

            currentNumbers.push(arr[j]);
        }

        if (output.length < currentNumbers.length) {
            output = currentNumbers;
        }
    }

    console.log(output.join(" "));
}