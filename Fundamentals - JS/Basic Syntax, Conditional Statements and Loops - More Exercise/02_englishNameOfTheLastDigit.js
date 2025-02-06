function englishNameOfTheLastDigit(number) {
    const numbers = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine"
    };
    const lastDigit = (number % 10).toString();
    console.log(numbers[lastDigit]);
}