function dayOfWeek(dayOfWeekAsNumber) {
    const days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
    if (dayOfWeekAsNumber >= 1 && dayOfWeekAsNumber <= 7) {
        console.log(days[dayOfWeekAsNumber - 1]);
    } else {
        console.log("Invalid day!");
    }
}