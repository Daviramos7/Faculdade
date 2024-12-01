amigos = {}


def calcular_parcelas(valor_total):
    num_parcelas = int(input("Quantas parcelas deseja? (1 a 3): "))
    valor_parcela = valor_total / num_parcelas
    print(f"O valor de cada parcela é: R${valor_parcela:.2f}")


def calcular_estatisticas():
    total_assistiram_dois_filmes = 0
    arrecadacao_total = 0
    arrecadacao_pix = 0
    arrecadacao_dinheiro = 0
    arrecadacao_cartao = 0
    total_meia = 0
    total_inteira = 0
    arrecadacao_meia = 0
    arrecadacao_inteira = 0

    for amigo, dados in amigos.items():
        arrecadacao_total += dados["valor"]
        if dados["modalidade"] == "PIX":
            arrecadacao_pix += dados["valor"]
        elif dados["modalidade"] == "DINHEIRO":
            arrecadacao_dinheiro += dados["valor"]
        elif dados["modalidade"] == "CARTÃO":
            arrecadacao_cartao += dados["valor"]
            if dados["parcelas"] > 1:
                print(f"Parcelas para {amigo}:")
                calcular_parcelas(dados["valor"])

        if amigo in amigos_oppenheimer:
            total_assistiram_dois_filmes += 1

        if dados["tipo_entrada"] == "Meia":
            total_meia += 1
            arrecadacao_meia += dados["valor"]
        else:
            total_inteira += 1
            arrecadacao_inteira += dados["valor"]

    print("\n--- Estatísticas ---")
    print(f"Quantidade de pessoas que assistiram aos dois filmes: {total_assistiram_dois_filmes}")
    print(f"Arrecadação total do cinema: R${arrecadacao_total:.2f}")
    print(f"Arrecadacao média por pessoa: R${arrecadacao_total / len(amigos):.2f}")
    print(f"Arrecadação por modalidade: ")
    print(f"    - PIX: R${arrecadacao_pix:.2f}")
    print(f"    - Dinheiro: R${arrecadacao_dinheiro:.2f}")
    print(f"    - Cartão: R${arrecadacao_cartao:.2f}")
    print(f"Quantidade de pessoas que pagaram meia: {total_meia}")
    if total_meia > total_inteira:
        print("Mais pessoas pagaram meia do que inteira.")
    elif total_meia < total_inteira:
        print("Mais pessoas pagaram inteira do que meia.")
    else:
        print("O mesmo número de pessoas pagaram meia e inteira.")
    print(f"Arrecadação total da meia entrada: R${arrecadacao_meia:.2f}")
    print(f"Arrecadação total da entrada inteira: R${arrecadacao_inteira:.2f}")


for i in range(1, 5):
    nome = input(f"Nome do {i}º amigo: ")
    tipo_entrada = input(f"{nome}, sua entrada é meia ou inteira? ").capitalize()
    valor_entrada = 50 if tipo_entrada == "Meia" else 100
    modalidade = input(f"{nome}, como você vai pagar? (PIX, Dinheiro ou Cartão): ").upper()
    parcelas = 1
    if modalidade == "CARTÃO":
        parcelas = int(input(f"{nome}, quantas parcelas deseja? (1 a 3): "))
    amigos[nome] = {"tipo_entrada": tipo_entrada, "valor": valor_entrada, "modalidade": modalidade, "parcelas": parcelas}

print("\n--- Dados dos Amigos ---")
for amigo, dados in amigos.items():
    print(f"Nome: {amigo}, Tipo de entrada: {dados['tipo_entrada']}, Valor: R${
            dados['valor']:.2f}, Modalidade: {dados['modalidade']}")

print("\nAgora vamos ver quem irá assistir o filme do Oppenheimer...")

amigos_oppenheimer = []
for amigo, dados in amigos.items():
    opcao = input(f"{amigo}, você gostaria de assistir ao filme do Oppenheimer (S/N) ").upper()
    if opcao == "S":
        amigos_oppenheimer.append(amigo)

print("\n--- Estatísticas após assistir aos dois filmes ---")
calcular_estatisticas()
