velocidade = int(input('Digite a velocidade do carro: '))
if velocidade >= 80:
    multa = (velocidade - 80)*7
    print(f'Você foi multado! A multa é de R$ {multa}')
print('Tenha um bom dia! ')