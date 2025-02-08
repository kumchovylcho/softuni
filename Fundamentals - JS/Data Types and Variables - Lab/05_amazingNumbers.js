function amazingNumbers(number) {
    number = number.toString();
    let sum = 0;
    for (let i = 0; i < number.length; i++) sum += Number(number[i]);
    const isAmazing = sum.toString().includes("9") ? "True" : "False";
    console.log(`${number} Amazing? ${isAmazing}`);
}