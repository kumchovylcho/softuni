function foreignLanguage(country) {
    let language = "unknown";
    if (["England", "USA"].includes(country)) {
        language = "English";
    } else if (["Spain", "Argentina", "Mexico"].includes(country)) {
        language = "Spanish";
    }

    console.log(language);
}