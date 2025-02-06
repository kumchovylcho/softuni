function rounding(numberToRound, precision) {
    precision = Math.min(precision, 15);
    console.log(parseFloat(numberToRound.toFixed(precision)));
}