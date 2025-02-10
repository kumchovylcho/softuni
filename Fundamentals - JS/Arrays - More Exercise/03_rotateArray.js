function rotateArray(arr) {
    let rotations = Number(arr.pop());
    while (rotations) {
        arr.unshift(arr.pop());
        rotations--;
    }

    console.log(arr.join(" "));
}