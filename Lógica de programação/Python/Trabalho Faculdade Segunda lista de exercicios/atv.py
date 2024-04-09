sabores = [
    "CHOCOLATE",
    "BAUNILHA",
    "FLOCOS",
    "COCO",
    "TAPIOCA",
    "MENTA"
]

litros_vendidos_total = 0
litros_estoque_total = 0
sabor_maior_vendido = ""
max_vendido = -1
sabor_maior_estoque = ""
max_estoque = -1

sabores_maior_vendido_que_estoque = []

for sabor in sabores:
    vendidos = float(input(f"Quantos litros de {sabor} foram vendidos? "))
    em_estoque = float(input(f"Quantos litros de {sabor} estão em estoque? "))

    litros_vendidos_total += vendidos
    litros_estoque_total += em_estoque

    if vendidos > max_vendido:
        max_vendido = vendidos
        sabor_maior_vendido = sabor

    if em_estoque > max_estoque:
        max_estoque = em_estoque
        sabor_maior_estoque = sabor

    if vendidos > em_estoque:
        sabores_maior_vendido_que_estoque.append((sabor, vendidos, em_estoque))

media_vendidos = litros_vendidos_total / len(sabores)
media_estoque = litros_estoque_total / len(sabores)

if sabores_maior_vendido_que_estoque:
    print("\nSabores com quantidade vendida maior que estoque:")
    for sabor, qtd_vendida, qtd_estoque in sabores_maior_vendido_que_estoque:
        print(f"{sabor}: quantidade vendida ({qtd_vendida} litros) > estoque ({qtd_estoque} litros)")

preco_venda_litro = 50
preco_estoque_litro = 20
arrecadacao_total = litros_vendidos_total * preco_venda_litro
valor_estoque_total = litros_estoque_total * preco_estoque_litro

print("\nResultados:")
print(f"Quantidade total de litros vendidos: {litros_vendidos_total} litros")
print(f"Quantidade total de litros em estoque: {litros_estoque_total} litros")
print(f"Média de litros vendidos por sabor: {media_vendidos:.2f} litros")
print(f"Média de litros em estoque por sabor: {media_estoque:.2f} litros")
print(f"Sabor com maior quantidade vendida: {sabor_maior_vendido} ({max_vendido} litros)")
print(f"Sabor com maior quantidade em estoque: {sabor_maior_estoque} ({max_estoque} litros)")
print(f"Arrecadação total com vendas: R${arrecadacao_total:.2f}")
print(f"Valor total em estoque: R${valor_estoque_total:.2f}")
