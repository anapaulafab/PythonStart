#ano de nascimento de 7 pessoas quantas maiores de 18 e quantas menores de 18
from datetime import date
menor=0
maior=0
for c in range (1,8):
    dn = int(input(f'Em que ano a {c}ª data de nascimento: '))
    now = date.today().year
    idade = now - dn
    if idade >=21:
        maior+=1
    else:
        menor+=1
print(f'São {menor} menores de idade')
print(f'São {maior} maiores de idade')

