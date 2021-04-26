cont=1
while True:
    print(cont,'-', end='')
    cont+=1
print('Acabou')

#UTILIZANDO BREAK PARA CRIAR UMA INTERRUPÇÃO
n = s = 0
while True:
    n= int(input('Digite um numero: '))
    if n == 999:
        break
    s+=n
print(f' A soma vale {s}')

