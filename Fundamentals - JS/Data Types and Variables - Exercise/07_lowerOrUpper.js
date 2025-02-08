function lowerOrUpper(char) {
    const charCode = char.charCodeAt(0);
    console.log(charCode >= 65 && charCode <= 90 ? "upper-case" : "lower-case");
}