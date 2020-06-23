r1 = float(input(' Informe o primeiro segmento: '))
r2 = float(input(' Informe o segundo segmento: '))
r3  = float(input(' Informe o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 +r3 and r3 <r1 +r2:
    print('Os segmentos formam um triangulo')
else:
    print('Os segmentos não formam um triangulo ')