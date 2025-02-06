function login(arrPasswords) {
    const reverseString = (value) => {
        return value.split("").reverse().join("");
    }

    const username = arrPasswords.shift();
    let attempts = 0;
    const maxAttempts = 4;
    for (let i = 0; i < arrPasswords.length; i++) {
        attempts++;

        if (reverseString(arrPasswords[i]) === username) {
            console.log(`User ${username} logged in.`)
            break;
        }

        if (attempts === maxAttempts) {
            console.log(`User ${username} blocked!`);
            break;
        }

        console.log("Incorrect password. Try again.")
    }
}