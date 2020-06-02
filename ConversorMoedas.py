#Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
n = float(input('Quanto dinheiro você tem ? R$ '))
print(f'Com R${n} você pode comprar US${n/5.33 :.2f} doláres')
