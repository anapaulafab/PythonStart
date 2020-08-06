# 6 numeros inteiros a soma só de pares - impares desconsiderar
s=0
for c in range (1,7):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2==0:
        s+=n
print(f'Soma dos numeros Pares: {s}')
print('fim')