function converterParaBinario() {
    let decimal = parseInt(document.getElementById("decimal").value);
    
    if (isNaN(decimal) || decimal < 0) {
        document.getElementById("resultado").innerText = "Por favor insira um número válido";
        return;
    }

    let binario = "";
    let numero = decimal;
    let passos = [];

    while (numero > 0 ) {
        let resto = numero % 2;
        passos.push(`${numero} + 2 = ${Math.floor(numero / 2)}, resto ${resto}`);
        binario = resto + binario;
        numero = Math.floor(numero / 2);
    }

    if (binario === "") binario = "0";

    let resultadoTexto = `Valor decimal: ${decimal} <br> Processo de conversão <br> ${passos.reverse().join("<br>")} <br><br> Valor em binário: <strong>${binario}<strong>`;

    document.getElementById("resultado").innerHTML = resultadoTexto;

}
