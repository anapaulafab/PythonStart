#faça um programa que leia um numero inteiro e diga se ele é ou nao um numero primo

numero = int(input('Digite um numero: '))
tot=0
for c in range (1, numero + 1):
    if numero % c ==0:
        tot+=1
if tot ==2:
    print('É numero primo')
else:
    print('Não é primo')
