Monte um relatorio de todos os produtos cadastrados que tem o preço de venda acima da média

SELECT *
FROM Production.Product
WHERE ListPrice > (SELECT AVG(ListPrice) FROM Production.Product)

Eu quero saber o nome dos meus funcionários que tem o cargo de 'Design Engineer'

SELECT *
FROM person.person 
WHERE BunissesEntityID IN (
    SELECT BunissesEntityID FROM HumanResources.Employee
    WHERE JobTitle = 'Design Engineer'
)

