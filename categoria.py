from datetime import datetime
ano = int(input(' Digite o ano de seu nascimento: '))
now = datetime.now()
idade = now.year - ano
if idade <= 9:
    print(' Categoria mirim')
elif idade <= 14:
    print(' Categoria infantil')
elif idade <= 19:
    print(' Categoria junior')
elif idade <= 20:
    print(' Categoria Sênior')
else:
    print(' Categoria master')
