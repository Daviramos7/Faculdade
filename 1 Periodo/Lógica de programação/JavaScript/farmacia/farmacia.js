function calcularTotalCompra(itens) {
    let total = 0;
    for (let i = 0; i < itens.length; i++) {
        total += itens[i].quantidade * itens[i].preco;
    }
    return total;
}

const itensCompra = [];

for (let i = 0; i < 3; i++) {
    let nome = prompt(`Informe o nome do item ${i + 1}:`);
    let quantidade = parseInt(prompt(`Informe a quantidade do item ${i + 1}:`));
    let preco = parseFloat(prompt(`Informe o preço unitário do item ${i + 1}:`));

    itensCompra.push({ nome, quantidade, preco });
}

let calcularTotalCompra