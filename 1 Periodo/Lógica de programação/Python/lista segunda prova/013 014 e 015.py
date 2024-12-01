# Programa completo que inclui as partes 13, 14 e 15

# Parte 13: Armazenar dados dos seriados
NomeSeriado = [""] * 3
QuantidadeEpisodios = [0] * 3
TotalEpisodios = 0
MaxEpisodios = 0
MaxIndex = 0

# Recebendo os dados dos seriados
for i in range(3):
    NomeSeriado[i] = input("Informe o nome do seriado: ")
    QuantidadeEpisodios[i] = int(input("Informe a quantidade de episodios: "))
    TotalEpisodios += QuantidadeEpisodios[i]
    if QuantidadeEpisodios[i] > MaxEpisodios:
        MaxEpisodios = QuantidadeEpisodios[i]
        MaxIndex = i

# Calculando a média de episódios
MediaEpisodios = TotalEpisodios / 3

# Exibindo os resultados
print(f"Total de episodios: {TotalEpisodios}")
print(f"Media de episodios por serie: {MediaEpisodios:.2f}")
print(f"Seriado com mais episodios: {NomeSeriado[MaxIndex]}")

# Parte 14: Listar os vetores de trás para frente
print("\nListando os seriados de trás para frente:")
for i in range(2, -1, -1):
    print(f"Seriado: {NomeSeriado[i]}, Episodios: {QuantidadeEpisodios[i]}")

# Parte 15: Geração de números pares de 0 a 500
print("\nNúmeros pares de 0 a 500:")
for i in range(0, 501, 2):
    print(i)
