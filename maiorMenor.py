num1 = int(input(' Digite o primeiro numero: '))
num2 = int(input(' Digite o segundo número: '))
num3 = int(input(' Digite o terceiro número: '))
maior = num1
if (num2 > maior):
    maior = num2
if (num3 > maior):
    maior = num3
print(f'Maior: {maior}')
menor = num1
if (num2 < menor):
    menor = num2
if (num3 < menor):
    menor = num3
print(f'Menor: {menor}')
