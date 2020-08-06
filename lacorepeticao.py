for c in range(0,6):
    print('oi')
print('fim')

n = int(input)('Digite um número: ')
for c in range(0,n+1):
    print(c)
print('fim')    

i = int(input('inicio:'))
f = int(input('fim: '))
p = int(input('passo: '))
for c in range(i, f+1, p):
    print(c)
print('fim')    

s = 0
for c in range (0,4):
    n = int(input('Digite um valor: '))
    s += n
print(f' A soma é {s}')