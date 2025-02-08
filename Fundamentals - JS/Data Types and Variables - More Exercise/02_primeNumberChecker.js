function isPrime(number) {
    if (number < 2) return false;

    let prime = true;
    for (let i = 2; i < number; i++) {
        if (number % i === 0) {
            prime = false;
            break;
        }
    }

    return prime;
}