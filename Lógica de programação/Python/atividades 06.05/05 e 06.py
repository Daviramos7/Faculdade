soma_salarios = 0

for i in range(5):
    salario = float(input(f"Digite o {i+1} salário: "))
    soma_salarios += salario

media_salarios = soma_salarios / 5

print("Soma dos salários:", soma_salarios)
print("Média dos salários:", media_salarios)