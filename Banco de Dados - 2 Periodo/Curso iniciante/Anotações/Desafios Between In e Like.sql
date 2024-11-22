1- Quantos produtos temos cadastrados no sistema que custam mais que 1500 dolares

SELECT count(listprice)
FROM production.product
WHERE ListPrice > 1500

2- Quantas pessoas temos com o sobrenome que inicia com a letra P

SELECT count(lastName)
FROM Person.person
WHERE LastName like 'p%'

3- Em quantas cidades únicas estão cadastrados nossos clientes 

SELECT count(distinct(city))
FROM person.Address

4- Quais são as cidades únicas que temos cadastrados em nosso sistema

SELECT distinct(city)
FROM person.Address

5- Quantos produtos vermelhs tem preço entre 500 a 1000 dolares

SELECT count(*)
FROM production.product
WHERE color = 'red'
AND ListPrice between 500 and 1000

6- Quantos produtos cadastrados tem a palavra 'road' no nome deles

SELECT count(*)
FROM production.product
WHERE name like '%road%'