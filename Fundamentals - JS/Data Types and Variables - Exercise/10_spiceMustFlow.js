function spiceFlow(startYield) {
    let sourceExtracted = 0;
    let daysMined = 0;
    while (startYield >= 100) {
        daysMined++;
        sourceExtracted += startYield - 26;
        startYield -= 10;
    }

    if (sourceExtracted >= 26) {
        sourceExtracted -= 26;
    }

    console.log(daysMined);
    console.log(sourceExtracted);
}