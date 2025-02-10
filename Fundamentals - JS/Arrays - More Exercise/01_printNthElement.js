function printNthElement(arr) {
    const step = Number(arr.pop());
    console.log(arr.filter((_, index) => index % step === 0).join(" "));
}