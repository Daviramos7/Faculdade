def ler_dados_pessoa():
    nome = input("Digite o seu nome: ")
    salario = float(input("Digite o seu salário: "))
    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura da pessoa: "))
    return (nome, salario, peso, altura)

def pessoa_mais_alta(pessoas):
    maior_altura = 0.0
    pessoa_mais_alta = None

    for pessoa in pessoas:
        nome, _, _, altura = pessoa
        if altura > maior_altura:
            maior_altura = altura
            pessoa_mais_alta = nome

    return pessoa_mais_alta, maior_altura

def calcular_medias(pessoas):
    total_salarios = sum(pessoa[1] for pessoa in pessoas)
    total_pesos = sum(pessoa[2] for pessoa in pessoas)
    qtd_pessoas = len(pessoas)

    media_salario = total_salarios / qtd_pessoas
    media_peso = total_pesos / qtd_pessoas
    
    return(media_salario, media_peso)

def main():
    pessoas = []

    for _ in range(3):
        pessoa = ler_dados_pessoa()
        pessoas.append(pessoa)
    
    mais_alta, altura_mais_alta = pessoa_mais_alta(pessoas)

    media_salario, media_peso = calcular_medias(pessoas)

    print(f"A pessoa mais alta é: {mais_alta} com altura de {altura_mais_alta} metros.")
    print(f"A média de salário das três pessoas é: {media_salario:.2f}")
    print(f"A média de peso das três pessoas é: {media_peso:.2f}")

if __name__ == "__main__" :
    main()
    