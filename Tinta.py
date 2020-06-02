#Faça um programa que leia a largura e altura de uma parede em metros, calcule sua área e quantidade de tinta
#necessária para pinta-la sabendo que cada litro de tinta, pinta uma área de 2m².

l = float(input('Informe a largura: '))
a = float(input('Informe a altura: '))
area = l * a
print(f'A quantidade de tinta necessária é de : {area/2} litros')
