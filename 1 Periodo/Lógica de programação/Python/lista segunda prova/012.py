Numero = [0] * 10

for CONT in range(1, 11):
    Numero[CONT - 1] = 2 * CONT

for CONT in range(1, 11):
    print(f"Numero[{CONT}] := {Numero[CONT - 1]}")
