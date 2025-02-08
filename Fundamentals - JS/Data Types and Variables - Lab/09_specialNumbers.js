function specialNumbers(n) {
    const isSpecial = (number) => {
        const asString = number.toString();
        let sum = 0;
        for (let i = 0; i < asString.length; i++) sum += Number(asString[i]);
        return sum === 5 || sum === 7 || sum === 11;
    }

    for (let i = 1; i <= n; i++) console.log(`${i} -> ${isSpecial(i) ? "True" : "False"}`);
}