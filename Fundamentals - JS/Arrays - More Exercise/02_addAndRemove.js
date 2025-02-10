function addAndRemove(arr) {
    let initialNumber = 1;
    const output = [];

    for (const command of arr) {
        if (command === "add") {
            output.push(initialNumber);
        } else if (command === "remove") {
            output.pop();
        }

        initialNumber++;
    }

    console.log(output.length ? output.join(" ") : "Empty");
}