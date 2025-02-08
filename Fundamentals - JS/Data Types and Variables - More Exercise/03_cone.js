function cone(radius, height) {
    let slant = Math.sqrt(radius ** 2 + height ** 2);
    let volume = (Math.PI * radius ** 2 * height) / 3;
    let area = Math.PI * radius * (radius + slant);

    console.log(`volume = ${volume.toFixed(4)}`);
    console.log(`area = ${area.toFixed(4)}`);
}