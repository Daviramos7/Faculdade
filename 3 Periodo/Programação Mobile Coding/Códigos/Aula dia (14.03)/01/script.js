function calcularPreco() {
    let custoFabrica = parseFloat(document.getElementById("custoFabrica").value);
    if (isNaN(custoFabrica) || custoFabrica <= 0) {
        alert("Digite um valor válido para o custo de fábrica.");
        return;
    }

    let impostos = custoFabrica * 0.40;
    let lucroMontadora = custoFabrica * 0.45;
    let lucroConcessionaria = custoFabrica * 0.25;

    let precoFinal = custoFabrica + impostos + lucroMontadora + lucroConcessionaria;
    document.getElementById("resultado").innerText = "Valor total do carro: R$ " + precoFinal;
}