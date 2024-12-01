O having é usado em junção com o group by para filtrar resultados de um agrupamento

é como se fosse um where para dados agrupados

    SELECT coluna1,funcaoAgregacao(coluna2)
    FROM nomeTabela
    GROUP BY coluna1
    HAVING condicao;

A diferença entre having e where.
é que o having é aplicado depois que os dados já foram agrupados, enquanto o where é aplicado antes dos dados serem agrupados


1- Estamos querendo identificar as provincias(stateProvinceID) com o maior numero de cadastros no nosso sistema, então é preciso encontra quais províncias (stateProvinceID) estão registradas no banco de dados mais que 1000 vezes

    SELECT stateProvinceID,COUNT(stateProvinceID) as "quantidade"
    FROM person.Address
    GROUP BY stateProvinceID
    HAVING COUNT(stateProvinceID) > 1000

2- Sendo que se trata de uma mutinacional os gerentes querem saber quais produtos (ProductID) não estão trazendo em média no mínimo 1 milhão em total de vendas (Linetotal)

    SELECT productid,AVG(Linetotal) as "quantidade"
    FROM sales.salesorderdetail
    Group BY productid
    HAVING AVG(Linetotal) < 1000000