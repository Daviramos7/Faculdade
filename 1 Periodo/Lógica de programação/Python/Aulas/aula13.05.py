nomes = []

for i in range(3):
    nome = input("Digite um nome: ")
    nomes.append(nome)

print("\nLista de nomes digitados: ")
for cont, nome in enumerate(nomes, start = 1):
    print(cont, nome)

