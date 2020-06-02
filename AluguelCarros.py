
dias = int(input(' Qual a quantidade de dias alugados? '))
km = float(input(' Quantos KM rodados? '))
print(f' O total a pagar é de R$ {(dias*60) + (km*0.15) :.2f}')
