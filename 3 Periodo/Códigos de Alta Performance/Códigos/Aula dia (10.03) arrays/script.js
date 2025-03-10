//aray - JS
//declaração
// todo array funciona num sistema de indexação
            // 0           1         2      n-1 = 3
let nomes = ['marlon', "carlos", `maria`, 'carol']

// como observar dados de um array em js
// console.log(nomes[0])

// sempre sei qual é o primeiro elemento de um array - elemento 0
//console.log(nomes[0])
//console.log(nomes)

// manipulação de um elemento de array
nomes[2] = "carina"
//console.log(nomes)

//como descobrir o tamanho de um array
//console.log("Tamanho do array: ",nomes.length)

//sempre sei como descobrir o último elemento de um array
//console.log("último índice do array:")
//console.log(nomes[nomes.length -1])

//JS é uma linguagem de variável dinâmica, portanto:
//let coisas = [marlon,true,36,()=>{console.log('oi')}, {nome:'marlon'}]
// console.log(coisas)
//coisas[0] = 32659
// console.log(coisas)
//let nomes = ['marlon', 'carlos', 'maria', 'carol']
//nomes[5] = 'huahua'
//console.log(nomes)

// métodos de array - sem
//let nomes = ['marlon', "carlos", `maria`, 'carol']

//pop e push
//nomes.push('marcelo') //adiciona ao último elemento do array
//console.log(nomes)
// nomes.pop() remove do último elemento do array e retorna o elemento retirado
//console.log(nomes.pop())
//console.log(nomes)

//shift e unshift
//let nomes = ['marlon', "carlos", `maria`, 'carol']
//nomes.unshift('brugunha') // adicionar ao primeiro elemento do array
//console.log(nomes)

//console.log(nomes.shift()) // remove do primeiro elemento do array e retorna o elemento removido
//console.log(nomes)

//crie um código que aceita 5 inserções de nomes em um array
//métode clássico usando o sistema de indexação
// método com métodos de array
// let nomes = []
// for(let i=0; i<=4; i++){
//     nomes.push(prompt('digite um nome'))
// }
// console.log(nomes)

//métodos indexOf -> acha o índice de um elemento do array, se existir, senão, devolve -1
// let nomes = ["marlon", "carlos", "maria", "carol"]
// console.log(nomes.indexOf('catrovenga'))
// crie um script que rastreia se o nome 'marlon' está no array usando o método indexOf
// for(let i=0; i<nomes.length; i++) {
//     if(nomes.indexOf('marlon') != -1) {
//         console.log("Marlon está no array")
//     }else{
//         console.log("Marlon não está no array")
//     }
// }

// toda string no js é um array
// let nome = 'maria'
// console.log(nome.length)

//sort -> método de organização
// let nomes = ['marlon', 'carlos', 'maria', 'carol']
// let numeros = [1,11,20,32,120,25,36,57]
// console.log(nomes.sort()) apenas para texto
// console.log(numeros.sort(function(a,b){
//     return a-b
// })) apenas para números

// let nomes = ['marlon', 'carlos', 'maria', 'carol']
// // console.log(nomes.includes('carlos')) //retornar se true ou false caso o elemento de busca não exista ou não está no array
// // faço uma remoção do array e retorna um novo array com os elementos, o primeiro parâmetro diz onde, o segundo quantos ele remove
// //console.log(nomes.splice(1,3))
// console.log(nomes)


// funções 
// declaração
// function imprime() {
//     console.log("biro biro")
// }
// execução
//imprime()

//funções auto-executáveis
// (function imprime() {
//     console.log("biro biro")
// })() 
//só executa uma vez, não dá para chamar de novo
// imprime()

//HOISTING
// console.log(x)
// let x = 10

// //HOISTING
// imprime()
// function imprime() {
//     console.log('biro biro')
// }

// funções anônimas
let x = function() {
    console.log('oi')
}
x()

let y = () =>{
    console.log('oi')
}
y()

// o caso do arrow function mais reduzido
// só pode haver uma linha de código no bloco de código
// só pode haver uma entrada no parâmetro
let z = a => console.log(a)
z('oi')
