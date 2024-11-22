SELECT coluna1,coluna2
FROM tabela
ORDER BY coluna1 asc/desc

/*
DESAFIO 1
Obter o ProductID dos 10 produtos mais caros cadastrados no sistema, listando do mais caro para o mais barato
*/

SELECT TOP 10 ProductID
FROM Production.product
ORDER BY listprice desc

/*
DESAFIO 2
Obter o nome e numero do produto dos produtos que tem o ProductID entre 1~4
*/

SELECT TOP 4 name,productnumber
FROM production.product
ORDER BY ProductID