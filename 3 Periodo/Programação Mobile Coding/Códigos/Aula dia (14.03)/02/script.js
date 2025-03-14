function calcularRaizes() {
    let a = parseFloat(document.getElementById("a").value);
    let b = parseFloat(document.getElementById("b").value);
    let c = parseFloat(document.getElementById("c").value);

    if (isNaN(a) || isNaN(b) || isNaN(c)) {
        document.getElementById("resultado").innerText = "Por favor, insira valores a equação.";
        document.getElementById("equacao").innerText = "";
        return;
    }
    let equacao = `${a}x² ${b >= 0 ? '+' : ''} ${b}x ${c >= 0 ? '+' : ''} ${c} = 0`;
    document.getElementById("equacao").innerText = `Equação: ${equacao}`;

    let delta = b * b - 4 * a * c;

    if (delta > 0) {
        let x1 = (-b + Math.sqrt(delta)) / (2 * a);
        let x2 = (-b - Math.sqrt(delta)) / (2 * a);

        document.getElementById("resultado").innerText = `Duas raízes reais e diferentes: X1 = ${x1.toFixed(2)}, X2 = ${x2.toFixed(2)}`;
    } else if (delta === 0) {
        let x = -b / (2 * a);
        document.getElementById("resultado"). innerText = `Uma raiz real e única: X = ${x.toFixed(2)}`;
    } else {
        let real = (-b / (2 * a)).toFixed(2);
        let imaginaria = (Math.sqrt(-delta) / (2 * a)).toFixed(2);
        
        document.getElementById("resultado").innerText = `Raízes complexas: X1 = ${real} + ${imaginaria}i, X2 = ${real} - ${imaginaria}i`;
        }
    }