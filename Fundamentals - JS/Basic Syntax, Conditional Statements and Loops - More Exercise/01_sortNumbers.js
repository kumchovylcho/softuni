function sort(first, second, third) {
    let que = [first, second, third];
    while (que.length) {
        const biggest = Math.max(...que);
        que.splice(que.indexOf(biggest), 1);
        console.log(biggest);
    }
}