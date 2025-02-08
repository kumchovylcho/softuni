function arrayRotation(arr, rotations) {
    for (let i = 0; i < rotations; i++) arr.push(arr.shift());
    console.log(arr.join(" "));
}