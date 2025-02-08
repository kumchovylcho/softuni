function sumDigits(number) {
    let sum = 0;
    while (number > 0) {
        sum += Math.floor(number % 10);
        number /= 10;
    }

    console.log(sum);
}