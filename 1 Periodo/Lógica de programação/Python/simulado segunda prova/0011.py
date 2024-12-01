clube = []
pontos = []

p = int(input('Quantos clubes voce quer no campeonato? '))

for i in range(p):
    nomer = input(f'Quantal nome do time {i+1}')
    pontor = int(input(f'Quantos pontos tem o time {nomer}'))
    clube.append(nomer)
    pontos.append(pontor)

campeao = clube[pontos.index(max(pontos))]

print(f'Campeao foi {campeao}')

