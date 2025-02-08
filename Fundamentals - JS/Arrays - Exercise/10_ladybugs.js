function ladybugs(input) {
    let fieldSize = Number(input[0]);
    let ladybugsIndexes = input[1].split(" ").map(Number);
    let field = new Array(fieldSize).fill(0);

    for (let index of ladybugsIndexes) {
        if (index >= 0 && index < fieldSize) {
            field[index] = 1;
        }
    }

    for (let i = 2; i < input.length; i++) {
        let [startIndex, direction, flyLength] = input[i].split(" ");
        startIndex = Number(startIndex);
        flyLength = Number(flyLength);

        if (startIndex < 0 || startIndex >= fieldSize || field[startIndex] !== 1) continue;

        field[startIndex] = 0;

        let position = startIndex;
        let step = direction === "right" ? flyLength : -flyLength;
        while (position >= 0 && position < fieldSize) {
            position += step;

            if (position >= 0 && position < fieldSize && field[position] === 0) {
                field[position] = 1;
                break;
            }
        }
    }

    console.log(field.join(" "));
}