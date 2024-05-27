nome = []
episodio = []

for i in range(3):
    nomer = input(f'Qual nome da série {i+1}')
    episodior = int(input(f'Quantos episodios tem a série {nomer}'))
    nome.append(nomer)
    episodio.append(episodior)

total = sum(episodio)
media = total/len(episodio)
maximo = nome[episodio.index(max(episodio))]

print(f'Total de episodios é {total}')
print(f'Meida de episodios é {media}')
print(f'Seire com mais episodios {maximo}')