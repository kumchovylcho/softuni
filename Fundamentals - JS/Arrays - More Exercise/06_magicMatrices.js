function magicMatrices(matrix) {
    const sumRow = (row) => row.reduce((acc, curr) => acc + curr, 0);

    const sumCol = (colIndex) => {
        let sum = 0;
        for (let row = 0; row < matrix.length; row++) {
            sum += matrix[row][colIndex];
        }
        return sum;
    };


    const targetSum = sumRow(matrix[0]);
    for (let i = 0; i < matrix.length; i++) {
        if (sumRow(matrix[i]) !== targetSum || sumCol(i) !== targetSum) {
            return false;
        }
    }

    return true;
}