function mergeArrays(arr, arr2) {
    console.log(arr
        .map((value, i) => {
            if (i % 2 === 0) {
                return Number(value) + Number(arr2[i]);
            }

            return `${value}${arr2[i]}`;
        })
        .join(" - ")
    );
}