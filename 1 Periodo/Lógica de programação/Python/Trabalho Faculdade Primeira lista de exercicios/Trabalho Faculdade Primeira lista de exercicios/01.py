v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))

if v1 < v2:
    menor_valor = v1
elif v1 == v2:
    print("Os valores são iguais")
    exit()
else: 
    menor_valor = v2

print("O menor valor é:", menor_valor)