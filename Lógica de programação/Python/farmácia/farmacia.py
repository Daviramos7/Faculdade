def calcular_total_compra(itens):
    total = 0
    for item in itens:
        total += item['quantidade'] * item['preco']
    return total


itens_compra = []

for i in range(3):
    nome = input(f"Informe o nome do item {i + 1}: ")
    quantidade = int(input(f"Informe a quantidade do item {i + 1}: "))
    preco = float(input(f"Informe o preço unitário do item {i + 1}: "))
    itens_compra.append(
        {'nome': nome, 'quantidade': quantidade, 'preco': preco})

total_compra = calcular_total_compra(itens_compra)

forma_pagamento = input("Informe a forma de pagamento (pix ou cartão): ")

if forma_pagamento == "pix":
    total_compra *= 0.90
elif forma_pagamento == "cartão":
    total_compra *= 1.05

inserir_cpf = input("Deseja inserir o CPF? (sim ou não): ")

if inserir_cpf == "sim":
    total_compra *= 0.90

print(f"Total a pagar: R$ {total_compra:.2f}")
