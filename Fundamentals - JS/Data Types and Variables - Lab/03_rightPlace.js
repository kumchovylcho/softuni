function rightPlace(string, char, originalString) {
    console.log(string.replace("_", char) === originalString ? "Matched" : "Not Matched");
}