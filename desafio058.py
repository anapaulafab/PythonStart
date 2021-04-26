import random
tentativas=0
numero = random.randint(a = 0 , b = 10)
numUsuario = int(input('Advinhe um número de 1 a 10:'))
while numUsuario != numero:
    print('Você errou! Continue !')
    numUsuario = int(input('Advinhe um número de 1 a 10:'))
    tentativas = tentativas + 1
    if numUsuario == numero:
        print(f'Parabéns você acertou o número {numero} com {tentativas} tentativas')
   
