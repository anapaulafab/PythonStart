num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))
escolha = 0
while escolha != 5:
    escolha = int(input('''Escolha uma opção:
[1] SOMA
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA
Digite: '''))
    if escolha == 1:
        print (f' A soma do {num1} + o {num2} é: {num1+num2}')
    if escolha == 2:
        print(f' A multiplicação do {num1} com o {num2}: é {num1 * num2}')
    if escolha == 3:
        maior = 0 
        if num1 > num2:
            maior = num1
        else:
             maior = num2
        print(f'O numero maior é: {maior}')
    if escolha == 4:
        num1 = int(input('Digite um valor: '))
        num2 = int(input('Digite um valor: '))
    elif escolha == 5:
        print('Fim do Programa')

    
