#Desenvolva um programa que leia o primeiro termo e a razão de um a P.A. No final mostre os 10 primeiros 
#termos dessa progressão

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
n = 10
ultimo = primeiro + (n-1) * razao
ultimo = ultimo + 1
for var in range (primeiro, ultimo, razao):
print(var)
