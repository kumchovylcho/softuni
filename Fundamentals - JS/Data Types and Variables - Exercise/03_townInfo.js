function townInfo(town, population, area) {
    let errors = [];
    if (town.length < 3) {
        errors.push("Town name must be at least 3 characters!");
    }

    for (const [item, description] of [[population, "Population"], [area, "Area"]]) {
        if (item < 0) errors.push(`${description} must be a positive number!`);
    }

    if (errors.length) {
        console.log(errors.join("\n"));
        return;
    }

    console.log(`Town ${town} has population of ${population} and area ${area} square km.`);
}