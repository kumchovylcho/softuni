function chessBoard(children) {
    const getIndentation = (indent) => " ".repeat(indent);
    const indent = (text, indent) => `${getIndentation(indent)}${text}`;

    const container = ['<div class="chessboard">'];
    for (let i = 0; i < children; i++) {
        container.push(indent("<div>", 2));
        let useBlackClass = !(i % 2);
        for (let j = 0; j < children; j++) {
            container.push(
                indent(
                    `<span class="${useBlackClass ? "black" : "white"}"></span>`,
                    4
                )
            );

            useBlackClass = !useBlackClass;
        }

        container.push(indent("</div>", 2));
    }

    container.push('</div>');
    return container.join("\n");
}