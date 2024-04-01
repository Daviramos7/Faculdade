n1 = float(input('Qual foi a sua primeira nota: '))
n2 = float(input('E a sua segunda nota: '))

med1 = n1 + n2
med2 = med1/2 

if med2 >= 7: 
    print('Você passou!')
elif med2 >= 4:
    print('Você foi para a recuperação!')
else: 
    print('Você foi reprovado!')