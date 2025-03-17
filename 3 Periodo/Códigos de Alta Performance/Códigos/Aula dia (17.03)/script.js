// Função callback -> é uma função que entra como entrada de parâmetro para uma outra função

// let contador = 0
// setInterval(()=>{//o arrow function em questão é um callback
//     document.body.innerHTML = contador
//     contador++
// }, 1000)//1000 milissegundos, que é 1 segundo

//métodos de array com uso de callback
//forEach -> ele executa uma função tanto quanto o número de elementos de um array

// let nomes = ['marlon', "carlos", 'maria', 'carol']
// //podemos entrar com atê 3 parâmetros elemento: marlon / index: 0
// nomes.forEach(function(elemento, index){
//     console.log(`Elemento: ${elemento}`)
//     console.log(`Índice: ${index}`)
// })

//método filter -> filtrar e devolver (return) um novo array a partir de alguma comparação
// let nomes = ['marlon', "carlos", 'maria', 'carol']

// let nomesPequenos = nomes.filter((e)=>{
//     return e.length < 6
// })//retorna um array cuja os elementos tem menos que 6 caracteres

// let nomesPequenos1 = nomes.filter((e)=>{
//     return e.includes('m')
// })//rastreie e retorne um array que possue uma letra específica
// console.log(nomesPequenos)


// let numeros = [6,10,5,2,7,21]
// //o método map -> ele retorna um array que a partir de alguma modificação necessária 
// let numerosCopia = numeros.map(function(e) {
//     return e*10
// })
// console.log(numerosCopia)

// JSON - Local Storage
// JSON -> javascript object notation 
// declarar um objeto javascript
// let usuario = {
//     nome: 'marlon',
//     idade: 36,
//     endereco: {
//         rua: 'aquela lá',
//         bairro: 'aquele outro',
//         numero: 6543
//     },
//     imprimeTudo: ()=>{
//         console.log(usuario)
//     }
// }
// como orientar um Objeto no js

// forma 1 -> usando ponto
// console.log(usuario.idade)

// // forma 2 -> usando colchete e string como entrada de parâmetro
// console.log(usuario['nome'])

// // possibilidade de misturar as orientações
// console.log(usuario.endereco.rua)
// console.log(usuario['endereco'] ['bairro'])
// console.log(usuario['endereco'].numero)

// // modificar os dados de um objeto
// usuario.nome = 'marcelo'
// console.log(usuario)

//mudança de estrutura de dados em um objeto
// usuario.id = 10
// console.log(usuario)

// conversão de objeto do tipo javascript para o formato JSON

// let usuario = {
//     nome: 'marlon',
//     idade: 36,
//     endereco: {
//         rua: 'aquela lá',
//         bairro: 'aquele outro',
//         numero: 6543
//     },
//     imprimeTudo: ()=>{
//         console.log(usuario)
//     }
// }
// console.log(usuario)
// objetos não podem ser renderizados de forma geral
// document.body.innerHTML = usuario.endereco.rua
// como converter objeto para forma string
// document.body.innerHTML = (JSON.stringify(usuario))
// console.log(typeof usuario)
// console.log(typeof JSON.stringify(usuario))
// // converter novamente para o formato objeto
// console.log(typeof JSON.parse(JSON.stringify(usuario)))
// document.body.innerHTML = JSON.stringify(usuario)
// let copia = JSON.stringify(usuario)
// console.log(typeof copia)
// console.log("-----*-----")
// copia = JSON.parse(copia)
// console.log(typeof copia)

// Local e Session Storage
// Session é um local de amarzenamento que duara apenas durante a sessão de um navegador, ou seja, apenas enquanto a janela está aberta
// Primeiro comando, como criar um espaço no session|local storage
// sessionStorage.setItem('nome', 'astrogildo')
// localStorage.setItem('nome', 'marlon')
// comandos para ler o session | local storage
// let nome = localStorage . getItem('nome')
// document.body.innerHTML = nome
// localStorage.setItem('novoNome', 'carol')

// como apagar todo o local storage
// localStorage.clear()

// como apagar uma chave específica no local storage
// localStorage.removeItem('nome')

// let contador = 0

// if(localStorage.getItem('guarda')){
//     contador = localStorage.getItem('guarda')
// }

// setInterval(()=>{//o arrow function em questão é um callback
//     document.body.innerHTML = contador
//     localStorage.setItem('guarda', contador)
//     contador++
// }, 1000)//1000 milissegundos, que é 1 segundo

// localStorage.setItem('nome', 'seupai')
// if(localStorage.getItem('nome')){
//     console.log("Existe")
// } else {
//     console.log("N existe")
// }

// let usuario = {
//     nome: 'mariana',
//     idade: 20
// }
// localStorage.setItem('usuario', JSON.stringify(usuario))
// let usuarioCopia = JSON.parse(localStorage.getItem('usuario'))
// console.log(usuarioCopia.nome)

// fetch -> consumo de API -> assíncrona
// qual a url da api?
// fetch("https://pokeapi.co/api/v2/pokemon/1000")
// // que tipo de dado você espera para retornar?
// .then(response => {
//     return response.json()
// })
// .then(data=>{
//     console.log(data.sprites.other['official-artwork'].front_default)
// })
// .catch(error=>{
//     console.log(error)
// })
// console.log('oi')