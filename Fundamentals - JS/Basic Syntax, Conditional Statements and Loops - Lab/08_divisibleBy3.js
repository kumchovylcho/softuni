function divisibleByThree() {
    for (let i = 1; i < 101; i++) {
        if (i % 3 !== 0) continue;

        console.log(i);
    }
}