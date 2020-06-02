#Faça um algoritimo que leia o salario de um funcionário e mostre seu novo salário com 15% de aumento

n = float(input(' Qual o salário? R$ '))
print(f' Seu salário com reajuste de 15% é de R${n+n*15/100:.2f}')
