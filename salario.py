salario = float(input( 'Digite o salário: '))
if salario > 1250:
    print(f'O salário com aumento de 10% será de {salario+salario*10/100:.2f} reais')
else:
    print(f'O salário com aumento de 15% será de {salario+salario*15/100:.2f} reais')
