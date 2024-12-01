function mostraAvisoUm(){
    let nome = document.getElementById('nome').value
    if (nome.trim().length>2) {
        document.getElementById('avisoUm').innerHTML=""
    }
    else {
        document.getElementById('avisoUm').innerHTML="Mín. de 3 Caracteres"
    }
}

function mostraAvisoDois(){
    let senha = document.getElementById('senha').value
    if (senha.trim().length>2) {
        document.getElementById('avisoDois').innerHTML=""
    }
    else {
        document.getElementById('avisoDois').innerHTML="Mín. de 3 Caracteres"
    }

}

function redireciona(){
    let nome = document.getElementById('nome').value
    let senha = document.getElementById('senha').value
    // se o nome for maior que duas letras e a senha for maior que três letras, vai redirecionar a página dois
    if(nome.trim().length>2 && senha.trim().length>2) {
        alert('login feito com sucesso!')
        location.href = 'paginaDois.html'
    }
}