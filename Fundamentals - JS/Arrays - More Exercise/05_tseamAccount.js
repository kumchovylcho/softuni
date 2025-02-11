function tseamAccount(arr) {
    const games = arr.shift().split(" ");
    for (let i = 0; i < arr.length; i++) {
        const [command, ...game] = arr[i].split(" ");
        if (command === "Play!") break;

        if (command === "Install" && !games.includes(...game)) games.push(...game);
        else if (command === "Uninstall" && games.includes(...game)) games.splice(games.indexOf(...game), 1);
        else if (command === "Update" && games.includes(...game)) {
            games.splice(games.indexOf(...game), 1);
            games.push(...game);
        } else if (command === "Expansion") {
            const [gameName, expansion] = game[0].split("-");
            if (!games.includes(gameName)) continue;

            games.splice(games.indexOf(gameName) + 1, 0, `${gameName}:${expansion}`);
        }
    }

    console.log(games.join(" "));
}