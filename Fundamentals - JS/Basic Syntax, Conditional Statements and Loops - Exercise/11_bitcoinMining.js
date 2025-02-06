function bitcoinMining(golds) {
    let bitcoinPrice = 11949.16;
    let goldPrice = 67.51;

    let boughtBitcoins = 0;
    let moneyMade = 0;
    let boughtBitcoinDay = 0;

    for (let i = 0; i < golds.length; i++) {
        let goldCurrentDay = golds[i];

        if ((i + 1) % 3 === 0) {
            goldCurrentDay *= 0.7;
        }

        moneyMade += goldPrice * goldCurrentDay;
        while (moneyMade >= bitcoinPrice) {
            if (!boughtBitcoinDay) {
                boughtBitcoinDay = i + 1;
            }

            moneyMade -= bitcoinPrice;
            boughtBitcoins++;
        }
    }

    console.log(`Bought bitcoins: ${boughtBitcoins}`);
    if (boughtBitcoinDay) {
        console.log(`Day of the first purchased bitcoin: ${boughtBitcoinDay}`);
    }
    console.log(`Left money: ${moneyMade.toFixed(2)} lv.`);
}