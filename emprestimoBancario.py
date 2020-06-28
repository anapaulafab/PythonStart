valorCasa = int(input(' Digite o valor da casa: '))
salario = int(input(' Digite seu salário: '))
parcelas = int(input( ' Digite em quantos anos deseja pagar: '))
valorParcela = valorCasa/(parcelas * 12)
calculoSalario = (salario*30/100)
if valorParcela <= calculoSalario:
    print(f'O valor da prestação será de {valorParcela:.2f}')
else: 
    print(' O valor da parcela excede 30% do seu salário !')


