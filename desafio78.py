# Faça um programa que leie 5 valores numericos e guarde-os
# em uma lista. No final, mostre qual foi o maior e o menor valor
#digitado e as sua respectivas posições na lista

listanum = list()
maior = 0
menor = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c ==0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]

print(f'Você digitou os valores{listanum}')
print(f' O maior valor é {maior} nas posições ', end ='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f' {i} ',end='')
print()
print(f'O menor valor é {menor} nas posições ', end='')
for i , v in enumerate(listanum):
    if v == menor:
        print(f' {i} ', end='')