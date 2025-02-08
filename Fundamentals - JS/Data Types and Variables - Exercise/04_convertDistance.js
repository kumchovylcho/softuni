function convertDistance(meters) {
    const kmToMiles = 0.621371;
    const metersToKms = meters / 1000;
    const milesFromKms = metersToKms * kmToMiles;
    console.log(`${meters} meters is equal to ${metersToKms} kilometers.`);
    console.log(`${metersToKms} kilometers is equal to ${milesFromKms.toFixed(2)} miles.`);
}