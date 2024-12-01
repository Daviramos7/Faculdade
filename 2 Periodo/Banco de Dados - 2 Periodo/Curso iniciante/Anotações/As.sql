Usado para renomear informações

1- Encontrar o firstname e lastname person.person
    SELECT TOP 10 Firstname as "nome", lastname as "sobrenome"
    from person.person


2- ProductNumber da tabela production.product "Numero do Produto"
    SELECT TOP 10 ProductNumber as "Numero do Produto"
    from Production.Product


3- sales.salesorderdetail unitPrice "Preço Unitário"
    SELECT unitPrice as "Preço Unitário"
    FROM sales.salesorderdetail