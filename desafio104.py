#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 
# a função input() do python, só que fazendo a validação para aceitar apenas um valor numérico.
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Digite um numero inteiro valido')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Voce digitou o número {n}')