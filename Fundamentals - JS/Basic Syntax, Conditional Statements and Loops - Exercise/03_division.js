function division(number) {
    const tryDivisions = [10, 7, 6, 3, 2];
    let canDivide = false;
    for (const division of tryDivisions) {
        if (number % division === 0) {
            canDivide = true;
            console.log(`The number is divisible by ${division}`);
            break;
        }
    }

    if (!canDivide) console.log("Not divisible");
}