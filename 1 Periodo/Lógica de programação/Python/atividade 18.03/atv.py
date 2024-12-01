meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

num_mes = int(input("Digite o número do mês: "))
mes_texto = meses.get(num_mes)

num_dia = int(input("Digite o número do dia: "))

ano_atual = 2024

print(f"{num_dia} de {mes_texto} de {ano_atual}")