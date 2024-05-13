def encontra_maior_salario(nomes, salarios):
    indice_maior_salario = salarios.index(max(salarios))
    return nomes[indice_maior_salario]


nomes = []
salarios = []
for i in range(5):
    nome = input(f"Digite o nome {i+1}: ")
    nomes.append(nome)
    salario = float(input("Digite o salário: "))
    salarios.append(salario)

print("\n Lista de funcionários")
for nome, salario in zip(nomes, salarios):
    print(f"{nome}: R${salario:.2f}")

total_pago = sum(salarios)
print(f"\n O total a ser pago pela empresa é: R${total_pago:.2f}")

media = total_pago / 5 
print (f"A média salarial é de R$: {media:.2f}")

nome_maior_salario = encontra_maior_salario(nomes, salarios)
print(f"{nome_maior_salario} possui o maior salário")

maior_salario = max(salarios)
print (f"O maior salário é {maior_salario}")

