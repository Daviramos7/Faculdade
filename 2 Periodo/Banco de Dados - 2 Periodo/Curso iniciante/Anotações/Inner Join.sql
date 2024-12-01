SELECT C.ClientId,C.Nome,E.Rua, E.Cidade
FROM Cliente C
INNER JOIN Endereco E ON E.EnderecoId = C.EnderecoId

2 | Bruno | Rua Norte | São Paulof