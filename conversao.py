
num = int(input(' Digite um número: '))
escolha = int(input(' Escolha qual conversão deseja \n 1 para Binário \n \
2 para octal \n 3 para hexadecimal \n Digite: '  ))
if escolha == 1:
    print(f'{bin(num)}'[2:])
elif escolha == 2:
    print(f'{oct(num)}'[2:])
elif escolha == 3 :
    print(f'{hex(num)}'[2:])
