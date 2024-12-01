SELECT Nome_Coluna
FROM Tabela A, Tabela B
WHERE Condição

Eu quero encontrar (nome e data de contratação) de todos os funcionários que foram contratados no mesmo ano

SELECT A.firstname,A.hiredate,b.firstname,b.hiredate
FROM Employees A, Employees B
WHERE DATEPART(YEAR,a.hiredate) = DATEPART(YEAR,B.hiredate)