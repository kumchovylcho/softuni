function gladiatorExpenses(lostFights, helmetPrice, swordPrice, shieldPrice, armorPrice) {
    let brokenShields = 0;
    let expenses = 0;

    for (let i = 1; i <= lostFights; i++) {
        if (!(i % 2)) {
            expenses += helmetPrice;
        }

        if (!(i % 3)) {
            expenses += swordPrice;
        }

        if (!(i % 2) && !(i % 3)) {
            expenses += shieldPrice;
            brokenShields++;

            if (!(brokenShields % 2)) {
                expenses += armorPrice;
            }
        }
    }

    console.log(`Gladiator expenses: ${expenses.toFixed(2)} aureus`);
}