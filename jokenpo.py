from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''[0]PEDRA
[1]PAPEL
[2]TESOURA''')
jogador = int(input('Sua jogada: '))
print('jo')
sleep(1)
print('ken')
sleep(1)
print('po!')
print(f'Computador: {itens[computador]}')
print(f'Jogador: {itens[jogador]}')
if computador == 0: # comp jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR GANHOU')
    elif jogador == 2:
        print('COMPUTADOR GANHOU')
    else:
        print('joagada inválida')
if computador == 1: #comp jogou papel
    if jogador == 0:
        print('COMPUTADOR GANHOU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR GANHOU')
    else:
        print('joagada inválida')
if computador == 2: #comp jogou tesoura
    if jogador == 0:
        print('JOGADOR GANHOU')
    elif jogador == 1:
        print('COMPUTADOR GANHOU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('joagada inválida')