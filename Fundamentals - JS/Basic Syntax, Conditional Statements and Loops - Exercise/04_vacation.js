function vacation(groupNumber, groupType, dayOfWeek) {
    const prices = {
        "Students": {"Friday": 8.45, "Saturday": 9.8, "Sunday": 10.46},
        "Business": {"Friday": 10.9, "Saturday": 15.6, "Sunday": 16},
        "Regular": {"Friday": 15, "Saturday": 20, "Sunday": 22.5}
    };

    let total = groupNumber * prices[groupType][dayOfWeek];
    if (groupType === "Students" && groupNumber >= 30) {
        total *= 0.85;
    } else if (groupType === "Business" && groupNumber >= 100) {
        total -= 10 * prices[groupType][dayOfWeek];
    } else if (groupType === "Regular" && (groupNumber >= 10 && groupNumber <= 20)) {
        total *= 0.95;
    }

    console.log(`Total price: ${total.toFixed(2)}`);
}