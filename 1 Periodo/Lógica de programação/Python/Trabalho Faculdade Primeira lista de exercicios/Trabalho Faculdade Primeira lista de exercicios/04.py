cod_operadora = input("Digite um código da operadora (C, V, O, T): ")

if cod_operadora == "C":
    print("Operadora: Claro")
elif cod_operadora == "V":
    print("Operadora: Vivo")
elif cod_operadora == "O":
    print("Operadora: Oi")
elif cod_operadora == "T":
    print("Operadora: Tim")
else: 
    print("Código de operadora inválida")