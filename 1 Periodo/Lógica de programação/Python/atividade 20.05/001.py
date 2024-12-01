nomes = [['' for _ in range(2)] for _ in range(2)]
idades = [[0 for _ in range(2)] for _ in range(2)]

for i in range(2):
    for j in range(2):
        nomes[i][j] = input(f"Digite o nome para a posição [{i}] [{j}]: ")
        idades[i][j] = int(input(f"Digite a idade para a posição [{i}] [{j}]: "))

print("\nLista de nomes e idades equivalentes:")
for i in range(2):
    for j in range(2):
        print(f"Nome: {nomes[i][j]}, Idade: {idades[i][j]}")