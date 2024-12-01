cod_instrumento = input("Digite o código do instrumento (G, V, B, P): ")

if cod_instrumento == "G":
    preco = 1000
    instrumento = "Guitarra"
elif cod_instrumento == "V":
    preco = 800
    instrumento = "Violão"
elif cod_instrumento == "B":
    preco = 3000
    instrumento = "Bateria"
elif cod_instrumento == "P":
    preco = 200
    instrumento = "Pandeiro"
else:
    print("Código de instrumento inválido.")
    exit()

print(f"Você escolheu um(a) {instrumento} que custa {preco} R$.")