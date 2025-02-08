function commonElements(arr1, arr2) {
    arr1.forEach(element => {
        if (arr2.includes(element)) {
            console.log(element);
        }
    });
}