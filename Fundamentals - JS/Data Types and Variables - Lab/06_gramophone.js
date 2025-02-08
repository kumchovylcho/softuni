function gramophone(band, album, song) {
    const songDuration = (album.length * band.length) * song.length / 2;
    const oneRotation = 2.5;
    const totalRotations = Math.ceil(songDuration / oneRotation);
    console.log(`The plate was rotated ${totalRotations} times.`)
}