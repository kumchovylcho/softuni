function ages(age) {
    const categories = [
        [0, 2, "baby"],
        [3, 13, "child"],
        [14, 19, "teenager"],
        [20, 65, "adult"],
        [66, 11111111, "elder"]
    ];

    const category = categories.find(([min, max]) => age >= min && age <= max);
    console.log(category ? category[2] : "out of bounds");
}