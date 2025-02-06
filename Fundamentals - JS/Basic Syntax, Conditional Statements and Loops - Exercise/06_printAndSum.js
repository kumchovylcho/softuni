function printAndSum(from, to) {
    const createRange = () => Array.from({length: to - from + 1}, (_, i) => from + i)

    const numbers = createRange()
    console.log(numbers.join(" "));
    console.log(`Sum: ${numbers.reduce(
        (acc, current) => acc + current, 0)
    }`);
}