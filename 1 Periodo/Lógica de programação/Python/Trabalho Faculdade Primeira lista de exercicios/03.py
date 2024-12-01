num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
resultado = num1 + num2

if num3 > resultado:
    print("Terceiro número é maior que a soma dos dois primeiros números.")
elif num3 == resultado:
    print("O Terceiro número é igual a soma dos dois primeiros")
else:
    print("Terceiro número é menor que a soma dos dois primeiros números.")
