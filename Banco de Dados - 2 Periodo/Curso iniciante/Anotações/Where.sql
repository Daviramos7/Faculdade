SELECT coluna1,coluna_n
FROM tabela
WHERE condicao;

    /*
    OPERADOR - DESCRIÇÃO
    =       IGUAL
    >       MAIOR QUE
    <       MENOR QUE
    >=      MAIOR QUE OU IGUAL QUE
    <=      MENOR QUE OU IGUAL QUE
    <>      DIFERENTE DE
    AND     OPERADOR LÓGICO E
    OR      OPERADOR LÓGICO OU
    */

    /*
    [DESAFIO] 
    a equipe de produção de produtos precisa do nome de todas as peças que pesam mais que 500kg mas não mais que 700 kg para inspeção
    */

    SELECT Name 
    FROM Production.Product
    WHERE Weight > 500 and Weight <= 700


    /*
    [DESAFIO]
    foi pedido pelo marketing uma relação de todos os empregados(employes) que são casados (married) e são asalariados
    */

    SELECT *
    FROM HumanResources.Employe
    Where MaritalSatus = 'm' AND SalariedFlag = 1


    /*
    um usuário chamado Peter Krebs está devendo um pagamento, consiga o email dele para que possamos enviar uma cobrança
    */

    SELECT *
    FROM Person.Person
    WHERE FirstName = 'peter' and LastName = 'krebs'

    SELECT * 
    FROM person.EmailAddress
    WHERE BusinessEntityID = 26
