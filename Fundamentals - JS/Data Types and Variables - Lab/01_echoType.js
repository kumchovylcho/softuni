function echoType(value) {
    const type = typeof value;
    if (!["string", "number"].includes(type)) {
        console.log(type);
        console.log("Parameter is not suitable for printing");
        return;
    }

    console.log(type);
    console.log(value);
}