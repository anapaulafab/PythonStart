from datetime import date
ano = int(input(' Digite o ano de seu nascimento: '))
now = date.today().year
idade = now - ano
if idade < 18 :
    print (' Ainda não chegou aos 18 anos!')
elif idade == 18:
    print (' Esse ano você deverá se alistar !')
elif idade > 18:
    print('Já passou da idade do alistamento!')