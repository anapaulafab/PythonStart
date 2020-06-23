distancia = float(input('Qual a distancia em KM ?: '))
if distancia <= 200:
    print(f'Sua passagem será de {distancia * 0.50:.2f} reais')
else:
    print (f'Sua passagem será de {distancia * 0.45:.2f}')
