function theatrePromotions(day, personAge) {
    const prices = {
        "Weekday": { child: "12$", adult: "18$", senior: "12$" },
        "Weekend": { child: "15$", adult: "20$", senior: "15$" },
        "Holiday": { child: "5$", adult: "12$", senior: "10$" }
    };

    let personAgeInTerms = "";
    if (personAge >= 0 && personAge <= 18) personAgeInTerms = "child";
    else if (personAge > 18 && personAge <= 64) personAgeInTerms = "adult";
    else if (personAge > 64 && personAge <= 122) personAgeInTerms = "senior";

    console.log(personAgeInTerms ? prices[day][personAgeInTerms] : "Error!");
}