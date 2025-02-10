function nonDecreasingSubset(arr) {
    let max = Number.NEGATIVE_INFINITY;

    console.log(arr.filter(val => {
        if (val >= max) {
            max = val;
            return true;
        }
        return false;
    }).join(" "));
}