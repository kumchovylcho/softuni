function dungeonestDark(rooms) {
    let health = 100;
    let coins = 0;

    const roomsArr = rooms.split("|");
    for (let i = 0; i < roomsArr.length; i++) {
        const [enemy, number] = roomsArr[i].split(" ");
        if (enemy === "potion") {
            let previousHealth = health;
            health = Math.min(100, health + Number(number));
            console.log(`You healed for ${health - previousHealth} hp.`);
            console.log(`Current health: ${health} hp.`);
        } else if (enemy === "chest") {
            coins += Number(number);
            console.log(`You found ${number} coins.`);
        } else {
            health -= Number(number);
            if (health > 0) {
                console.log(`You slayed ${enemy}.`)
            } else {
                console.log(`You died! Killed by ${enemy}.`);
                console.log(`Best room: ${i + 1}`)
                break;
            }
        }
    }

    if (health > 0) {
        console.log("You've made it!");
        console.log(`Coins: ${coins}`);
        console.log(`Health: ${health}`);
    }
}