-O GROUP BY basicamente divide o resultado da sua pesquisa em grupos
-Para cada grupo você pode aplicar uma função de agregação, por exemplo:
    -calcular a soma de itens
    -contar o número de itens naquele grupo

SELECT coluna1,funcaoAgregacao(coluna2)
FROM nomeTabela
GROUP BY coluna1;

1- Eu preciso saber quantas pessoas tem o mesmo MiddleName agrupadas por o MiddleName
    SELECT MiddleName,COUNT(MiddleName) as "Quantidade"
    FROM Person.Person
    GROUP BY MiddleName

2- Eu preciso saber em média qual é a quantidade que cada produto é vendido na loja
    SELECT ProductID, AVG(OrderQty) as "Média"
    FROM sales.salesorderdetail
    GROUP BY ProductID

3- Eu quero saber qual foram as 10 vendas que no totla tiveram os maiores valores de venda(line total) por produto maior valor para o menor
    SELECT TOP 10 productid,SUM(Linetotal)
    FROM sales.salesorderdetail
    GROUP BY productid
    ORDER BY SUM(Linetotal) DESC;

4- Eu preciso saber quantos produtos e qual a quantidade media de produtos que temos cadastrados nas nossas ordem de serviço (WorkOrder), agrupados por ProductID

    SELECT ProductID,COUNT(ProductID) as "contagem",
    AVG(OrderQty) as "media"
    FROM Production.WorkOrder
    GROUP BY ProductID