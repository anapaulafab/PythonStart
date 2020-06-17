num = str(input(' Digite um numero de 0 a 9999: '))
SepararNumero = num.replace(""," ")
unidade = SepararNumero.split()[3]
dezena = SepararNumero.split()[2]
centena = SepararNumero.split()[1]
milhar = SepararNumero.split()[0]
print(f' Unidade: {(unidade)}\n Dezena: {(dezena)}\n Centena: {(centena)}\n Milhar: {milhar} ')

num = int(input(' Digite um numero de 0 a 9999: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print(f' Unidade: {(unidade)}\n Dezena: {(dezena)}\n Centena: {(centena)}\n Milhar: {milhar} ')
