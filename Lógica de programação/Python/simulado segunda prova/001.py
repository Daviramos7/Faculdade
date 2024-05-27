clubes = []
pontos = []

def add_clube_pontos(nome, pontos_clube):
    clubes.append(clubes)
    pontos.append(pontos_clube)

def enc_clube_mais_pontos():
    campeao = clubes[pontos.index(max(pontos))]
    return campeao

while True:
    nome = input("Digite o nome do clube (Ou digite fim para encerrar): ")
    if nome.lower() == 'fim':
        break
    pontos_clube = int(input("Digite os pontos do clube {}:".format(nome)))
    add_clube_pontos(nome, pontos_clube)

enc_clube_mais_pontos()
print(enc_clube_mais_pontos)

