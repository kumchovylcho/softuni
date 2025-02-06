function leapYear(year) {
    if (year % 100 === 0 && year % 400 !== 0) {
        console.log("no");
        return;
    }

    if (year % 4 !== 0) {
        console.log("no");
        return;
    }

    console.log("yes");
}